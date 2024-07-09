import unittest

from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType,
)


class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside it.

* This is a list item
* This is another list item
"""

        self.assertEqual(
            markdown_to_blocks(markdown),
            [
                "# This is a heading",
                (
                    "This is a paragraph of text. It has some **bold** and"
                    " *italic* words inside it."
                ),
                "* This is a list item\n* This is another list item",
            ],
        )

    def test_markdown_to_blocks_new_lines(self):
        markdown = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""

        self.assertEqual(
            markdown_to_blocks(markdown),
            [
                "This is **bolded** paragraph",
                (
                    "This is another paragraph with *italic* text and `code`"
                    " here\nThis is the same paragraph on a new line"
                ),
                "* This is a list\n* with items",
            ],
        )


class TestBlockToType(unittest.TestCase):
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), BlockType.UL)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.OL)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
