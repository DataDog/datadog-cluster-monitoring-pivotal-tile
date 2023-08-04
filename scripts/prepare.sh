#!/usr/bin/env bash

set -e

RESOURCES_DIR="tile/resources"

AGENT_VERSION=4.14.0
CLUSTER_AGENT_VERSION=2.6.0
NOZZLE_RELEASE_VERSION=86

# download agent bosh release tarball
curl -L "https://cloudfoundry.datadoghq.com/datadog-agent/datadog-agent-boshrelease-$AGENT_VERSION.tgz" -o $RESOURCES_DIR/datadog-agent-boshrelease.tgz

# download cluster agent bosh release tarball
curl -L "https://cloudfoundry.datadoghq.com/datadog-cluster-agent/datadog-cluster-agent-boshrelease-$CLUSTER_AGENT_VERSION.tgz" -o $RESOURCES_DIR/datadog-cluster-agent-boshrelease.tgz

# download nozzle bosh release tarball
curl -L "https://cloudfoundry.datadoghq.com/datadog-firehose-nozzle/datadog-firehose-nozzle-release-$NOZZLE_RELEASE_VERSION.tgz" -o $RESOURCES_DIR/datadog-firehose-nozzle-release.tgz
