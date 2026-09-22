#!/usr/bin/env python3
"""
Find republished items: two folders holding the same conversation or essay.

Usage:
    python scripts/dedupe_check.py            # every source
    python scripts/dedupe_check.py catalyst   # one source

Why this exists: publishers rerun episodes. The Catalyst archive contains two
folders, eleven months apart with different slugs, that hold the same interview
with the same guest. Nothing about the filenames or the frontmatter reveals it.
Any count of episodes, and any thread-frequency tally, silently double-counts
that conversation unless someone knows.

A newsletter has the same failure mode from a different cause. Steel For Fuel
published "For AI, energy is nothing, and energy is everything" and, two years
later, a piece under the same title marked "(reprise)". Those two share no
identical paragraph, so they are genuinely separate pieces and this check
correctly leaves them alone, but the titles alone cannot tell you that.

Method: compare 5-gram sets of the document body with frontmatter stripped,
scoring by containment rather than Jaccard, so a short episode nested inside a
longer one is still caught.

The comparison is exact and all-pairs. An earlier version sampled shingles to
build candidate pairs first; it missed a genuine 99%-overlap pair because the
sampled collisions landed just under its cutoff. At a few hundred episodes the
exact comparison takes seconds, and a correctness check that sometimes misses
is worse than no check at all.

Exit code is 0 when no duplicate pair is found, 1 otherwise.
"""

import io
import itertools
import os
import re
import sys

import archive

ROOT = archive.ROOT

THRESHOLD = 0.25   # containment above this is worth a human look


def shingles(path):
    text = io.open(path, encoding="utf-8", errors="replace").read()
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
    words = [w for w in re.findall(r"[a-z']+", text.lower()) if len(w) > 3]
    return set(zip(words, words[1:], words[2:], words[3:], words[4:]))


def scan(show):
    cfg = archive.load(show)
    kind = archive.kind(cfg)
    items_dir = archive.items_dir(show, cfg)
    if not os.path.isdir(items_dir):
        return []

    docs = {}
    for folder in archive.item_folders(show, cfg):
        path = archive.any_source_doc(os.path.join(items_dir, folder))
        if path:
            docs[folder] = shingles(path)
    print(f"{show}: {len(docs)} {kind['documents']} compared")
    if len(docs) < 2:
        return []

    hits = []
    for a, b in itertools.combinations(sorted(docs), 2):
        A, B = docs[a], docs[b]
        smaller = min(len(A), len(B))
        if not smaller:
            continue
        # Containment cannot exceed the size ratio, so skip pairs that could
        # not clear the threshold even if one were wholly inside the other.
        if smaller / max(len(A), len(B)) < THRESHOLD:
            continue
        containment = len(A & B) / smaller
        if containment > THRESHOLD:
            hits.append((containment, show, a, b))
    return hits


def main(argv):
    known = archive.source_names()
    if not known:
        sys.exit("no sources configured under sources/")
    shows = argv or known
    for s in shows:
        if s not in known:
            sys.exit("unknown source %r; known: %s" % (s, ", ".join(known)))

    hits = []
    for show in shows:
        hits += scan(show)

    if not hits:
        print("\nno near-duplicate transcript pairs found")
        return 0

    print("\n%d possible duplicate pair(s):" % len(hits))
    for containment, show, a, b in sorted(hits, reverse=True):
        print("\n  %.0f%% overlap  [%s]" % (containment * 100, show))
        print("     %s" % a)
        print("     %s" % b)
    print("\nA high-overlap pair is usually a rerun. Keep both notes if they")
    print("differ in substance, but record the pair in the show's")
    print("synthesis/archive-caveats.md so the synthesis layer counts the")
    print("conversation once.")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
