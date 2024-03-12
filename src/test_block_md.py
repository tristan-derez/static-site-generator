import unittest
from block_md import (
    block_to_block_type,
    markdown_to_blocks,
    blocktype_paragraph,
    blocktype_quote,
    blocktype_code,
    blocktype_heading,
    blocktype_olist,
    blocktype_ulist,
)


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is an *italic* paragraph

This is another paragraph with **bolded** text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is an *italic* paragraph",
                "This is another paragraph with **bolded** text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), blocktype_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), blocktype_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), blocktype_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), blocktype_ulist)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), blocktype_olist)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), blocktype_paragraph)


if __name__ == "__main__":
    unittest.main()
