#!/usr/bin/env python3
"""
Structural validation for episode notes.

Usage:
    python scripts/validate_notes.py                     # every source
    python scripts/validate_notes.py catalyst            # one source
    python scripts/validate_notes.py catalyst <folder>   # specific items

Checks structure only. It cannot tell you whether a note is accurate or whether
it captured the episode's argument; those need a human or a verification pass.
What it does catch is the mechanical failures that would otherwise hide inside a
120-note batch: missing sections, invented thread tags, bulleted argument
sections, unattributed claims, placeholder text.

Exit code is 0 when no note has an ERROR, 1 otherwise.
"""

import os
import re
import sys

import archive

ROOT = archive.ROOT
SPEC = os.path.join(ROOT, "docs", "NOTE-SPEC.md")

REQUIRED_SECTIONS = [
    "The question",
    "The answer",
    "The argument",
    "What you need to know first",
    "Details worth keeping",
    "Claims worth citing",
    "Where it's contested",
]

# Three of these are named differently for an essay: `post` rather than
# `episode`, `author` rather than `guest`, and `source_document` rather than
# `source_transcript`. archive.py holds which is which.
SHARED_FRONTMATTER = ["published", "threads", "note_version"]

OPTIONAL_FRONTMATTER = ["age_warning", "disclosure", "proposed_threads"]


def required_frontmatter(kind):
    return SHARED_FRONTMATTER + [kind["note_title_field"],
                                 kind["note_author_field"],
                                 kind["note_source_field"]]


def known_frontmatter():
    """Every field name valid for any content type.

    Used to decide whether an unexpected field is a typo. A podcast note
    carrying `author` is worth a warning, but naming every essay field as
    unexpected in a podcast run would bury the real ones.
    """
    fields = set(SHARED_FRONTMATTER) | set(OPTIONAL_FRONTMATTER)
    for kind in archive.CONTENT_TYPES.values():
        fields |= set(required_frontmatter(kind))
    return fields


PLACEHOLDERS = re.compile(r"\b(TODO|TBD|FIXME|XXX|lorem ipsum|\[insert)\b", re.I)


def load_vocabulary():
    """Parse the controlled thread vocabulary out of the spec.

    The spec is the single source of truth, so the two cannot drift apart.
    """
    if not os.path.isfile(SPEC):
        return None
    text = open(SPEC, encoding="utf-8").read()
    m = re.search(r"## Controlled vocabulary for `threads`(.*?)```(.*?)```",
                  text, re.S)
    if not m:
        return None
    return set(m.group(2).split())


def split_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return None, text
    fields = {}
    for line in m.group(1).split("\n"):
        fm = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if fm:
            fields[fm.group(1)] = fm.group(2).strip()
    return fields, m.group(2)


def section_body(body, heading):
    """Text between this ## heading and the next ## heading."""
    m = re.search(r"^## %s\s*$(.*?)(?=^## |\Z)" % re.escape(heading),
                  body, re.S | re.M)
    return m.group(1).strip() if m else ""


