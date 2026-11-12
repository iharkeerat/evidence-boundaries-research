"""Checks local research-data structure, not media accuracy or administrative truth."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from verify_corpus import load, urlkey, main

class TestCorpusStructure(unittest.TestCase):
    def test_declared_diagnostic_count(self):
        rows = load("diagnostic_claims_12.csv", ["id", "article_url"])
        self.assertEqual(len(rows), 12)

    def test_retrospective_count(self):
        rows = load("outlet_event_grid_10.csv", ["event", "outlet"])
        self.assertEqual(len(rows), 10)

    def test_structural_verification(self):
        main()  # Checks declared code totals, page types and cross-dataset overlap.

    def test_amp_normalization(self):
        self.assertEqual(
            urlkey("https://example.org/article/amp/1"),
            urlkey("https://example.org/article")
        )

    def test_reject_non_https(self):
        with self.assertRaises(ValueError):
            urlkey("file:///local/private.txt")

if __name__ == "__main__":
    unittest.main()
