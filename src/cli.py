"""CLI entry point for the AI Information Gathering tool."""

from datetime import datetime

import click

from src.config import Channel, load_config, save_config
from src.feed import build_rss_url, get_new_videos
from src.metadata import Err as MetaErr
from src.metadata import resolve_channel_id
from src.process import process_inbox
from src.vault import ensure_vault_structure


@click.group()
def main() -> None:
    """AI Information Gathering — personal knowledge management tool."""


@main.command()
def init() -> None:
    """Initialize the vault directory structure."""
    config = load_config()
    ensure_vault_structure(config.vault_path)
    click.echo(f"Vault initialized at {config.vault_path.resolve()}")


@main.command()
def process() -> None:
    """Process all unprocessed files in the vault inbox."""
    config = load_config()
    process_inbox(config)


@main.group()
def channel() -> None:
    """Manage tracked YouTube channels."""


@channel.command("add")
@click.argument("channel_url")
def channel_add(channel_url: str) -> None:
    """Add a YouTube channel to track.

    Args:
        channel_url: YouTube channel URL (@handle, /channel/ID, /c/name).
    """
    config = load_config()

    click.echo(f"Resolving channel: {channel_url}")
    result = resolve_channel_id(channel_url)

    if isinstance(result, MetaErr):
        click.echo(f"Error: {result.message}")
        return

    meta = result.value
    existing_ids = {ch.channel_id for ch in config.channels}

    if meta.channel_id in existing_ids:
        click.echo(f"Channel already tracked: {meta.channel_name}")
        return

    rss_url = build_rss_url(meta.channel_id)
    new_channel = Channel(
        name=meta.channel_name,
        channel_id=meta.channel_id,
        rss_url=rss_url,
        added_date=datetime.now().strftime("%Y-%m-%d"),
    )

    config.channels.append(new_channel)
    save_config(config)
    click.echo(f"Added channel: {meta.channel_name} ({meta.channel_id})")


@channel.command("list")
def channel_list() -> None:
    """List all tracked YouTube channels."""
    config = load_config()

    if not config.channels:
        click.echo("No channels tracked. Use 'aig channel add <url>' to add one.")
        return

    for ch in config.channels:
        click.echo(f"  {ch.name} ({ch.channel_id}) — added {ch.added_date}")


@channel.command("remove")
@click.argument("channel_name")
def channel_remove(channel_name: str) -> None:
    """Remove a tracked YouTube channel by name.

    Args:
        channel_name: Name of the channel to remove.
    """
    config = load_config()
    original_count = len(config.channels)
    config.channels = [ch for ch in config.channels if ch.name.lower() != channel_name.lower()]

    if len(config.channels) == original_count:
        click.echo(f"Channel not found: {channel_name}")
        return

    save_config(config)
    click.echo(f"Removed channel: {channel_name}")


@main.command("feed")
def feed_check() -> None:
    """Check RSS feeds for new videos on tracked channels."""
    config = load_config()

    if not config.channels:
        click.echo("No channels tracked. Use 'aig channel add <url>' to add one.")
        return

    total_new = 0
    for ch in config.channels:
        entries = get_new_videos(ch.rss_url, config.last_feed_check)
        if entries:
            click.echo(f"\n{ch.name} ({len(entries)} new):")
            for entry in entries:
                pub_str = entry.published.strftime("%Y-%m-%d") if entry.published else "unknown"
                click.echo(f"  [{pub_str}] {entry.title}")
                click.echo(f"    {entry.url}")
            total_new += len(entries)

    if total_new == 0:
        click.echo("No new videos since last check.")

    config.last_feed_check = datetime.now()
    save_config(config)
    click.echo(f"\nTotal: {total_new} new video(s). Last check updated.")


if __name__ == "__main__":
    main()
