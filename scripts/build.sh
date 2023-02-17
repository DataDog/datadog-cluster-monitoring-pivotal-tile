#!/usr/bin/env bash

set -e

pushd tile/

# build artifact
tile build $VERSION

popd
