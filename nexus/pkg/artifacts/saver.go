package artifacts

import (
	"context"
	"fmt"
	"os"
	"time"

	"github.com/Khan/genqlient/graphql"

	"github.com/wandb/wandb/nexus/internal/gql"
	"github.com/wandb/wandb/nexus/internal/uploader"
	"github.com/wandb/wandb/nexus/pkg/observability"
	"github.com/wandb/wandb/nexus/pkg/service"
	"github.com/wandb/wandb/nexus/pkg/utils"
)

type ArtifactSaver struct {
	// Resources.
	Ctx           context.Context
	Logger        *observability.NexusLogger
	GraphqlClient graphql.Client
	UploadManager *uploader.UploadManager
	// Input.
	Artifact    *service.ArtifactRecord
	HistoryStep int64
}

func NewArtifactSaver(
	ctx context.Context,
	logger *observability.NexusLogger,
	graphQLClient graphql.Client,
	uploadManager *uploader.UploadManager,
	artifact *service.ArtifactRecord,
	historyStep int64,
) ArtifactSaver {
	return ArtifactSaver{
		Ctx:           ctx,
		Logger:        logger,
		GraphqlClient: graphQLClient,
		UploadManager: uploadManager,
		Artifact:      artifact,
		HistoryStep:   historyStep,
	}
}

func (as *ArtifactSaver) createArtifact() (
	attrs gql.CreateArtifactCreateArtifactCreateArtifactPayloadArtifact, rerr error) {
	aliases := []gql.ArtifactAliasInput{}
	for _, alias := range as.Artifact.Aliases {
		aliases = append(aliases,
			gql.ArtifactAliasInput{
				ArtifactCollectionName: as.Artifact.Name,
				Alias:                  alias,
			},
		)
	}
	response, err := gql.CreateArtifact(
		as.Ctx,
		as.GraphqlClient,
		as.Artifact.Entity,
		as.Artifact.Project,
		as.Artifact.Type,
		as.Artifact.Name,
		&as.Artifact.RunId,
		as.Artifact.Digest,
		utils.NilIfZero(as.Artifact.Description),
		aliases,
		utils.NilIfZero(as.Artifact.Metadata),
		utils.NilIfZero(as.Artifact.TtlDurationSeconds),
		utils.NilIfZero(as.HistoryStep),
		utils.NilIfZero(as.Artifact.DistributedId),
		as.Artifact.ClientId,
		as.Artifact.SequenceClientId,
	)
	if err != nil {
		return gql.CreateArtifactCreateArtifactCreateArtifactPayloadArtifact{}, err
	}
	return response.GetCreateArtifact().GetArtifact(), nil
}

func (as *ArtifactSaver) createManifest(
	artifactId string, baseArtifactId *string, manifestDigest string, includeUpload bool,
) (attrs gql.CreateArtifactManifestCreateArtifactManifestCreateArtifactManifestPayloadArtifactManifest, rerr error) {
	manifestType := gql.ArtifactManifestTypeFull
	manifestFilename := "wandb_manifest.json"
	if as.Artifact.IncrementalBeta1 {
		manifestType = gql.ArtifactManifestTypeIncremental
		manifestFilename = "wandb_manifest.incremental.json"
	} else if as.Artifact.DistributedId != "" {
		manifestType = gql.ArtifactManifestTypePatch
		manifestFilename = "wandb_manifest.patch.json"
	}

	response, err := gql.CreateArtifactManifest(
		as.Ctx,
		as.GraphqlClient,
		artifactId,
		baseArtifactId,
		manifestFilename,
		manifestDigest,
		as.Artifact.Entity,
		as.Artifact.Project,
		as.Artifact.RunId,
		manifestType,
		includeUpload,
	)
	if err != nil {
		return gql.CreateArtifactManifestCreateArtifactManifestCreateArtifactManifestPayloadArtifactManifest{}, err
	}
	return response.GetCreateArtifactManifest().ArtifactManifest, nil
}

