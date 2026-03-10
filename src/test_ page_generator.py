import unittest

from page_generator import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# Hello"
        self.assertEqual(extract_title(markdown), "Hello")

    def test_extract_title_with_spaces(self):
        markdown = "#   Hello World   "
        self.assertEqual(extract_title(markdown), "Hello World")

    def test_extract_title_multiline(self):
        markdown = """
## Not this one
# Real Title

Some paragraph
"""
        self.assertEqual(extract_title(markdown), "Real Title")

    def test_extract_title_raises(self):
        markdown = "## No h1 here"
        with self.assertRaises(Exception):
            extract_title(markdown)


if __name__ == "__main__":
    unittest.main()