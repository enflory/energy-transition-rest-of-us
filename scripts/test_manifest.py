"""Regression tests for the manifest merge in scrape.py.

    python3 scripts/test_manifest.py        (add -v for each test's name)

write_manifest has lost data twice. An early version rewrote the Catalyst
manifest (podcast) wholesale, and a partial run cut it from 146 rows to 48.
On 2026-11-11 a blocked Catalyst fetch rewrote 20 of its 21 dated "no
transcript" rows as undated errors, which also made them look like pending
work to the status check. These tests pin the merge order that prevents
both. They make no network requests and write only to a temporary
directory; the committed Catalyst manifest is copied, never written.

They replace scrape.py's module globals (ROOT, OUT_ROOT, MANIFEST) and, for
the end-to-end case, load_config, fetch and parse. A refactor of those names
needs this file updated with it.
"""
import csv
import email.message
import errno
import os
import shutil
import socket
import ssl
import sys
import tempfile
import unittest
import urllib.error

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(SCRIPTS)
sys.path.insert(0, SCRIPTS)
import scrape  # noqa: E402

HEADER = ["published", "title", "status", "words", "folder", "url"]
U = "https://example.com/a"
NT = ["2023-11-03", "slug-a", "no transcript", "", "", U]
NT2 = ["2023-11-04", "slug-a", "no transcript", "", "", U]
ERR = ["", "slug-a", "error: HTTPError", "", "", U]
ERR2 = ["", "slug-a", "error: URLError", "", "", U]
PERR = ["", "slug-a", "error: IndexError", "", "", U]
SAVED = ["2024-01-01", "T", "saved", "10", "2024-01-01-t", U]


def http_error(code):
    return urllib.error.HTTPError("https://example.com/", code, "msg",
                                  email.message.Message(), None)


def read(path):
    with open(path, encoding="utf-8", newline="") as f:
        return {r[5]: r for r in csv.reader(f)
                if len(r) == 6 and r[0] != "published"}


class ScrapeTestCase(unittest.TestCase):
    """Points scrape.py at a temp directory and restores it afterwards."""

    SOURCE = "catalyst"  # a podcast source, whose middle status is "no transcript"

    def patch(self, obj, name, value):
        # Register the restore before anything else can fail, so a broken
        # setUp never leaves the module patched for the tests that follow.
        self.addCleanup(setattr, obj, name, getattr(obj, name))
        setattr(obj, name, value)

    def setUp(self):
        self.patch(scrape.time, "sleep", lambda seconds: None)
        for name in ("ROOT", "OUT_ROOT", "MANIFEST", "CFG", "KIND",
                     "load_config", "fetch", "parse"):
            self.patch(scrape, name, getattr(scrape, name))
        scrape.load_config(self.SOURCE)
        self.tmp = tempfile.mkdtemp(prefix="test-manifest-")
        self.addCleanup(shutil.rmtree, self.tmp, True)
        scrape.OUT_ROOT = os.path.join(self.tmp, "items")
        scrape.MANIFEST = os.path.join(self.tmp, "manifest.csv")
        os.makedirs(scrape.OUT_ROOT)

    def write_prior(self, rows):
        with open(scrape.MANIFEST, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, lineterminator="\n")
            w.writerow(HEADER)
            w.writerows(rows)

    def save_document(self, folder, url):
        d = os.path.join(scrape.OUT_ROOT, folder)
        os.makedirs(d)
        with open(os.path.join(d, scrape.KIND["source_file"]), "w",
                  encoding="utf-8") as f:
            f.write(f'---\ntitle: "T"\nurl: "{url}"\n'
                    f'published: "2024-01-01T00:00:00"\nword_count: 10\n---\n')

    def merged(self, prior, rows, unreached=(), saved=()):
        self.write_prior(prior)
        for folder, url in saved:
            self.save_document(folder, url)
        self.kept = scrape.write_manifest(rows, set(unreached))
        return read(scrape.MANIFEST)


class Unreachable(unittest.TestCase):
    """Which exceptions from fetch() learned nothing about the item."""

    def test_only_404_and_410_say_the_page_is_gone(self):
        for code in (404, 410):
            with self.subTest(code=code):
                self.assertFalse(scrape.unreachable(http_error(code)))

    def test_every_other_http_status_is_the_route(self):
        # 301/302 arrive here when urllib gives up on a redirect loop.
        for code in (301, 302, 400, 401, 403, 407, 408, 429, 451, 500, 503):
            with self.subTest(code=code):
                self.assertTrue(scrape.unreachable(http_error(code)))

    def test_network_level_failures(self):
        for exc in (urllib.error.URLError("dns"), socket.timeout(),
                    ConnectionResetError(), ssl.SSLEOFError(),
                    OSError(errno.EHOSTUNREACH, "no route")):
            with self.subTest(exc=type(exc).__name__):
                self.assertTrue(scrape.unreachable(exc))


