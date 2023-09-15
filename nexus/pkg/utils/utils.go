package utils

import (
	"crypto/md5"
	b64 "encoding/base64"
)

func NilIfZero[T comparable](x T) *T {
	var zero T
	if x == zero {
		return nil
	}
	return &x
}

func ComputeB64MD5(data []byte) (string, error) {
	hasher := md5.New()
	_, err := hasher.Write(data)
	if err != nil {
		return "", err
	}
	return b64.StdEncoding.EncodeToString(hasher.Sum(nil)), nil
}
