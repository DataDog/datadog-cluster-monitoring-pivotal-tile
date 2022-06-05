#!/usr/bin/env bash

set -e

RESOURCES_DIR="tile/resources"

AGENT_VERSION=${AGENT_VERSION:-4.9.2}
CLUSTER_AGENT_VERSION=${CLUSTER_AGENT_VERSION:-2.1.1}
NOZZLE_RELEASE_VERSION=${NOZZLE_RELEASE_VERSION:-85}

# download agent bosh release tarball
curl -L "https://cloudfoundry.datadoghq.com/datadog-agent/datadog-agent-boshrelease-$AGENT_VERSION.tgz" -o $RESOURCES_DIR/datadog-agent-boshrelease.tgz

# download cluster agent bosh release tarball
curl -L "https://cloudfoundry.datadoghq.com/datadog-cluster-agent/datadog-cluster-agent-boshrelease-$CLUSTER_AGENT_VERSION.tgz" -o $RESOURCES_DIR/datadog-cluster-agent-boshrelease.tgz

# download nozzle bosh release tarball
curl -L "https://cloudfoundry.datadoghq.com/datadog-firehose-nozzle/datadog-firehose-nozzle-release-$NOZZLE_RELEASE_VERSION.tgz" -o $RESOURCES_DIR/datadog-firehose-nozzle-release.tgz

# install tile-generator
if ! [ command -v tile 2>&1 >/dev/null ] ; then
    curl -L "https://github.com/cf-platform-eng/tile-generator/releases/download/v14.0.5/tile_linux-64bit" -o tile_linux-64bit
    chmod +x tile_linux-64bit
    mv tile_linux-64bit /usr/local/bin/tile
fi
