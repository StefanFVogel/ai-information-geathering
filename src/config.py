"""Load and manage application configuration from config.yaml."""

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import yaml


@dataclass
class Channel:
    """A tracked YouTube channel."""

    name: str
    channel_id: str
    rss_url: str
    added_date: str


@dataclass
class Config:
    """Application configuration."""

    vault_path: Path
    summary_length: int
    last_feed_check: datetime | None
    channels: list[Channel]


def _parse_channel(data: dict[str, str]) -> Channel:
    """Parse a channel entry from config data."""
    return Channel(
        name=data["name"],
        channel_id=data["channel_id"],
        rss_url=data["rss_url"],
        added_date=data.get("added_date", ""),
    )


def load_config(config_path: Path = Path("config.yaml")) -> Config:
    """Load configuration from a YAML file.

    Args:
        config_path: Path to the config.yaml file.

    Returns:
        Parsed Config object.

    Raises:
        FileNotFoundError: If the config file does not exist.
    """
    with config_path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    channels = [_parse_channel(ch) for ch in (data.get("channels") or [])]
    last_check_raw = data.get("last_feed_check")
    last_feed_check = datetime.fromisoformat(last_check_raw) if last_check_raw else None

    return Config(
        vault_path=Path(data.get("vault_path", "./vault")),
        summary_length=data.get("summary_length", 300),
        last_feed_check=last_feed_check,
        channels=channels,
    )


def save_config(config: Config, config_path: Path = Path("config.yaml")) -> None:
    """Save configuration back to a YAML file.

    Args:
        config: The Config object to save.
        config_path: Path to the config.yaml file.
    """
    channels_data = [
        {
            "name": ch.name,
            "channel_id": ch.channel_id,
            "rss_url": ch.rss_url,
            "added_date": ch.added_date,
        }
        for ch in config.channels
    ]

    data = {
        "vault_path": str(config.vault_path),
        "summary_length": config.summary_length,
        "last_feed_check": config.last_feed_check.isoformat() if config.last_feed_check else None,
        "channels": channels_data,
    }

    with config_path.open("w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
