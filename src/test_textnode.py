import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_same_props_defaults_url_none(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_not_eq_different_text(self):
        node1 = TextNode("Text A", TextType.TEXT)
        node2 = TextNode("Text B", TextType.TEXT)
        self.assertNotEqual(node1, node2)

    def test_not_eq_different_text_type(self):
        node1 = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_not_eq_different_url_one_none(self):
        node1 = TextNode("Anchor", TextType.LINK, None)
        node2 = TextNode("Anchor", TextType.LINK, "https://example.com")
        self.assertNotEqual(node1, node2)

    def test_not_eq_other_type(self):
        node = TextNode("Hello", TextType.TEXT)
        self.assertNotEqual(node, "Hello")  # different type


if __name__ == "__main__":
    unittest.main()