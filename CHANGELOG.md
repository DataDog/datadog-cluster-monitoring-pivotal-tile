# Changelog

## 4.1.0 / 2020-07-24

* [Added] Add ability to configure the Cloud Foundry API integration as a cluster check. See [#24](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/24).
* [Added] Add nozzle configuration options for metadata collection. See [#23](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/23).
* [Changed] Simplify configuration of Cluster Agent by generating certificate and private key automatically. See [#25](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/25).
    * Users that configured the Cluster Agent with custom CA certificate and generated client certificate and private key will need to configure it in the `Datadog Cluster Agent Settings` tab again.
    * Users that specified the OpsMan root CA don't need to do anything.

This tile includes the following packages:
  * [Firehose Nozzle 80](https://github.com/DataDog/datadog-firehose-nozzle-release/releases/tag/80)
  * [Datadog Agent Bosh Release 3.1.0](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/3.1.0)
  * [Datadog Cluster Agent Bosh Release 1.1.0](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.1.0)

## 4.0.0 / 2020-06-18

* [Added] Add Datadog Cluster Agent Bosh release to the tile. See [#19](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/19).  
  **Note:** When enabled, the Datadog Cluster Agent is deployed on an additional VM created during the tile deployment and may impact the billing from the cloud provider running your VMware Tanzu infrastructure. This additional VM can be configured in the `Resource Config` tab of the tile.
* [Changed] Disable NPM with system probe by default. See [#20](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/20).

This tile includes the following packages:
  * [Firehose Nozzle 79](https://github.com/DataDog/datadog-firehose-nozzle-release/releases/tag/79)
  * [Datadog Agent Bosh Release 3.0.0](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/3.0.0)
  * [Datadog Cluster Agent Bosh Release 1.0.0](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.0.0)
