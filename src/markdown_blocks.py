from enum import Enum
import re


from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node


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
    if re.fullmatch(r"#{1,6} .*", block):
        return BlockType.HEADING
    if re.fullmatch(r"```.*```", block, flags=re.DOTALL):
        return BlockType.CODE
    if re.fullmatch(r"(>.*(\n|$))+", block):
        return BlockType.QUOTE
    if re.fullmatch(r"([*-] .*(\n|$))+", block):
        return BlockType.UL
    if re.fullmatch(r"(\d+\. .*(\n|$))+", block):
        for i, line in enumerate(block.splitlines(), start=1):
            if not line.startswith(f"{i}"):
                return BlockType.PARAGRAPH
        return BlockType.OL
    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)

        html_node = None
        match block_type:
            case BlockType.PARAGRAPH:
                html_node = paragraph_to_html_node(block)
            case BlockType.HEADING:
                html_node = heading_to_html_node(block)
            case BlockType.CODE:
                html_node = code_to_html_node(block)
            case BlockType.QUOTE:
                html_node = quote_to_html_node(block)
            case BlockType.UL:
                html_node = unordered_list_to_html_node(block)
            case BlockType.OL:
                html_node = ordered_list_to_html_node(block)
        children.append(html_node)

    return ParentNode("div", children=children)


def text_to_children(text):
    textnodes = text_to_textnodes(text)
    children = [text_node_to_html_node(textnode) for textnode in textnodes]

    return children


def paragraph_to_html_node(block):
    lines = block.splitlines()
    text = " ".join(lines)
    children = text_to_children(text)

    return ParentNode("p", children)


def heading_to_html_node(block):
    (hashes, text) = re.fullmatch(r"(#{1,6}) (.*)", block).groups()
    children = text_to_children(text)

    return ParentNode(f"h{len(hashes)}", children)


def code_to_html_node(block):
    text = block[4:-3]
    children = text_to_children(text)
    code_html_node = ParentNode("code", children)

    return ParentNode("pre", [code_html_node])


def quote_to_html_node(block):
    lines = block.splitlines()
    lines = [line.removeprefix(">").strip() for line in lines]
    text = " ".join(lines)
    children = text_to_children(text)

    return ParentNode("blockquote", children)


def unordered_list_to_html_node(block):
    lines = block.splitlines()
    children = [ParentNode("li", text_to_children(line[2:])) for line in lines]

    return ParentNode("ul", children)


def ordered_list_to_html_node(block):
    lines = block.splitlines()
    children = [ParentNode("li", text_to_children(line[3:])) for line in lines]

    return ParentNode("ol", children)
