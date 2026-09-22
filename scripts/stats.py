#!/usr/bin/env python3
"""
Archive size and coverage.

Usage:
    python scripts/stats.py            # every source
    python scripts/stats.py catalyst   # one source

Reports note counts, word counts and thread-tag usage. Source-document figures
are only shown when the documents are present locally; they are not committed,
so a fresh clone reports zero until you run a fetch.
"""

import csv
import io
import os
import re
import statistics
import sys
from collections import Counter

import archive

ROOT = archive.ROOT
SPEC = os.path.join(ROOT, "docs", "NOTE-SPEC.md")


def vocabulary():
    if not os.path.isfile(SPEC):
        return set()
    text = io.open(SPEC, encoding="utf-8").read()
    m = re.search(r"## Controlled vocabulary for `threads`(.*?)```(.*?)```",
                  text, re.S)
    return set(m.group(2).split()) if m else set()


def report(show, vocab):
    cfg = archive.load(show)
    kind = archive.kind(cfg)
    items_dir = archive.items_dir(show, cfg)
    print(f"\n=== {show} ===")
    if not os.path.isdir(items_dir):
        print(f"  no {kind['items_dir']} directory yet")
        return

    folders = archive.item_folders(show, cfg)
    note_words, n_tr, tags = [], 0, Counter()

    for folder in folders:
        base = os.path.join(items_dir, folder)
        if os.path.isfile(os.path.join(base, kind["source_file"])):
            n_tr += 1
        note = os.path.join(base, "note.md")
        if not os.path.isfile(note):
            continue
        text = io.open(note, encoding="utf-8").read()
        body = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
        note_words.append(len(body.split()))
        m = re.search(r"^threads:\s*\[(.*?)\]", text, re.M)
        if m:
            for t in m.group(1).split(","):
                if t.strip():
                    tags[t.strip()] += 1

    manifest = archive.manifest(show)
    n_published = n_missing = 0
    if os.path.isfile(manifest):
        with io.open(manifest, encoding="utf-8", newline="") as f:
            for row in csv.reader(f):
                if len(row) == 6 and row[0] != "published":
                    n_published += 1
                    if row[2] == "no " + kind["document"]:
                        n_missing += 1

    print(f"  {kind['items'] + ' seen':<20} {n_published or len(folders)}")
    if n_missing:
        print(f"    of which no {kind['document']} published   {n_missing}")
    print(f"  {kind['documents'] + ' on disk':<20} {n_tr}"
          + ("" if n_tr else "   (run: python run.py fetch %s)" % show))
    print(f"  notes                {len(note_words)}")
    if note_words:
        w = sorted(note_words)
        print(f"  note words           {sum(w):,} total")
        print(f"  median / mean        {statistics.median(w):.0f} / "
              f"{statistics.mean(w):.0f}")
        print(f"  range                {w[0]} - {w[-1]}")
    if tags:
        unused = len(vocab) - len(tags) if vocab else 0
        print(f"  thread tags in use   {len(tags)}"
              + (f" of {len(vocab)} ({unused} unused)" if vocab else ""))
        print("  most used:")
        for k, v in tags.most_common(8):
            print(f"     {k:<24} {v}")


def main(argv):
    known = archive.source_names()
    if not known:
        sys.exit("no sources configured under sources/")
    for s in argv:
        if s not in known:
            sys.exit("unknown source %r; known: %s" % (s, ", ".join(known)))
    vocab = vocabulary()
    for show in (argv or known):
        report(show, vocab)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
