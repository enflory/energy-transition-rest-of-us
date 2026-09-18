#!/usr/bin/env python3
"""
Archive size and coverage.

Usage:
    python scripts/stats.py            # every podcast
    python scripts/stats.py catalyst   # one podcast

Reports note counts, word counts and thread-tag usage. Transcript figures are
only shown when transcripts are present locally; they are not committed, so a
fresh clone reports zero until you run a fetch.
"""

import csv
import io
import os
import re
import statistics
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PODCASTS = os.path.join(ROOT, "podcasts")
SPEC = os.path.join(ROOT, "docs", "NOTE-SPEC.md")


def vocabulary():
    if not os.path.isfile(SPEC):
        return set()
    text = io.open(SPEC, encoding="utf-8").read()
    m = re.search(r"## Controlled vocabulary for `threads`(.*?)```(.*?)```",
                  text, re.S)
    return set(m.group(2).split()) if m else set()


def podcast_names():
    if not os.path.isdir(PODCASTS):
        return []
    return sorted(d for d in os.listdir(PODCASTS)
                  if os.path.isfile(os.path.join(PODCASTS, d, "podcast.json")))


def report(show, vocab):
    episodes_dir = os.path.join(PODCASTS, show, "episodes")
    print(f"\n=== {show} ===")
    if not os.path.isdir(episodes_dir):
        print("  no episodes directory yet")
        return

    folders = sorted(d for d in os.listdir(episodes_dir)
                     if os.path.isdir(os.path.join(episodes_dir, d)))
    note_words, n_tr, tags = [], 0, Counter()

    for folder in folders:
        base = os.path.join(episodes_dir, folder)
        if os.path.isfile(os.path.join(base, "transcript.md")):
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

    manifest = os.path.join(PODCASTS, show, "manifest.csv")
    n_published = n_no_transcript = 0
    if os.path.isfile(manifest):
        with io.open(manifest, encoding="utf-8", newline="") as f:
            for row in csv.reader(f):
                if len(row) == 6 and row[0] != "published":
                    n_published += 1
                    if row[2] == "no transcript":
                        n_no_transcript += 1

    print(f"  episodes seen        {n_published or len(folders)}")
    if n_no_transcript:
        print(f"    of which no transcript published   {n_no_transcript}")
    print(f"  transcripts on disk  {n_tr}"
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
    known = podcast_names()
    if not known:
        sys.exit("no podcasts configured under podcasts/")
    for s in argv:
        if s not in known:
            sys.exit("unknown podcast %r; known: %s" % (s, ", ".join(known)))
    vocab = vocabulary()
    for show in (argv or known):
        report(show, vocab)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
