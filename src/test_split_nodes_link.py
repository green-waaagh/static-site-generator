import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_link


class TestSplitNodesLink(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )

    def test_split_single_link(self):
        node = TextNode(
            "Before [Google](https://google.com) after",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Before ", TextType.TEXT),
                TextNode("Google", TextType.LINK, "https://google.com"),
                TextNode(" after", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_link_only(self):
        node = TextNode(
            "[Boot.dev](https://boot.dev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Boot.dev", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes,
        )

    def test_split_no_links(self):
        node = TextNode("Just plain text", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)

    def test_split_non_text_node_unchanged(self):
        node = TextNode("italic", TextType.ITALIC)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)