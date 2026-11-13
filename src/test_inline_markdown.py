import unittest

from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    # split_nodes_delimiter

    def test_code_blocks(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        expected_response = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertEqual(new_nodes, expected_response)

    def test_non_matching_delimiters(self):
        node = TextNode("This is text with non matching delimiters **", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.CODE)

    def test_delimiters_at_start(self):
        node = TextNode("_italic_ non italic", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)

        expected_response = [
            TextNode("italic", TextType.ITALIC),
            TextNode(" non italic", TextType.TEXT),
        ]

        self.assertEqual(new_nodes, expected_response)
    
    def test_delimiters_at_end(self):
        node = TextNode("non italic _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)

        expected_response = [
            TextNode("non italic ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
        ]

        self.assertEqual(new_nodes, expected_response)

    def test_multiple_delimeters(self):
        node = TextNode("non bold **bold** non bold again **bold again**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected_response = [
            TextNode("non bold ", TextType.TEXT, None),
            TextNode("bold", TextType.BOLD, None),
            TextNode(" non bold again ", TextType.TEXT, None),
            TextNode("bold again", TextType.BOLD, None)
        ]

        self.assertEqual(new_nodes, expected_response)

    # extract_markdown_images

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
    def test_extract_markdown_images_with_links(self):
        matches = extract_markdown_images(
            "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual([], matches)
    # extract_markdown_links

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_links("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([], matches)


if __name__ == "__main__":
    unittest.main()