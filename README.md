# Datadog Cluster Monitoring for Pivotal Platform

Configuration file for the Datadog Cluster Monitoring tile for Pivotal Platform.

# Build new tile

## Prerequisite

- Create a virtual environment for installing needed python packages
    ```bash
    cd tile
    virtualenv venv
    source venv/bin/activate
    ```

- Install the [Tile Generator](https://docs.pivotal.io/tiledev/2-5/tile-generator.html) utility on your machine
    ```bash
    pip install tile-generator
    ```
    - If it is already installed, update it with
      ```bash
      pip install --upgrade tile-generator
      ```

- Download the [Datadog Firehose Nozzle release](https://github.com/DataDog/datadog-firehose-nozzle-release/releases) and [Datadog Agent BOSH release](https://github.com/DataDog/datadog-agent-boshrelease/releases) from GitHub.

## Build

- Place the `datadog-firehose-nozzle-release.tgz` and the `datadog-agent-boshrelease.tgz` files into the `tile/resources` folder.

- Update the `tile.yml` file to bump to the version of the agent boshrelease that you put in the resources folder.

- Create the tile by specifying the version. Look at the [tile-history.yml](tile/tile-history.yml) for the latest version that was built.
    ```bash
    tile build <TILE_VERSION>
    ```

The tile (`datadog-*.*.*.pivotal` file) is available in the `tile/product` folder, and `tile/tile-history.yml` has been automatically updated.
