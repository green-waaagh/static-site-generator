import unittest

from textnode import TextNode, TextType
from inline_markdown import text_to_textnodes


class TestTextToTextNodes(unittest.TestCase):

    def test_full_example(self):
        text = (
            "This is **text** with an _italic_ word and a `code block` "
            "and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) "
            "and a [link](https://boot.dev)"
        )

        nodes = text_to_textnodes(text)

        self.assertEqual(
            nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode(
                    "obi wan image",
                    TextType.IMAGE,
                    "https://i.imgur.com/fJRm4Vk.jpeg",
                ),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
        )

    def test_plain_text(self):
        text = "Just some text"

        nodes = text_to_textnodes(text)

        self.assertEqual(
            nodes,
            [TextNode("Just some text", TextType.TEXT)],
        )

    def test_bold_only(self):
        text = "**bold text**"

        nodes = text_to_textnodes(text)

        self.assertEqual(
            nodes,
            [TextNode("bold text", TextType.BOLD)],
        )

    def test_code_and_text(self):
        text = "Text with `code` here"

        nodes = text_to_textnodes(text)

        self.assertEqual(
            nodes,
            [
                TextNode("Text with ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" here", TextType.TEXT),
            ],
        )

    def test_link_only(self):
        text = "[Boot.dev](https://boot.dev)"

        nodes = text_to_textnodes(text)

        self.assertEqual(
            nodes,
            [
                TextNode("Boot.dev", TextType.LINK, "https://boot.dev"),
            ],
        )


if __name__ == "__main__":
    unittest.main()