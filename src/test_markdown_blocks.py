import unittest

from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestInlineMarkdown(unittest.TestCase):
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

    def test_markdown_to_blocks_newlines(self):
        md = """
    This is **bolded** paragraph




    This is another paragraph with _italic_ text and `code` here
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here",
            ],
        )

    def test_markdown_to_blocks_whitespace(self):
        md = "   Block with leading spaces.   \n\n   Another block with trailing spaces.   "
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Block with leading spaces.",
                "Another block with trailing spaces.",
            ],
        )

    # block_to_block_type

    def test_block_to_block_type_heading(self):
        block = "# A heading"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.HEADING)

    def test_block_to_block_type_heading2(self):
        block = "## A heading"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.HEADING)

    def test_block_to_block_type_invalid_heading(self):
        block = "#Invalid heading"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_code(self):
        block = """```
        A code 
        ```"""
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.CODE)

    def test_block_to_block_type_multiline_code(self):
        block = """```
        A code
        Another one
        Great Code```"""
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.CODE)

    def test_block_to_block_type_invalid_code(self):
        block = """```A code 
        ```"""
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_quote(self):
        block = """> Quote 1\n> Quote 2"""
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.QUOTE)
    
    def test_block_to_block_type_single_quote(self):
        block = """> Quote 1"""
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.QUOTE)

    def test_block_to_block_type_invalid_quote(self):
        block = """> Quote 1\n Not a quote"""
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_unordered_list(self):
        block = """- Item\n- Item 2"""
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.UNORDERED_LIST)
    
    def test_block_to_block_type_invalid_unordered_list(self):
        block = """- Item\n Not a list item"""
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_ordered_list(self):
        block = """1. Item\n2. Item 2"""
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_block_to_block_type_invalid_ordered_list(self):
        block = """1. Item\n3. Item 2"""
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_paragraph(self):
        block = """A paragraph"""
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)
if __name__ == "__main__":
    unittest.main()