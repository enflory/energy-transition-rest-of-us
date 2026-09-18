#!/usr/bin/env python3
"""
Find republished episodes: two folders holding the same conversation.

Usage:
    python scripts/dedupe_check.py            # every podcast
    python scripts/dedupe_check.py catalyst   # one podcast

Why this exists: publishers rerun episodes. The Catalyst archive contains two
folders, eleven months apart with different slugs, that hold the same interview
with the same guest. Nothing about the filenames or the frontmatter reveals it.
Any count of episodes, and any thread-frequency tally, silently double-counts
that conversation unless someone knows.

Method: compare 5-gram sets of the transcript body with frontmatter stripped,
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

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PODCASTS = os.path.join(ROOT, "podcasts")

THRESHOLD = 0.25   # containment above this is worth a human look


def shingles(path):
    text = io.open(path, encoding="utf-8", errors="replace").read()
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
    words = [w for w in re.findall(r"[a-z']+", text.lower()) if len(w) > 3]
    return set(zip(words, words[1:], words[2:], words[3:], words[4:]))


def podcast_names():
    if not os.path.isdir(PODCASTS):
        return []
    return sorted(d for d in os.listdir(PODCASTS)
                  if os.path.isfile(os.path.join(PODCASTS, d, "podcast.json")))


def scan(show):
    episodes_dir = os.path.join(PODCASTS, show, "episodes")
    if not os.path.isdir(episodes_dir):
        return []

    docs = {}
    for folder in sorted(os.listdir(episodes_dir)):
        path = os.path.join(episodes_dir, folder, "transcript.md")
        if os.path.isfile(path):
            docs[folder] = shingles(path)
    print(f"{show}: {len(docs)} transcripts compared")
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
    known = podcast_names()
    if not known:
        sys.exit("no podcasts configured under podcasts/")
    shows = argv or known
    for s in shows:
        if s not in known:
            sys.exit("unknown podcast %r; known: %s" % (s, ", ".join(known)))

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
