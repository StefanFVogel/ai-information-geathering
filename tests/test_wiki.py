"""Tests for wiki module."""

from pathlib import Path

import frontmatter  # type: ignore[import-untyped]

from src.vault import ensure_vault_structure
from src.wiki import _slugify, lint_wiki, update_index, update_wiki_from_summary


def test_slugify() -> None:
    """Convert names to kebab-case slugs."""
    assert _slugify("Andrej Karpathy") == "andrej-karpathy"
    assert _slugify("RAG") == "rag"
    assert _slugify("Fine-Tuning") == "fine-tuning"


def test_update_wiki_creates_people_page(tmp_path: Path) -> None:
    """Create a new person wiki page."""
    ensure_vault_structure(tmp_path)

    updated = update_wiki_from_summary(
        tmp_path, "2026-04-07-test-video.md", ["Andrej Karpathy"], [], []
    )

    assert len(updated) == 1
    page_path = tmp_path / "wiki" / "people" / "andrej-karpathy.md"
    assert page_path.exists()

    post = frontmatter.load(str(page_path))
    assert post["title"] == "Andrej Karpathy"
    assert post["type"] == "wiki"
    assert "2026-04-07-test-video.md" in post["related_sources"]


def test_update_wiki_creates_concept_page(tmp_path: Path) -> None:
    """Create a new concept wiki page."""
    ensure_vault_structure(tmp_path)

    update_wiki_from_summary(tmp_path, "source.md", [], ["RAG"], [])

    page_path = tmp_path / "wiki" / "concepts" / "rag.md"
    assert page_path.exists()


def test_update_wiki_adds_source_to_existing(tmp_path: Path) -> None:
    """Add source reference to existing wiki page."""
    ensure_vault_structure(tmp_path)

    update_wiki_from_summary(tmp_path, "video1.md", ["Andrej Karpathy"], [], [])
    update_wiki_from_summary(tmp_path, "video2.md", ["Andrej Karpathy"], [], [])

    page_path = tmp_path / "wiki" / "people" / "andrej-karpathy.md"
    post = frontmatter.load(str(page_path))

    assert "video1.md" in post["related_sources"]
    assert "video2.md" in post["related_sources"]


def test_update_wiki_no_duplicate_source(tmp_path: Path) -> None:
    """Do not add the same source twice."""
    ensure_vault_structure(tmp_path)

    update_wiki_from_summary(tmp_path, "video1.md", ["Andrej Karpathy"], [], [])
    update_wiki_from_summary(tmp_path, "video1.md", ["Andrej Karpathy"], [], [])

    page_path = tmp_path / "wiki" / "people" / "andrej-karpathy.md"
    post = frontmatter.load(str(page_path))

    assert post["related_sources"].count("video1.md") == 1


def test_update_index(tmp_path: Path) -> None:
    """Rebuild wiki index includes all pages."""
    ensure_vault_structure(tmp_path)
    update_wiki_from_summary(tmp_path, "s.md", ["Andrej Karpathy"], ["RAG"], [])

    update_index(tmp_path)

    index_path = tmp_path / "index.md"
    content = index_path.read_text(encoding="utf-8")

    assert "[[Andrej Karpathy]]" in content
    assert "[[RAG]]" in content


def test_update_index_empty_wiki(tmp_path: Path) -> None:
    """Rebuild index with no wiki pages shows empty sections."""
    ensure_vault_structure(tmp_path)
    update_index(tmp_path)

    index_path = tmp_path / "index.md"
    content = index_path.read_text(encoding="utf-8")

    assert "## People" in content
    assert "*No entries yet.*" in content


def test_lint_wiki_finds_orphans(tmp_path: Path) -> None:
    """Lint detects wiki pages with no source references."""
    ensure_vault_structure(tmp_path)

    # Create a page without sources
    page_path = tmp_path / "wiki" / "people" / "nobody.md"
    post = frontmatter.Post("# Nobody\n", type="wiki", title="Nobody", related_sources=[])
    page_path.parent.mkdir(parents=True, exist_ok=True)
    with page_path.open("w", encoding="utf-8") as f:
        f.write(frontmatter.dumps(post))

    findings = lint_wiki(tmp_path)
    assert "Nobody" in findings["orphaned_pages"]


def test_lint_wiki_healthy(tmp_path: Path) -> None:
    """Lint on healthy wiki returns no findings."""
    ensure_vault_structure(tmp_path)
    update_wiki_from_summary(tmp_path, "s.md", ["Test Person"], [], [])

    findings = lint_wiki(tmp_path)
    assert findings["orphaned_pages"] == []
