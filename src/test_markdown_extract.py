import unittest

from markdown_extract import extract_markdown_images, extract_markdown_links


class TestMarkdownExtract(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )

        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")],
            matches,
        )

    def test_extract_multiple_images(self):
        text = (
            "Text ![rick](https://img.com/rick.gif) "
            "and ![obi](https://img.com/obi.jpeg)"
        )

        matches = extract_markdown_images(text)

        self.assertListEqual(
            [
                ("rick", "https://img.com/rick.gif"),
                ("obi", "https://img.com/obi.jpeg"),
            ],
            matches,
        )

    def test_extract_markdown_links(self):
        text = "A link [to boot dev](https://www.boot.dev)"

        matches = extract_markdown_links(text)

        self.assertListEqual(
            [("to boot dev", "https://www.boot.dev")],
            matches,
        )

    def test_extract_multiple_links(self):
        text = (
            "Links [boot](https://boot.dev) "
            "and [youtube](https://youtube.com)"
        )

        matches = extract_markdown_links(text)

        self.assertListEqual(
            [
                ("boot", "https://boot.dev"),
                ("youtube", "https://youtube.com"),
            ],
            matches,
        )


if __name__ == "__main__":
    unittest.main()