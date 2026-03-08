import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):

    def test_code_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)

        result = split_nodes_delimiter([node], "`", TextType.CODE)

        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_bold_split(self):
        node = TextNode("This is **bold** text", TextType.TEXT)

        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_italic_split(self):
        node = TextNode("This is _italic_ text", TextType.TEXT)

        result = split_nodes_delimiter([node], "_", TextType.ITALIC)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_multiple_splits(self):
        node = TextNode("This has `code` and `more code`", TextType.TEXT)

        result = split_nodes_delimiter([node], "`", TextType.CODE)

        expected = [
            TextNode("This has ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("more code", TextType.CODE),
        ]

        self.assertEqual(result, expected)

    def test_invalid_markdown(self):
        node = TextNode("This has `broken markdown", TextType.TEXT)

        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_non_text_node(self):
        node = TextNode("bold", TextType.BOLD)

        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(result, [node])


if __name__ == "__main__":
    unittest.main()