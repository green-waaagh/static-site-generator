import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_multiple(self):
        node = HTMLNode(
            tag="a",
            props={
                "href": "https://www.google.com",
                "target": "_blank"
            }
        )

        result = node.props_to_html()
        expected = ' href="https://www.google.com" target="_blank"'

        self.assertEqual(result, expected)

    def test_props_to_html_single(self):
        node = HTMLNode(
            tag="img",
            props={"src": "image.png"}
        )

        result = node.props_to_html()
        expected = ' src="image.png"'

        self.assertEqual(result, expected)

    def test_props_to_html_none(self):
        node = HTMLNode(tag="p")

        result = node.props_to_html()

        self.assertEqual(result, "")

    def test_props_to_html_empty_dict(self):
        node = HTMLNode(tag="div", props={})

        result = node.props_to_html()

        self.assertEqual(result, "")


if __name__ == "__main__":
    unittest.main()