func (as *ArtifactSaver) uploadFiles(artifactID string, manifest Manifest, manifestID string) error {
	const batchSize int = 10000
	const maxBacklog int = 10000

	type TaskResult struct {
		Task *uploader.UploadTask
		Name string
	}

	// Prepare all file specs.
	fileSpecs := []gql.CreateArtifactFileSpecInput{}
	for name, entry := range manifest.Contents {
		if entry.LocalPath == nil {
			continue
		}
		fileSpec := gql.CreateArtifactFileSpecInput{
			ArtifactID:         artifactID,
			Name:               name,
			Md5:                entry.Digest,
			ArtifactManifestID: &manifestID,
		}
		fileSpecs = append(fileSpecs, fileSpec)
	}

	// Upload in batches.
	numInProgress, numDone := 0, 0
	nameToScheduledTime := map[string]time.Time{}
	taskResultsChan := make(chan TaskResult)
	fileSpecsBatch := make([]gql.CreateArtifactFileSpecInput, 0, batchSize)
	var startTime, subStartTime time.Time
	for numDone < len(fileSpecs) {
		startTime = time.Now()
		// Prepare a batch.
		now := time.Now()
		fileSpecsBatch = fileSpecsBatch[:0]
		for _, fileSpec := range fileSpecs {
			if _, ok := nameToScheduledTime[fileSpec.Name]; ok {
				continue
			}
			nameToScheduledTime[fileSpec.Name] = now
			fileSpecsBatch = append(fileSpecsBatch, fileSpec)
			if len(fileSpecsBatch) >= batchSize {
				break
			}
		}
		if len(fileSpecsBatch) > 0 {
			// Fetch upload URLs.
			subStartTime = time.Now()
			response, err := gql.CreateArtifactFiles(
				as.Ctx,
				as.GraphqlClient,
				fileSpecsBatch,
				gql.ArtifactStorageLayoutV2,
			)
			fmt.Println("  got signed URLs in", time.Since(subStartTime))
			if err != nil {
				return err
			}
			if len(fileSpecsBatch) != len(response.CreateArtifactFiles.Files.Edges) {
				return fmt.Errorf(
					"expected %v upload URLs, got %v",
					len(fileSpecsBatch),
					len(response.CreateArtifactFiles.Files.Edges),
				)
			}
			// Save birth artifact ids, schedule uploads.
			for i, edge := range response.CreateArtifactFiles.Files.Edges {
				name := fileSpecsBatch[i].Name
				entry := manifest.Contents[name]
				entry.BirthArtifactID = &edge.Node.Artifact.Id
				manifest.Contents[name] = entry
				if edge.Node.UploadUrl == nil {
					numDone++
					continue
				}
				numInProgress++
				task := &uploader.UploadTask{
					Path:    *entry.LocalPath,
					Url:     *edge.Node.UploadUrl,
					Headers: edge.Node.UploadHeaders,
					CompletionCallback: func(task *uploader.UploadTask) {
						taskResultsChan <- TaskResult{task, name}
					},
				}
				as.UploadManager.AddTask(task)
			}
		}
		// Wait for uploader to catch up. If there's nothing more to schedule, wait for all in progress tasks.
		subStartTime = time.Now()
		for numInProgress > maxBacklog || (len(fileSpecsBatch) == 0 && numInProgress > 0) {
			numInProgress--
			result := <-taskResultsChan
			if result.Task.Err != nil {
				// We want to retry when the signed URL expires. However, distinguishing that error from others is not
				// trivial. As a heuristic, we retry if the request failed more than an hour after we fetched the URL.
				if time.Since(nameToScheduledTime[result.Name]) < 1*time.Hour {
					return result.Task.Err
				}
				delete(nameToScheduledTime, result.Name) // retry
				continue
			}
			numDone++
		}
		fmt.Println("  waited for uploader to catch up in", time.Since(subStartTime))
		fmt.Println("Batch time", time.Since(startTime))
	}
	return nil
}

