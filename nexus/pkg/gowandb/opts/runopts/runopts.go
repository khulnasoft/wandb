// sub-package for gowandb run options
package runopts

import (
	"github.com/wandb/wandb/nexus/pkg/gowandb/runconfig"
)

type RunParams struct {
	Config *runconfig.Config
	Name   *string
	RunID  *string
}

type RunOption func(*RunParams)

func WithConfig(config runconfig.Config) RunOption {
	return func(p *RunParams) {
		p.Config = &config
	}
}

func WithName(name string) RunOption {
	return func(p *RunParams) {
		p.Name = &name
	}
}

func WithRunID(runID string) RunOption {
	return func(p *RunParams) {
		p.RunID = &runID
	}
}