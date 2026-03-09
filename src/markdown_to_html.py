from parentnode import ParentNode
from leafnode import LeafNode
from textnode import TextNode, TextType
from markdown_blocks import BlockType, block_to_block_type
from markdown_blocks import markdown_to_blocks
from inline_markdown import text_to_textnodes
from textnode_utils import text_node_to_html_node


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for tn in text_nodes:
        children.append(text_node_to_html_node(tn))
    return children


def block_to_html_node(block):
    block_type = block_to_block_type(block)

    if block_type == BlockType.PARAGRAPH:
        text = block.replace("\n", " ")
        return ParentNode("p", text_to_children(text))

    if block_type == BlockType.HEADING:
        level = 0
        while block[level] == "#":
            level += 1
        text = block[level + 1 :]
        return ParentNode(f"h{level}", text_to_children(text))

    if block_type == BlockType.QUOTE:
        lines = block.split("\n")
        cleaned = []
        for line in lines:
            cleaned.append(line.lstrip(">").strip())
        text = " ".join(cleaned)
        return ParentNode("blockquote", text_to_children(text))

    if block_type == BlockType.UNORDERED_LIST:
        lines = block.split("\n")
        children = []
        for line in lines:
            item_text = line[2:]
            children.append(ParentNode("li", text_to_children(item_text)))
        return ParentNode("ul", children)

    if block_type == BlockType.ORDERED_LIST:
        lines = block.split("\n")
        children = []
        for line in lines:
            text = line.split(". ", 1)[1]
            children.append(ParentNode("li", text_to_children(text)))
        return ParentNode("ol", children)

    if block_type == BlockType.CODE:
        lines = block.split("\n")
        code = "\n".join(lines[1:-1]) + "\n"
        code_node = LeafNode("code", code)
        return ParentNode("pre", [code_node])

    raise ValueError("Unknown block type")


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        children.append(block_to_html_node(block))

    return ParentNode("div", children)