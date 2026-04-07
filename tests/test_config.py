"""Tests for config module."""

from pathlib import Path

import yaml

from src.config import Channel, Config, load_config, save_config


def test_load_config_defaults(tmp_path: Path) -> None:
    """Load config with minimal values uses defaults."""
    config_file = tmp_path / "config.yaml"
    config_file.write_text("vault_path: ./vault\nchannels: []\n")

    config = load_config(config_file)

    assert config.vault_path == Path("./vault")
    assert config.summary_length == 300
    assert config.last_feed_check is None
    assert config.channels == []


def test_load_config_with_channels(tmp_path: Path) -> None:
    """Load config with channel entries."""
    data = {
        "vault_path": "./my-vault",
        "summary_length": 500,
        "last_feed_check": None,
        "channels": [
            {
                "name": "Test Channel",
                "channel_id": "UC123",
                "rss_url": "https://www.youtube.com/feeds/videos.xml?channel_id=UC123",
                "added_date": "2026-04-07",
            }
        ],
    }
    config_file = tmp_path / "config.yaml"
    config_file.write_text(yaml.dump(data))

    config = load_config(config_file)

    assert len(config.channels) == 1
    assert config.channels[0].name == "Test Channel"
    assert config.channels[0].channel_id == "UC123"
    assert config.summary_length == 500


def test_save_and_reload(tmp_path: Path) -> None:
    """Save config and reload produces same values."""
    config = Config(
        vault_path=Path("./test-vault"),
        summary_length=200,
        last_feed_check=None,
        channels=[
            Channel(name="Ch1", channel_id="UC1", rss_url="http://rss", added_date="2026-04-07")
        ],
    )

    config_file = tmp_path / "config.yaml"
    save_config(config, config_file)
    reloaded = load_config(config_file)

    assert reloaded.vault_path == Path("./test-vault")
    assert reloaded.summary_length == 200
    assert len(reloaded.channels) == 1
    assert reloaded.channels[0].name == "Ch1"
