#!/usr/bin/env python3
"""
Shared knowledge of the archive's layout. Imported by every other script.

This file exists to hold one thing: what differs between a podcast and an
essay collection. Before it, five scripts each hard-coded "episodes" and
"transcript.md", which meant a second content type could not be added without
editing all five and getting all five right.

A *source* is a publication: a podcast, or a newsletter. Each one is a
directory under `sources/` with a `source.json` describing where its items are
published and how to read them. An *item* is one episode or one post.

The two content types differ in a handful of ways and no others:

    content_type   items live in   the source doc is   note points at it with
    ------------   -------------   -----------------   ----------------------
    podcast        episodes/       transcript.md       source_transcript
    essay          posts/          essay.md            source_document

and in two note frontmatter fields: a podcast note names the `episode` and its
`guest`, an essay note names the `post` and its `author`.

Everything else -- discovery, fetching, the manifest, the note sections, the
validator, dedupe -- is shared. If you find yourself adding a third branch on
content type somewhere else, that is a sign the difference belongs here
instead.
"""

import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCES = os.path.join(ROOT, "sources")

# The only per-content-type facts in the repository.
CONTENT_TYPES = {
    "podcast": {
        "items_dir": "episodes",
        "source_file": "transcript.md",
        "note_source_field": "source_transcript",
        "note_title_field": "episode",
        "note_author_field": "guest",
        # The half of docs/NOTE-SPEC.md that applies to this content type.
        "spec_section": "Notes on a podcast episode",
        # Used in the wording of reports and briefs, so a run against a
        # newsletter does not talk about episodes and transcripts.
        "item": "episode",
        "items": "episodes",
        "document": "transcript",
        "documents": "transcripts",
    },
    "essay": {
        "items_dir": "posts",
        "source_file": "essay.md",
        "note_source_field": "source_document",
        "note_title_field": "post",
        "note_author_field": "author",
        "spec_section": "Notes on an essay",
        "item": "post",
        "items": "posts",
        "document": "essay",
        "documents": "essays",
    },
}

DEFAULT_TYPE = "podcast"

# Configs were called podcast.json before essays existed. A checkout that
# predates the rename still works; nothing has to be migrated in a hurry.
CONFIG_NAMES = ("source.json", "podcast.json")


def config_path(name):
    """Path to a source's config, or None if it has none."""
    for filename in CONFIG_NAMES:
        path = os.path.join(SOURCES, name, filename)
        if os.path.isfile(path):
            return path
    return None


def source_names():
    """Every configured source, alphabetically."""
    if not os.path.isdir(SOURCES):
        return []
    return sorted(d for d in os.listdir(SOURCES) if config_path(d))


def load(name):
    """Read and return a source's config."""
    path = config_path(name)
    if not path:
        raise SystemExit(
            "no config at %s (see docs/ADDING-A-SOURCE.md)"
            % os.path.join(SOURCES, name, "source.json"))
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def kind(cfg):
    """The content type of a config, validated.

    An unknown value is fatal rather than silently treated as a podcast: it
    would otherwise look for episodes/ in a newsletter, find nothing, and
    report an empty archive as though that were the truth.
    """
    value = cfg.get("content_type", DEFAULT_TYPE)
    if value not in CONTENT_TYPES:
        raise SystemExit(
            "unknown content_type %r in %s; known: %s"
            % (value, cfg.get("name", "?"), ", ".join(sorted(CONTENT_TYPES))))
    return CONTENT_TYPES[value]


def words(name):
    """The vocabulary for one source, by name."""
    return kind(load(name))


def items_dir(name, cfg=None):
    """Directory holding this source's items."""
    cfg = cfg if cfg is not None else load(name)
    return os.path.join(SOURCES, name, kind(cfg)["items_dir"])


def item_folders(name, cfg=None):
    """Every item folder for a source, alphabetically."""
    base = items_dir(name, cfg)
    if not os.path.isdir(base):
        return []
    return sorted(d for d in os.listdir(base)
                  if os.path.isdir(os.path.join(base, d)))


