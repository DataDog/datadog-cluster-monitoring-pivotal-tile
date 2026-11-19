import re
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
TILE = yaml.safe_load((ROOT / "tile/tile.yml").read_text())


def property_value(expression, values):
    match = re.fullmatch(r"\(\( \.properties\.([\w.]+)\.value \)\)", expression)
    if not match:
        raise AssertionError(f"Unexpected property expression: {expression}")

    value = values
    for part in match.group(1).split("."):
        value = value.get(part) if isinstance(value, dict) else None
    return value


class AgentDestinationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.global_properties = next(
            form["properties"]
            for form in TILE["forms"]
            if form["name"] == "datadog-config"
        )
        release = next(
            release
            for release in TILE["packages"]
            if release["name"] == "datadog-cluster-agent-boshrelease"
        )
        cls.cluster_agent = release["jobs"][0]["properties"]["cluster_agent"]
        cls.node_agents = {
            runtime["name"]: addon["properties"]["dd"]
            for runtime in TILE["runtime_configs"]
            for addon in runtime["runtime_config"]["addons"]
            if any(job["name"] == "dd-agent" for job in addon["jobs"])
        }

    def test_site_reaches_all_agents(self):
        agents = {"cluster-agent": self.cluster_agent, **self.node_agents}
        for values, expected in (
            ({}, None),
            ({"site": ""}, ""),
            ({"site": "datadoghq.eu"}, "datadoghq.eu"),
        ):
            for name, agent in agents.items():
                with self.subTest(agent=name, properties=values):
                    self.assertEqual(property_value(agent["site"], values), expected)

    def test_shared_fqdn_conversion_reaches_all_agents(self):
        setting = next(
            prop
            for prop in self.global_properties
            if prop["name"] == "convert_dd_site_fqdn_enabled"
        )
        self.assertEqual(setting["type"], "boolean")
        self.assertTrue(setting["configurable"])
        self.assertIs(setting["default"], True)
        conversions = {
            "cluster-agent": self.cluster_agent["convert_dd_site_fqdn"],
            **{
                name: agent["agent_config"]["convert_dd_site_fqdn"]
                for name, agent in self.node_agents.items()
            },
        }
        for enabled in (setting["default"], False):
            values = {setting["name"]: enabled}
            for name, conversion in conversions.items():
                with self.subTest(agent=name, enabled=enabled):
                    self.assertIs(
                        property_value(conversion["enabled"], values), enabled
                    )

    def test_downloaded_node_release_matches_runtime_configs(self):
        prepare = (ROOT / "scripts/prepare.sh").read_text()
        downloaded_version = re.search(
            r"^AGENT_VERSION=(\S+)$", prepare, re.MULTILINE
        ).group(1)
        for runtime in TILE["runtime_configs"]:
            release = next(
                release
                for release in runtime["runtime_config"]["releases"]
                if release["name"] == "datadog-agent"
            )
            with self.subTest(runtime=runtime["name"]):
                self.assertEqual(downloaded_version, release["version"])


if __name__ == "__main__":
    unittest.main()
