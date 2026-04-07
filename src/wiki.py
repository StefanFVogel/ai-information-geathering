"""Wiki maintenance: create and update entity pages from processed sources."""

import re
from datetime import date
from pathlib import Path

import frontmatter  # type: ignore[import-untyped]

from src.vault import write_note


def update_wiki_from_summary(
    vault_path: Path,
    source_filename: str,
    people: list[str],
    concepts: list[str],
    tools: list[str],
) -> list[str]:
    """Create or update wiki pages for entities mentioned in a source.

    Args:
        vault_path: Root path of the Obsidian vault.
        source_filename: Name of the source file that mentions these entities.
        people: List of people names extracted from summary.
        concepts: List of concept names extracted from summary.
        tools: List of tool names extracted from summary.

    Returns:
        List of wiki pages that were created or updated.
    """
    updated_pages: list[str] = []

    for name in people:
        path = _ensure_entity_page(vault_path, "people", name, source_filename)
        updated_pages.append(str(path.relative_to(vault_path)))

    for name in concepts:
        path = _ensure_entity_page(vault_path, "concepts", name, source_filename)
        updated_pages.append(str(path.relative_to(vault_path)))

    for name in tools:
        path = _ensure_entity_page(vault_path, "tools", name, source_filename)
        updated_pages.append(str(path.relative_to(vault_path)))

    return updated_pages


def _ensure_entity_page(vault_path: Path, category: str, name: str, source_filename: str) -> Path:
    """Create or update an entity wiki page.

    Args:
        vault_path: Root path of the Obsidian vault.
        category: Entity category (people, concepts, tools).
        name: Entity name.
        source_filename: Source file that mentions this entity.

    Returns:
        Path to the created or updated wiki page.
    """
    slug = _slugify(name)
    file_path = vault_path / "wiki" / category / f"{slug}.md"

    if file_path.exists():
        _add_source_reference(file_path, source_filename)
    else:
        _create_entity_page(file_path, category, name, source_filename)

    return file_path


def _create_entity_page(file_path: Path, category: str, name: str, source_filename: str) -> None:
    """Create a new entity wiki page.

    Args:
        file_path: Path for the new file.
        category: Entity category.
        name: Entity name.
        source_filename: Source file reference.
    """
    post = frontmatter.Post(
        f"# {name}\n\n"
        f"## Sources\n\n"
        f"- [[{source_filename}]]\n",
        type="wiki",
        category=category,
        title=name,
        related_sources=[source_filename],
        last_updated=date.today().isoformat(),
    )
    write_note(file_path, post)


def _add_source_reference(file_path: Path, source_filename: str) -> None:
    """Add a source reference to an existing wiki page.

    Args:
        file_path: Path to the existing wiki page.
        source_filename: Source file to add.
    """
    post = frontmatter.load(str(file_path))
    existing_sources: list[str] = list(post.get("related_sources") or [])

    if source_filename in existing_sources:
        return

    existing_sources.append(source_filename)
    post["related_sources"] = existing_sources
    post["last_updated"] = date.today().isoformat()

    source_link = f"- [[{source_filename}]]\n"
    if source_link not in post.content:
        post.content = post.content.rstrip() + f"\n{source_link}"

    write_note(file_path, post)


def update_index(vault_path: Path) -> None:
    """Rebuild the wiki index from all wiki pages.

    Args:
        vault_path: Root path of the Obsidian vault.
    """
    wiki_path = vault_path / "wiki"
    sections: dict[str, list[str]] = {"people": [], "concepts": [], "tools": [], "syntheses": []}

    for category in sections:
        cat_path = wiki_path / category
        if not cat_path.exists():
            continue
        for md_file in sorted(cat_path.glob("*.md")):
            post = frontmatter.load(str(md_file))
            title = str(post.get("title", md_file.stem))
            sections[category].append(f"- [[{title}]]")

    index_content = _build_index_content(sections)
    index_path = vault_path / "index.md"
    index_post = frontmatter.Post(
        index_content,
        type="index",
        title="Wiki Index",
        last_updated=date.today().isoformat(),
    )
    write_note(index_path, index_post)


def _build_index_content(sections: dict[str, list[str]]) -> str:
    """Build index markdown content from sections.

    Args:
        sections: Dict mapping category names to lists of wikilinks.

    Returns:
        Formatted markdown string.
    """
    lines = ["# Wiki Index\n"]
    display_names = {"people": "People", "concepts": "Concepts", "tools": "Tools", "syntheses": "Syntheses"}

    for category, entries in sections.items():
        lines.append(f"\n## {display_names.get(category, category)}\n")
        if entries:
            lines.extend(entries)
        else:
            lines.append("*No entries yet.*")

    return "\n".join(lines) + "\n"


def lint_wiki(vault_path: Path) -> dict[str, list[str]]:
    """Check wiki health: orphaned pages, missing links.

    Args:
        vault_path: Root path of the Obsidian vault.

    Returns:
        Dict with findings: orphaned_pages, broken_links.
    """
    wiki_path = vault_path / "wiki"
    all_pages: set[str] = set()
    referenced_entities: set[str] = set()
    findings: dict[str, list[str]] = {"orphaned_pages": [], "broken_links": []}

    for md_file in wiki_path.rglob("*.md"):
        post = frontmatter.load(str(md_file))
        title = str(post.get("title", md_file.stem))
        all_pages.add(title)

        sources = post.get("related_sources") or []
        if not sources:
            findings["orphaned_pages"].append(title)

    sources_path = vault_path / "sources"
    if sources_path.exists():
        for md_file in sources_path.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            wikilinks = re.findall(r"\[\[([^\]]+)\]\]", content)
            referenced_entities.update(wikilinks)

    for entity in referenced_entities:
        slug = _slugify(entity)
        found = False
        for category in ["people", "concepts", "tools", "syntheses"]:
            if (wiki_path / category / f"{slug}.md").exists():
                found = True
                break
        if not found:
            findings["broken_links"].append(entity)

    return findings


def _slugify(name: str) -> str:
    """Convert a name to a kebab-case filename slug.

    Args:
        name: The name to slugify.

    Returns:
        Kebab-case slug string.
    """
    slug = name.lower().strip()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"[\s]+", "-", slug)
    return slug
