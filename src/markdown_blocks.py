def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")

    cleaned_blocks = []

    for block in blocks:
        block = block.strip()
        if block:
            cleaned_blocks.append(block)

    return cleaned_blocks

from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

import re


def block_to_block_type(block):

    # heading
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING

    # code block
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    lines = block.split("\n")

    # quote
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    # unordered list
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # ordered list
    ordered = True
    for i, line in enumerate(lines):
        if not line.startswith(f"{i+1}. "):
            ordered = False
            break
    if ordered:
        return BlockType.ORDERED_LIST

    # default
    return BlockType.PARAGRAPH