def source_doc(name, folder, cfg=None):
    """Path to one item's source document, whether or not it exists."""
    cfg = cfg if cfg is not None else load(name)
    return os.path.join(items_dir(name, cfg), folder,
                        kind(cfg)["source_file"])


def note(name, folder, cfg=None):
    """Path to one item's note, whether or not it exists."""
    return os.path.join(items_dir(name, cfg), folder, "note.md")


def manifest(name):
    return os.path.join(SOURCES, name, "manifest.csv")


PROFILE = "SOURCE-PROFILE.md"


def profile(name):
    return os.path.join(SOURCES, name, PROFILE)


# The note length band for a podcast episode, which runs 3,000 to 10,000 words
# and is always several times longer than its note.
WORD_MIN, WORD_MAX = 900, 2000

# Roughly the shortest a note can be while still carrying seven sections, a
# date stamp and an attribution on every claim. Below this the format itself is
# the binding constraint rather than the material, which matters for the
# handful of posts shorter than a note.
FORMAT_FLOOR = 400


def word_band(kind, source_words):
    """The sensible note length for a document of this size.

    A transcript is always several times longer than its note, so the fixed
    900-2,000 band works and is left alone: it was tuned against 125 podcast
    notes, and scaling it retroactively re-flagged five of them that had been
    clean for no reason connected to their quality.

    Essays are the case it does not fit. In the Steel For Fuel archive 12 of
    57 posts are themselves under 900 words and the shortest is 266. Holding
    those to the transcript floor would demand a note up to five times the
    length of the thing it summarizes, which is exactly the situation where a
    writer starts supplying facts the source does not contain.

    So for essays the band tracks the source: a note runs between a fifth and
    two thirds of its source, still bounded by the transcript band, so no essay
    note is allowed to run longer than a podcast note would.

    Two thirds rather than a half, because a note has fixed overhead. Seven
    required sections, a date stamp and an attribution on every claim cost
    roughly the same whatever the source length, so a purely proportional rule
    bites hardest in the middle of the range rather than where padding
    actually happens. The existing archive bears this out: across its 136
    podcast notes the median note is 32% of its transcript, but the shortest
    transcripts run far higher, and the shortest of all, at 1,797 words,
    produced an accepted 1,518-word note at 84%. A rule that would reject that
    note is measuring the wrong thing.

    The real floor under this is the separate check that a note may not be
    materially longer than its source, which is an error rather than a warning.
    See over_length().

    Returns the default band when the source length is unknown, which is the
    case in a fresh clone, where documents are not committed and have not been
    fetched yet.
    """
    if kind["items_dir"] != "posts" or not source_words:
        return WORD_MIN, WORD_MAX
    return (max(150, min(WORD_MIN, source_words // 5)),
            min(WORD_MAX, max(FORMAT_FLOOR, source_words * 2 // 3)))


def over_length(kind, note_words, source_words):
    """Whether a note has outgrown the thing it summarizes.

    A note several times the length of its source is not summarizing it, and
    the surplus has to come from somewhere, which in practice means outside
    knowledge. That is worth an error rather than a warning.

    The allowance matters, though. The archive's shortest essay is 248 words,
    and seven sections with an attribution on every claim cannot fit inside
    that however well written they are. Holding a 360-word post to a 360-word
    note would not produce a better note; it would produce a note missing
    sections. So below FORMAT_FLOOR the format is what binds, and the check
    only fires past it.
    """
    if not source_words:
        return False
    return note_words > max(FORMAT_FLOOR, source_words)


def document_words(path):
    """The word count recorded in a source document's frontmatter, or 0."""
    if not path or not os.path.isfile(path):
        return 0
    with open(path, encoding="utf-8") as f:
        head = f.read(2000)
    import re
    m = re.search(r"^(?:transcript_)?word_count: (\d+)", head, re.M)
    return int(m.group(1)) if m else 0


def any_source_doc(folder_path):
    """Path to whichever source document is in this folder, or None.

    For code that walks folders without knowing the content type, such as
    dedupe, which compares every document in the archive against every other.
    """
    for spec in CONTENT_TYPES.values():
        path = os.path.join(folder_path, spec["source_file"])
        if os.path.isfile(path):
            return path
    return None
