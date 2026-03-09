from textnode import TextNode, TextType
from copy_static import copy_static


def main():

    # debug
    node = TextNode(
        "This is some anchor text",
        TextType.LINK,
        "https://www.boot.dev"
    )
    print(node)

    # копирование static
    copy_static("static", "public")


if __name__ == "__main__":
    main()