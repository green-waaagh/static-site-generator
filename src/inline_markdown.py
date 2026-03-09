from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        if len(parts) % 2 == 0:
            raise Exception("Invalid Markdown syntax: missing closing delimiter")

        for i, part in enumerate(parts):
            if part == "":
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))

    return new_nodes

from textnode import TextNode, TextType
from markdown_extract import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        images = extract_markdown_images(text)

        if not images:
            new_nodes.append(old_node)
            continue

        for alt, url in images:
            image_markdown = f"![{alt}]({url})"
            sections = text.split(image_markdown, 1)

            if len(sections) != 2:
                raise ValueError("invalid markdown image syntax")

            before, text = sections

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))

            new_nodes.append(TextNode(alt, TextType.IMAGE, url))

        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        links = extract_markdown_links(text)

        if not links:
            new_nodes.append(old_node)
            continue

        for anchor, url in links:
            link_markdown = f"[{anchor}]({url})"
            sections = text.split(link_markdown, 1)

            if len(sections) != 2:
                raise ValueError("invalid markdown link syntax")

            before, text = sections

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))

            new_nodes.append(TextNode(anchor, TextType.LINK, url))

        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

from textnode import TextNode, TextType



def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

    return nodes