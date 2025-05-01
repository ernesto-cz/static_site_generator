import unittest
from block_markdown import (
    markdown_to_blocks,
    block_to_block,
    BlockType
)

class TestBlockMarkdown(unittest.TestCase):

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

    def test_markdown_to_blocks2(self):
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

    def test_block_to_block_header(self):
        block = "###### Heading 6"
        btb = block_to_block(block)
        self.assertEqual(
            btb,
            BlockType.HEADING
        )

    def test_block_to_block_header2(self):
        md = "####### Heading 6"
        with self.assertRaises(ValueError) as cm:
            block_to_block(md)
        self.assertEqual(
            'Invalid synstax: Heading level must be between 1 and 6 (e.g., "#" to "######")',
            str(cm.exception)
        )

    def test_block_to_block_ordered_list(self):
        md = """
            1. Item 1
            2. Item 2
            3. Item 3
            4. Item 4
            5. Item 5
            6. Item 6
            7. Item 7
            8. Item 8
            9. Item 9
            10. Item 10
            """
        blocks = markdown_to_blocks(md)
        btb = block_to_block(blocks[0])
        self.assertEqual(
            btb,
            BlockType.ORDERED
        )

    def test_block_to_block_ordered_list2(self):
        md = """
            1. Item 1
            2. Item 2
            3. Item 3
            4. Item 4
            5. Item 5
            6. Item 6
            7. Item 7
            8. Item 8
            11. Item 9
            10. Item 10
            """
        blocks = markdown_to_blocks(md)
        with self.assertRaises(ValueError) as cm:
            block_to_block(blocks[0])
        self.assertEqual(
            'Invalid syntax: Order list line number mistmach - current line is 11, but expected 9.',
            str(cm.exception)
        )

    def test_block_to_block_quoute(self):
        md = """
        > Somewhere, something incredible is waiting to
        be known
        """
        blocks = markdown_to_blocks(md)
        btb = block_to_block(blocks[0])
        self.assertEqual(
            btb,
            BlockType.QUOTE
        )

    def test_block_to_block_quote_raise(self):
        md = """
        >> Somewhere, something incredible is waiting to
        be known
        """
        blocks = markdown_to_blocks(md)
        with self.assertRaises(ValueError) as cm:
            block_to_block(blocks[0])
        self.assertEqual(
            'Invalid syntax: Code level to open or close most be 1 (e.g., >)',
            str(cm.exception)
        )

    def test_block_to_block_code(self):
        md = """
        ```
        This is code
        ```
        """
        blocks = markdown_to_blocks(md)
        btb = block_to_block(blocks[0])
        self.assertEqual(
            btb,
            BlockType.CODE
        )

    def test_block_to_block_code_raise(self):
        md = """
            ````
            This is code
            ```
        """
        blocks = markdown_to_blocks(md)
        with self.assertRaises(ValueError) as cm:
            block_to_block(blocks[0])
        self.assertEqual(
            'Invalid syntax: Code level to open or close most be 3 (e.g., ```)',
            str(cm.exception)
        )

    def test_block_to_block_unordered(self):
        md = """
        - This is a list
        - with items
        - more items
        """
        blocks = markdown_to_blocks(md)
        btb = block_to_block(blocks[0])
        self.assertEqual(
            btb,
            BlockType.UNORDERED
        )

    def test_block_to_block_unordered_raise(self):
        md = """
        - This is a list
        with items
        - more items
        """
        blocks = markdown_to_blocks(md)
        with self.assertRaises(ValueError) as cm:
            block_to_block(blocks[0])
        self.assertEqual(
            'Invalid syntax: Unordered list - missing "- " at begingin of line 2',
            str(cm.exception)
        )

    def test_block_to_block_paragraph(self):
        block = " ###### Heading 6"
        btb = block_to_block(block)
        self.assertEqual(
            btb,
            BlockType.PARAGRAPH
        )

    def test_block_to_block_paragraph2(self):
        md = """
        ADDN - This is a list
        > - with items
        TASD - more items
        """
        blocks = markdown_to_blocks(md)
        btb = block_to_block(blocks[0])
        self.assertEqual(
            btb,
            BlockType.PARAGRAPH
        )

    def test_block_to_block_code_paragraph3(self):
        md = """
            this is text
            ``` hi
            This is code
            >
        """
        blocks = markdown_to_blocks(md)
        btb = block_to_block(blocks[0])
        self.assertEqual(
            btb,
            BlockType.PARAGRAPH
        )

    def test_block_to_block_code_paragraph4(self):
        md = """
            a.1. Item 1
            a.2. Item 2
            a.3. Item 3
            a.4. Item 4
            a.5. Item 5
            a.6. Item 6
            a.7. Item 7
            a.8. Item 8
            a.9. Item 9
            a.10. Item 10
            """
        blocks = markdown_to_blocks(md)
        btb = block_to_block(blocks[0])
        self.assertEqual(
            btb,
            BlockType.PARAGRAPH
        )

if __name__ == "__main__":
    unittest.main()
