# Changelog
## 4.0.0 / 2020-06-18

* [Added] Add Datadog Cluster Agent Bosh release to the tile. See [#19](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/19).  
  **Note:** When enabled, the Datadog Cluster Agent is deployed on an additional VM created during the tile deployment and may impact the billing from the cloud provider running your VMware Tanzu infrastructure. This additional VM can be configured in the `Resource Config` tab of the tile.
* [Changed] Disable NPM with system probe by default. See [#20](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/20).

This tile includes the following packages:
  * [Firehose Nozzle 79](https://github.com/DataDog/datadog-firehose-nozzle-release/releases/tag/79)
  * [Datadog Agent Bosh Release 3.0.0](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/3.0.0)
  * [Datadog Cluster Agent Bosh Release 1.0.0](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.0.0)
