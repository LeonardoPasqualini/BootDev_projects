import unittest
from src.markdown_blocks import BlockType, block_to_block_type, markdown_to_blocks

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        
    def test_paragrath_to_block_type(self):
        text = "This is a paragraph"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
        
    def test_header_to_block_type(self):
        text = "# This is a header"
        self.assertEqual(block_to_block_type(text), BlockType.HEADING)
        
    def test_code_to_block_type(self):
        text = "```\nthis is a code bloc\n```"
        self.assertEqual(block_to_block_type(text), BlockType.CODE)
        
    def test_quote_to_block_type(self):
        text = """
> This
> a quote
        """
        blocks = markdown_to_blocks(text)
        self.assertEqual(block_to_block_type(blocks[0]), BlockType.QUOTE)
        
    def test_unordered_list_to_block_type(self):
        text = """
- This
- is
- unorderd list
        """
        blocks = markdown_to_blocks(text)
        self.assertEqual(block_to_block_type(blocks[0]), BlockType.UNORDERED_LIST)

    def test_unordered_list_to_block_type(self):
            text = """
1. This
2. is
3. unorderd list
            """
            blocks = markdown_to_blocks(text)
            self.assertEqual(block_to_block_type(blocks[0]), BlockType.ORDERED_LIST)