class MergeOrder(ScrapeTestCase):

    def test_unreached_keeps_the_no_document_row(self):
        self.assertEqual(self.merged([NT], [ERR], unreached=[U])[U], NT)
        self.assertEqual(self.kept, 1)

    def test_reached_errors_replace_the_row(self):
        # A parse failure or a 404: the page answered, so the error is news.
        self.assertEqual(self.merged([NT], [PERR])[U], PERR)
        self.assertEqual(self.kept, 0)

    def test_new_url_records_its_error(self):
        self.assertEqual(self.merged([], [ERR], unreached=[U])[U], ERR)

    def test_newer_error_replaces_earlier_error(self):
        self.assertEqual(self.merged([ERR], [ERR2], unreached=[U])[U], ERR2)

    def test_outcome_replaces_earlier_error(self):
        self.assertEqual(self.merged([ERR], [NT2])[U], NT2)

    def test_outcome_replaces_earlier_outcome(self):
        self.assertEqual(self.merged([NT], [NT2])[U], NT2)

    def test_saved_on_disk_survives_an_unreached_error(self):
        got = self.merged([SAVED], [ERR], unreached=[U],
                          saved=[("2024-01-01-t", U)])
        self.assertEqual(got[U], SAVED)

    def test_saved_row_on_a_fresh_clone_survives_an_unreached_error(self):
        # Documents are gitignored, so on a fresh clone no saved row has its
        # document on disk and rows_from_disk() cannot restore it.
        self.assertEqual(self.merged([SAVED], [ERR], unreached=[U])[U], SAVED)
        self.assertEqual(self.kept, 1)

    def test_untouched_rows_are_never_dropped(self):
        other = ["2022-01-01", "slug-b", "no transcript", "", "",
                 "https://example.com/b"]
        got = self.merged([NT, other], [NT2])
        self.assertEqual(got[other[5]], other)


class EssaySource(ScrapeTestCase):
    """An essay source's middle status reads "no essay", not "no transcript"."""

    SOURCE = "steel-for-fuel"

    def test_unreached_keeps_the_no_essay_row(self):
        self.assertEqual(scrape.KIND["document"], "essay")
        row = ["2024-05-01", "slug-a", "no essay", "", "", U]
        self.assertEqual(self.merged([row], [ERR], unreached=[U])[U], row)


class ReplayOnAFreshClone(ScrapeTestCase):
    """A fetch on a fresh clone, where every saved document is absent, is
    blocked on every URL. The committed Catalyst manifest must come through
    unchanged: every saved row and every "no transcript" row.
    """

    def test_fully_blocked_fetch_leaves_the_manifest_unchanged(self):
        shutil.copy(os.path.join(REPO, "sources", "catalyst", "manifest.csv"),
                    scrape.MANIFEST)
        before = read(scrape.MANIFEST)
        self.assertGreater(len(before), 100, "expected the full manifest")
        rows = [["", u.rstrip("/").rsplit("/", 1)[-1], "error: HTTPError",
                 "", "", u] for u in before]
        kept = scrape.write_manifest(rows, set(before))
        self.assertEqual(read(scrape.MANIFEST), before)
        self.assertEqual(kept, sum(1 for r in before.values()
                                   if not r[2].startswith("error")))


class FetchLoop(ScrapeTestCase):
    """main() marks a URL unreached only when fetch() never got the page."""

    BLOCKED = "https://example.com/blocked"
    BLOCKED_SAVED = "https://example.com/blocked-saved"
    GONE = "https://example.com/gone"
    CRASH = "https://example.com/crash"
    NEW = "https://example.com/new"

    def test_only_unreached_pages_keep_their_rows(self):
        prior = [["2023-01-01", s, "no transcript", "", "", u]
                 for s, u in [("blocked", self.BLOCKED), ("gone", self.GONE),
                              ("crash", self.CRASH)]]
        saved = ["2023-02-01", "Saved", "saved", "900", "2023-02-01-saved",
                 self.BLOCKED_SAVED]
        self.write_prior(prior + [saved])
        paths = (scrape.OUT_ROOT, scrape.MANIFEST)
        real_load = scrape.load_config

        def load_config(source):
            real_load(source)
            scrape.OUT_ROOT, scrape.MANIFEST = paths
            # main() prints MANIFEST relative to ROOT; on Windows relpath()
            # fails across drives, so keep both in the temp directory.
            scrape.ROOT = self.tmp
            return scrape.CFG

        def fetch(url):
            if url in (self.BLOCKED, self.BLOCKED_SAVED, self.NEW):
                raise http_error(403)
            if url == self.GONE:
                raise http_error(404)
            return "<html>a page that arrived</html>"

        def parse(page, url):
            raise IndexError("a layout the parser has not seen")

        scrape.load_config, scrape.fetch, scrape.parse = load_config, fetch, parse
        with open(os.devnull, "w") as quiet:
            stdout, sys.stdout = sys.stdout, quiet
            try:
                scrape.main(["catalyst", self.BLOCKED, self.BLOCKED_SAVED,
                             self.GONE, self.CRASH, self.NEW, self.BLOCKED])
            finally:
                sys.stdout = stdout

        got = read(scrape.MANIFEST)
        self.assertEqual(got[self.BLOCKED], prior[0])
        self.assertEqual(got[self.BLOCKED_SAVED], saved)
        self.assertEqual(got[self.GONE][2], "error: HTTPError")
        self.assertEqual(got[self.CRASH][2], "error: IndexError")
        self.assertEqual(got[self.NEW][2], "error: HTTPError")


if __name__ == "__main__":
    unittest.main()