def check(items_dir, folder, vocab, kind):
    """Return (errors, warnings) for one item folder."""
    errors, warnings = [], []
    path = os.path.join(items_dir, folder, "note.md")
    if not os.path.isfile(path):
        return ["no note.md"], []

    text = open(path, encoding="utf-8").read()
    fields, body = split_frontmatter(text)

    required = required_frontmatter(kind)
    if fields is None:
        errors.append("frontmatter missing or malformed")
        fields = {}
    else:
        for key in required:
            if key not in fields:
                errors.append(f"frontmatter missing '{key}'")
        for key in sorted(set(fields) - known_frontmatter()):
            warnings.append(f"unexpected frontmatter field '{key}'")
        # A field belonging to the other content type is a sign the note was
        # written from the wrong half of the spec, which usually means the
        # wrong section structure came with it.
        for key in sorted(set(fields) & known_frontmatter() - set(required)
                          - set(OPTIONAL_FRONTMATTER)):
            warnings.append(
                f"frontmatter field '{key}' belongs to a different content "
                f"type; this source wants '{kind['note_title_field']}', "
                f"'{kind['note_author_field']}' and "
                f"'{kind['note_source_field']}'")

    # Read once, up front: several checks below scale against it. Zero when
    # the document is not on disk, which is the case in a fresh clone.
    source_words = archive.document_words(
        os.path.join(items_dir, folder, kind["source_file"]))

    # Sections present, in order.
    found = re.findall(r"^## (.+?)\s*$", body, re.M)
    for heading in REQUIRED_SECTIONS:
        if heading not in found:
            errors.append(f"missing section '{heading}'")
    ordered = [h for h in found if h in REQUIRED_SECTIONS]
    if ordered != [h for h in REQUIRED_SECTIONS if h in ordered]:
        errors.append("sections out of order")
    for heading in found:
        if heading not in REQUIRED_SECTIONS:
            if "hindsight" in heading.lower():
                errors.append(
                    f"deprecated section '{heading}' (belongs to synthesis)")
            else:
                warnings.append(f"extra section '{heading}'")

    # Thread vocabulary.
    raw = fields.get("threads", "")
    tags = [t.strip().strip('"') for t in raw.strip("[]").split(",")
            if t.strip()]
    if not tags:
        errors.append("no threads assigned")
    elif vocab:
        for t in tags:
            if t not in vocab:
                errors.append(f"thread '{t}' not in controlled vocabulary")
    if len(tags) > 6:
        warnings.append(f"{len(tags)} threads assigned (expected 2-5)")

    # The argument must be prose. This is the anti-pattern the spec exists for.
    argument = section_body(body, "The argument")
    # An ordered-list marker is a small number. Requiring 1-2 digits keeps a
    # sentence that happens to begin "2030." from reading as a list item.
    bullets = [l for l in argument.split("\n")
               if re.match(r"^\s*([-*+]|\d{1,2}\.)\s+", l)]
    if bullets:
        errors.append(f"'The argument' contains {len(bullets)} bullet(s); "
                      "must be prose")
    # The 150-word floor assumes a transcript. It is meaningless against a
    # 360-word post, where it would demand that the argument section alone be
    # 40% of the note.
    arg_floor = min(150, max(60, source_words // 3)) if (
        source_words and kind["items_dir"] == "posts") else 150
    if argument and len(argument.split()) < arg_floor:
        warnings.append(f"'The argument' is only {len(argument.split())} "
                        f"words (floor {arg_floor})")

    # Claims should carry attributions. Bullets wrap across lines, so rejoin
    # each logical bullet before looking for the trailing attribution.
    claims = section_body(body, "Claims worth citing")
    bullets_out, current = [], None
    for line in claims.split("\n"):
        if re.match(r"^\s*[-*+]\s+", line):
            if current is not None:
                bullets_out.append(current)
            current = line.strip()
        elif current is not None and line.strip():
            current += " " + line.strip()
        elif current is not None:
            bullets_out.append(current)
            current = None
    if current is not None:
        bullets_out.append(current)

    attributed = [b for b in bullets_out if re.search(r"\([^)]+\)[.\s]*$", b)]
    if bullets_out and len(attributed) < len(bullets_out) * 0.6:
        warnings.append(f"only {len(attributed)}/{len(bullets_out)} claims "
                        "carry a trailing attribution")
    if not re.search(r"\b20\d\d\b", claims):
        warnings.append("'Claims worth citing' has no date stamp")

    # Contested section should not be empty.
    contested = section_body(body, "Where it's contested")
    if contested and len(contested.split()) < 40:
        warnings.append("'Where it's contested' looks thin")

    floor, ceiling = archive.word_band(kind, source_words)
    scaled = "" if (floor, ceiling) == (archive.WORD_MIN, archive.WORD_MAX) \
        else f" (scaled to a {source_words}-word {kind['document']})"

    words = len(body.split())
    if words < floor:
        warnings.append(f"{words} words, under the {floor} floor{scaled}; a "
                        "thin note usually means the argument is "
                        "underdeveloped")
    elif words > ceiling:
        # Agents see this string at the moment they decide, not the spec. Say
        # the quiet part here: a long note is only a problem if it is padding.
        warnings.append(
            f"{words} words, over the {ceiling} soft ceiling{scaled}. "
            "ADVISORY ONLY. "
            "Ask what the excess is: cut duplication and loose phrasing, but "
            "KEEP attributed figures, reasoning turns and speakers' hedges and "
            "leave this warning standing. Trimming down to clear it is itself "
            "a failure.")
    if archive.over_length(kind, words, source_words):
        errors.append(
            f"the note has outgrown its {kind['document']} "
            f"({words} words against {source_words}). A note that outgrows "
            "its source is no longer summarizing it.")

    if PLACEHOLDERS.search(text):
        errors.append("contains placeholder text")

    # Single-item scope.
    if re.search(r"\b(as we saw in|in another (episode|post)|"
                 r"in a later (episode|post)|elsewhere in this archive)\b",
                 body, re.I):
        warnings.append("appears to reference another item")

    return errors, warnings


def main(argv):
    vocab = load_vocabulary()
    if vocab is None:
        print("WARNING: could not read thread vocabulary from docs/NOTE-SPEC.md\n")

    known = archive.source_names()
    if argv and argv[0] in known:
        sources, folders = [argv[0]], argv[1:]
    elif argv:
        sys.exit("unknown source %r; known: %s" % (argv[0], ", ".join(known)))
    else:
        sources, folders = known, []

    n_err = n_warn = n_ok = n_missing = 0
    for show in sources:
        cfg = archive.load(show)
        kind = archive.kind(cfg)
        items_dir = archive.items_dir(show, cfg)
        if not os.path.isdir(items_dir):
            continue
        targets = folders or archive.item_folders(show, cfg)
        targets = [f.strip("/\\").split(os.sep)[-1] for f in targets]

        for folder in targets:
            has_tr = os.path.isfile(
                os.path.join(items_dir, folder, kind["source_file"]))
            has_note = os.path.isfile(
                os.path.join(items_dir, folder, "note.md"))
            if has_tr and not has_note:
                n_missing += 1
                continue
            if not has_note:
                continue

            errors, warnings = check(items_dir, folder, vocab, kind)
            label = f"{show}/{folder}" if len(sources) > 1 else folder
            if errors:
                n_err += 1
                print(f"FAIL  {label}")
                for e in errors:
                    print(f"        ERROR   {e}")
                for w in warnings:
                    print(f"        warn    {w}")
            elif warnings:
                n_warn += 1
                print(f"WARN  {label}")
                for w in warnings:
                    print(f"        warn    {w}")
            else:
                n_ok += 1

    print("\n" + "-" * 60)
    print(f"  clean           {n_ok}")
    print(f"  warnings only   {n_warn}")
    print(f"  failed          {n_err}")
    if n_missing:
        print(f"  no note yet     {n_missing}")
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