func (as *ArtifactSaver) uploadManifest(manifestFile string, uploadUrl *string, uploadHeaders []string) error {
	resultChan := make(chan *uploader.UploadTask)
	task := &uploader.UploadTask{
		Path:    manifestFile,
		Url:     *uploadUrl,
		Headers: uploadHeaders,
		CompletionCallback: func(task *uploader.UploadTask) {
			resultChan <- task
		},
	}
	as.UploadManager.AddTask(task)
	<-resultChan
	return task.Err
}

func (as *ArtifactSaver) commitArtifact(artifactId string) {
	response, err := gql.CommitArtifact(
		as.Ctx,
		as.GraphqlClient,
		artifactId,
	)
	if err != nil {
		err = fmt.Errorf("CommitArtifact: %s, error: %+v response: %+v", as.Artifact.Name, err, response)
		as.Logger.CaptureFatalAndPanic("commitArtifact", err)
	}
}

func (as *ArtifactSaver) Save() (artifactID string, rerr error) {
	manifest, err := NewManifestFromProto(as.Artifact.Manifest)
	if err != nil {
		return "", err
	}

	artifactAttrs, err := as.createArtifact()
	if err != nil {
		return "", fmt.Errorf("ArtifactSaver.createArtifact: %w", err)
	}
	artifactId := artifactAttrs.Id
	var baseArtifactId *string
	if as.Artifact.BaseId != "" {
		baseArtifactId = &as.Artifact.BaseId
	} else if artifactAttrs.ArtifactSequence.LatestArtifact != nil {
		baseArtifactId = &artifactAttrs.ArtifactSequence.LatestArtifact.Id
	}
	if artifactAttrs.State == gql.ArtifactStateCommitted {
		if as.Artifact.UseAfterCommit {
			_, err := gql.UseArtifact(
				as.Ctx,
				as.GraphqlClient,
				as.Artifact.Entity,
				as.Artifact.Project,
				as.Artifact.RunId,
				artifactId,
			)
			if err != nil {
				return "", fmt.Errorf("gql.UseArtifact: %w", err)
			}
		}
		return artifactId, nil
	}
	// DELETED is for old servers, see https://github.com/wandb/wandb/pull/6190
	if artifactAttrs.State != gql.ArtifactStatePending && artifactAttrs.State != gql.ArtifactStateDeleted {
		as.Logger.CaptureFatalAndPanic(
			"ArtifactSaver", fmt.Errorf("unexpected artifact state %v", artifactAttrs.State),
		)
	}

	manifestAttrs, err := as.createManifest(
		artifactId, baseArtifactId, "" /* manifestDigest */, false, /* includeUpload */
	)
	if err != nil {
		return "", fmt.Errorf("ArtifactSaver.createManifest: %w", err)
	}

	err = as.uploadFiles(artifactId, manifest, manifestAttrs.Id)
	if err != nil {
		return "", fmt.Errorf("ArtifactSaver.uploadFiles: %w", err)
	}

	manifestFile, manifestDigest, err := manifest.WriteToFile()
	if err != nil {
		return "", fmt.Errorf("ArtifactSaver.writeManifest: %w", err)
	}
	defer os.Remove(manifestFile)
	manifestAttrs, err = as.createManifest(artifactId, baseArtifactId, manifestDigest, true /* includeUpload */)
	if err != nil {
		return "", fmt.Errorf("ArtifactSaver.createManifest: %w", err)
	}
	err = as.uploadManifest(manifestFile, manifestAttrs.File.UploadUrl, manifestAttrs.File.UploadHeaders)
	if err != nil {
		return "", fmt.Errorf("ArtifactSaver.uploadManifest: %v", err)
	}

	as.commitArtifact(artifactId)

	return artifactId, nil
}
