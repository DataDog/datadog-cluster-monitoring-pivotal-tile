# Changelog

## 6.4.0 / 2025-11-19

* [Changed] Add option for `logs_expected_tags_duration` agent property. See [#125](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/125).
* [Changed] Add option to enable the traceroute system probe submodule. See [#123](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/123).

## 6.3.0 / 2025-04-30

* [Added] Bump Datadog Agent Bosh Release to version 4.21.0. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.21.0) for details.
* [Added] Bump Datadog Cluster Agent Bosh Release to version 2.12.0. See [here](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/2.12.0) for details.

## 6.2.0 / 2024-12-11

* [Added] Bump Datadog Agent Bosh Release to version 4.20.0. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.20.0) for details.
* [Added] Bump Datadog Cluster Agent Bosh Release to version 2.11.0. See [here](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/2.11.0) for details.

## 6.1.1 / 2024-11-21

* [Added] Bump Datadog Agent Bosh Release to version 4.19.0. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.19.0) for details.
* [Added] Bump Datadog Cluster Agent Bosh Release to version 2.10.0. See [here](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/2.10.0) for details.

## 6.0.0 / 2024-01-30

* [Fixed] Fix monit / BPM selector always enabling BPM. See [#116](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/116).
* [Fixed] Fix optional and default value error message. See [#114](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/114).
* [Changed] Remove `datadog-bpm` job and `bpm` release. See [#117](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/117).

#### Breaking Changes:

BPM will not be included with the tile moving forward. To handle agent processes, a separate BPM installation is required.

## 5.9.1 / 2023-12-06

* [Fixed] Fix BPM memory optional values with default error. See [#113](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/113).
* [Fixed] Fix missing `datadog-application-monitoring` product in the runtime_config. See [#110](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/110).

## 5.9.0 / 2023-11-16

* [Added] Bump Datadog Agent Bosh Release to version 4.16.0. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.16.0) for details.
* [Added] Bump Datadog Cluster Agent Bosh Release to version 2.7.1. See [here](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/2.7.1) for details.
* [Added] Bump Datadog Firehose Nozzle Release to version 87. See [here](https://github.com/DataDog/datadog-firehose-nozzle-release/releases/tag/87) for details.
* [Added] Add options for Nozzle logs collection. See [#107](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/107).
* [Added] Add support for BPM. See [#106](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/106).

## 5.8.0 / 2023-09-21

* [Added] Bump Datadog Agent Bosh Release to version 4.15.1. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.15.1) for details.
* [Added] Add `enable_remote_configuration` and `enable_inventories_configuration` properties. See [#103](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/103).

## 5.7.0 / 2023-08-08

* [Added] Bump Datadog Agent Bosh Release to version 4.14.1. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.14.1) for details.
* [Added] Upgrade tile to `ubuntu-jammy` stemcells. See [#101](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/101).

## 5.6.0 / 2023-07-13

* [Added] Bump Datadog Agent Bosh Release to version 4.14.0. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.14.0) for details.
* [Added] Bump Datadog Cluster Agent Bosh Release to version 2.6.0. See [here](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/2.6.0) for details.

## 5.5.1 / 2023-02-07

* [Added] Bump Datadog Agent Bosh Release to version 4.13.1. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.13.1) for details.

## 5.5.0 / 2023-01-26

* [Added] Bump Datadog Agent Bosh Release to version 4.13.0. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.13.0) for details.
* [Added] Bump Datadog Cluster Agent Bosh Release to version 2.5.1. See [here](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/2.5.1) for details.
* [Added] Add options for the `container_tagger` properties. See [#88](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/88).
* [Changed] Use `ubuntu-xenial` stemcells. See [#89](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/89).

## 5.4.1 / 2022-11-16

*Note: This is a beta release.*
* [Added] Bump Datadog Agent Bosh Release to version 4.12.1. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.12.1) for details.

## 5.4.0 / 2022-11-15

* [Added] Bump Datadog Agent Bosh Release to version 4.12.0. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.12.0) for details.
* [Added] Add nozzle option to enable/disable app metadata prefix in app metrics. See [#84](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/84).
* [Added] Add support for ubuntu-jammy stemcell. See [#82](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/82).
* [Added] Add `refresh_on_cache_miss`, `sidecars_tags`, and `isolation_segments_tags` properties to the cluster agent. See [#79](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/79).
* [Added] Pass `api_key` to the cluster agent to add support for the flare command. See [#80](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/80).

## 5.3.2 / 2022-10-11

* [Added] Bump Datadog Agent Bosh Release to version 4.11.2. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.11.2) for details.

## 5.3.1 / 2022-08-17

* [Added] Bump Datadog Agent Bosh Release to version 4.11.1. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.11.1) for details.

## 5.3.0 / 2022-08-03

* [Added] Bump Datadog Agent Bosh Release to version 4.11.0. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.11.0) for details.
* [Added] Bump Datadog Cluster Agent Bosh Release to version 2.3.0. See [here](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/2.3.0) for details.

## 5.2.1 / 2022-07-11

* [Fixed] Add missing option to enable advanced tagging in the cluster agent. See [#74](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/74).

## 5.2.0 / 2022-06-09

* [Added] Bump Datadog Agent Bosh Release to version 4.10.0. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.10.0) for details.
* [Added] Bump Datadog Cluster Agent Bosh Release to version 2.2.0. See [here](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/2.2.0) for details.

## 5.1.0 / 2022-04-26

* [Added] Bump Datadog Firehose Nozzle Release to version 85. See [here](https://github.com/DataDog/datadog-firehose-nozzle-release/releases/tag/85) for details.
* [Added] Bump Datadog Agent Bosh Release to version 4.9.2. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.9.2) for details.
* [Added] Bump Datadog Cluster Agent Bosh Release to version 2.1.1. See [here](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/2.1.1) for details.
* [Added] Add option to enable advanced tagging in the nozzle. See [#67](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/67).
* [Added] Add options to use the cluster agent API and serve nozzle data. See [#66](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/66).

## 5.0.1 / 2022-02-25

* [Added] Bump Datadog Agent Bosh Release to version 4.9.1. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.9.1) for details.
* [Added] Add option to disable Network Performance Monitoring when enabling system probe. See [#64](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/64).

## 5.0.0 / 2022-02-07

* [Added] Bump Datadog Agent Bosh Release to version 4.9.0. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.9.0) for details.
* [Added] Bump Datadog Cluster Agent Bosh Release to version 2.0.0. See [here](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/2.0.0) for details.

This tile includes the following packages:
  * [Firehose Nozzle 83](https://github.com/DataDog/datadog-firehose-nozzle-release/releases/tag/83)
  * [Datadog Agent Bosh Release 4.9.0](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.9.0)
  * [Datadog Cluster Agent Bosh Release 2.0.0](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/2.0.0)

## 4.9.4 / 2021-12-23

* [Added] Bump Datadog Agent Bosh Release to version 4.8.3. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.8.3) for details.
* [Added] Bump Datadog Cluster Agent Bosh Release to version 1.9.3. See [here](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.9.3) for details.

This tile includes the following packages:
  * [Firehose Nozzle 83](https://github.com/DataDog/datadog-firehose-nozzle-release/releases/tag/83)
  * [Datadog Agent Bosh Release 4.8.3](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.8.3)
  * [Datadog Cluster Agent Bosh Release 1.9.3](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.9.3)

## 4.9.3 / 2021-12-21

* [Added] Bump Datadog Agent Bosh Release to version 4.8.2. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.8.2) for details.
* [Added] Bump Datadog Cluster Agent Bosh Release to version 1.9.2. See [here](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.9.2) for details.

This tile includes the following packages:
  * [Firehose Nozzle 83](https://github.com/DataDog/datadog-firehose-nozzle-release/releases/tag/83)
  * [Datadog Agent Bosh Release 4.8.2](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.8.2)
  * [Datadog Cluster Agent Bosh Release 1.9.2](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.9.2)

## 4.9.2 / 2021-12-14

* [Added] Bump Datadog Agent Bosh Release to version 4.8.1. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.8.1) for details.
* [Added] Bump Datadog Cluster Agent Bosh Release to version 1.9.1. See [here](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.9.1) for details.

This tile includes the following packages:
  * [Firehose Nozzle 83](https://github.com/DataDog/datadog-firehose-nozzle-release/releases/tag/83)
  * [Datadog Agent Bosh Release 4.8.1](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.8.1)
  * [Datadog Cluster Agent Bosh Release 1.9.1](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.9.1)

## 4.9.1 / 2021-12-03

* [Added] Bump Datadog Cluster Agent Bosh Release to version 1.9.0. See [here](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.9.0) for details.

This tile includes the following packages:
  * [Firehose Nozzle 83](https://github.com/DataDog/datadog-firehose-nozzle-release/releases/tag/83)
  * [Datadog Agent Bosh Release 4.8.0](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.8.0)
  * [Datadog Cluster Agent Bosh Release 1.9.0](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.9.0)

## 4.9.0 / 2021-11-29

* [Added] Bump Datadog Agent Bosh Release to version 4.8.0. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.8.0) for details.

This tile includes the following packages:
  * [Firehose Nozzle 83](https://github.com/DataDog/datadog-firehose-nozzle-release/releases/tag/83)
  * [Datadog Agent Bosh Release 4.8.0](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.8.0)
  * [Datadog Cluster Agent Bosh Release 1.9.0](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.9.0)

## 4.8.1 / 2021-09-21

* [Added] Bump Datadog Agent Bosh Release to version 4.7.1. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.7.1) for details.

This tile includes the following packages:
  * [Firehose Nozzle 83](https://github.com/DataDog/datadog-firehose-nozzle-release/releases/tag/83)
  * [Datadog Agent Bosh Release 4.7.1](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.7.1)
  * [Datadog Cluster Agent Bosh Release 1.8.0](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.8.0)

## 4.8.0 / 2021-09-20

* [Added] Bump Datadog Agent Bosh Release to version 4.7.0. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.7.0) for details.
* [Added] Bump Datadog Cluster Agent Bosh Release to version 1.8.0. See [here](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.8.0) for details.

This tile includes the following packages:
  * [Firehose Nozzle 83](https://github.com/DataDog/datadog-firehose-nozzle-release/releases/tag/83)
  * [Datadog Agent Bosh Release 4.7.0](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.7.0)
  * [Datadog Cluster Agent Bosh Release 1.8.0](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.8.0)

## 4.7.0 / 2021-08-18

* [Added] Add option to collect monit children processes. See [#53](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/53).
* [Added] Add option to force use of TLS 1.2. See [#52](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/52).
* [Added] Add configuration option for CC API list app endpoint batch size. See [#51](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/51).
* [Added] Add property to specify ulimit for number of open file descriptors. See [#50](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/50).
* [Added] Add configuration forms for Datadog Agent Bosh addon placement rules. See [#49](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/49).
* [Added] Bump Datadog Agent Bosh Release to version 4.6.0. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.6.0) for details.
* [Added] Bump Datadog Cluster Agent Bosh Release to version 1.7.0. See [here](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.7.0) for details.
* [Added] Bump Datadog Firehose Nozzle Release to version 83. See [here](https://github.com/DataDog/datadog-firehose-nozzle-release/releases/tag/83) for details.

This tile includes the following packages:
  * [Firehose Nozzle 83](https://github.com/DataDog/datadog-firehose-nozzle-release/releases/tag/83)
  * [Datadog Agent Bosh Release 4.6.0](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.6.0)
  * [Datadog Cluster Agent Bosh Release 1.7.0](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.7.0)

## 4.6.0 / 2021-04-20

* [Added] Add `no_proxy_nonexact_match` configuration option. See [#47](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/47).
* [Added] Add inputs to configure custom URLs for process, APM and logs. See [#46](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/46).
* [Added] Add option to send application environment variables as custom container tags. See [#45](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/45).
* [Added] Add option to poll Cloud Foundry API for more advanced container tagging. See [#42](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/42).
* [Added] Add option to collect containers only with the Process Agent. See [#41](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/41).
* [Added] Bump Datadog Agent Bosh Release to version 4.5.0. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.5.0) for details.
* [Added] Bump Datadog Cluster Agent Bosh Release to version 1.6.0. See [here](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.6.0) for details.

This tile includes the following packages:
  * [Firehose Nozzle 80](https://github.com/DataDog/datadog-firehose-nozzle-release/releases/tag/80)
  * [Datadog Agent Bosh Release 4.5.0](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.5.0)
  * [Datadog Cluster Agent Bosh Release 1.6.0](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.6.0)

## 4.5.0 / 2021-03-25

* [Added] Add option to append VM UUID to generated friendly hostnames. See [#39](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/39).
* [Added] Add TKGI kubernetes control plane monitoring. See [#38](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/38).
* [Fixed] Properly exclude kubernetes service instances in the placement rules. See [#37](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/37).
* [Added] Bump Datadog Agent Bosh Release to version 4.4.1. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.4.1) for details.

This tile includes the following packages:
  * [Firehose Nozzle 80](https://github.com/DataDog/datadog-firehose-nozzle-release/releases/tag/80)
  * [Datadog Agent Bosh Release 4.4.1](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.4.1)
  * [Datadog Cluster Agent Bosh Release 1.5.0](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.5.0)

## 4.4.0 / 2021-01-21

* [Fixed] Add field for customizing API site and properly sending data to other Datadog regions. See [#35](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/35).
* [Added] Bump Datadog Agent Bosh Release to version 4.3.0. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.3.0) for details.
* [Added] Bump Datadog Cluster Agent Bosh Release to version 1.5.0. See [here](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.5.0) for details.

This tile includes the following packages:
  * [Firehose Nozzle 80](https://github.com/DataDog/datadog-firehose-nozzle-release/releases/tag/80)
  * [Datadog Agent Bosh Release 4.3.0](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.3.0)
  * [Datadog Cluster Agent Bosh Release 1.5.0](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.5.0)

## 4.3.0 / 2020-12-14

* [Added] Bump Datadog Agent Bosh Release to version 4.2.0. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.2.0) for details.
* [Added] Bump Datadog Cluster Agent Bosh Release to version 1.4.0. See [here](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.4.0) for details.

This tile includes the following packages:
  * [Firehose Nozzle 80](https://github.com/DataDog/datadog-firehose-nozzle-release/releases/tag/80)
  * [Datadog Agent Bosh Release 4.2.0](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.2.0)
  * [Datadog Cluster Agent Bosh Release 1.4.0](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.4.0)

## 4.2.0 / 2020-10-13

* [Added] Bump Datadog Agent Bosh Release to version 4.1.0. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.1.0) for details.
* [Added] Bump Datadog Cluster Agent Bosh Release to version 1.3.0. See [here](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.3.0) for details.

This tile includes the following packages:
  * [Firehose Nozzle 80](https://github.com/DataDog/datadog-firehose-nozzle-release/releases/tag/80)
  * [Datadog Agent Bosh Release 4.1.0](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.1.0)
  * [Datadog Cluster Agent Bosh Release 1.3.0](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.3.0)

## 4.1.1 / 2020-09-21

* [Fixed] Bump Datadog Agent Bosh Release to version 4.0.1. See [here](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.0.1) for details.

This tile includes the following packages:
  * [Firehose Nozzle 80](https://github.com/DataDog/datadog-firehose-nozzle-release/releases/tag/80)
  * [Datadog Agent Bosh Release 4.0.1](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.0.1)
  * [Datadog Cluster Agent Bosh Release 1.2.0](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.2.0)

## 4.1.0 / 2020-09-04

* [Added] Enable usage of autogenerated BBS certificates. See [#29](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/29).
* [Added] Add ability to configure the Cloud Foundry API integration as a cluster check. See [#24](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/24).
* [Added] Add nozzle configuration options for metadata collection. See [#23](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/23).
* [Fixed] Use DNS alias instead of consuming cluster agent bosh link in Datadog Agent Bosh addon. See [#31](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/31).
  **Note**: This effectively fixes issues related to tile deployment order, and removes the need to perform deployments in two steps when enabling the Datadog Cluster Agent feature.

This tile includes the following packages:
  * [Firehose Nozzle 80](https://github.com/DataDog/datadog-firehose-nozzle-release/releases/tag/80)
  * [Datadog Agent Bosh Release 4.0.0](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/4.0.0)
  * [Datadog Cluster Agent Bosh Release 1.2.0](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.2.0)

## 4.0.0 / 2020-06-18

* [Added] Add Datadog Cluster Agent Bosh release to the tile. See [#19](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/19).
  **Note:** When enabled, the Datadog Cluster Agent is deployed on an additional VM created during the tile deployment and may impact the billing from the cloud provider running your VMware Tanzu infrastructure. This additional VM can be configured in the `Resource Config` tab of the tile.
* [Changed] Disable NPM with system probe by default. See [#20](https://github.com/DataDog/datadog-cluster-monitoring-pivotal-tile/pull/20).

This tile includes the following packages:
  * [Firehose Nozzle 79](https://github.com/DataDog/datadog-firehose-nozzle-release/releases/tag/79)
  * [Datadog Agent Bosh Release 3.0.0](https://github.com/DataDog/datadog-agent-boshrelease/releases/tag/3.0.0)
  * [Datadog Cluster Agent Bosh Release 1.0.0](https://github.com/DataDog/datadog-cluster-agent-boshrelease/releases/tag/1.0.0)
