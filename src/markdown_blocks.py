from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UL = "unordered_list"
    OL = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)

    return filtered_blocks


def block_to_block_type(block):
    if re.fullmatch(r"#{1,6} .*", block) is not None:
        return BlockType.HEADING
    if re.fullmatch(r"```.*```", block, flags=re.DOTALL) is not None:
        return BlockType.CODE
    if re.fullmatch(r"(>.*(\n|$))+", block) is not None:
        return BlockType.QUOTE
    if re.fullmatch(r"([*-] .*(\n|$))+", block) is not None:
        return BlockType.UL
    if re.fullmatch(r"(\d+\. .*(\n|$))+", block) is not None:
        for i, line in enumerate(block.splitlines(), start=1):
            if not line.startswith(f"{i}"):
                return BlockType.PARAGRAPH
        return BlockType.OL
    return BlockType.PARAGRAPH
