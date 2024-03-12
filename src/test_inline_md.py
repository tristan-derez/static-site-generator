import unittest
from inline_md import (
    extract_markdown_links,
    extract_markdown_images,
    split_nodes_delimiter,
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)


class TestInlineMD(unittest.TestCase):
    def test_delimiter_italic(self):
        node = TextNode("A text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("A text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delimiter_code(self):
        node = TextNode("A text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("A text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delimiter_bold(self):
        node = TextNode("A text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("A text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delimiter_double_bold(self):
        node = TextNode("A text with a **bolded** word and **another**", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("A text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_section_not_closed(self):
        node = TextNode("A text with a `code block not closed", text_type_text)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", text_type_code)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is a text with an ![image](https://i.imgur.com/blabla.jpg)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/blabla.jpg")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is a text with a normal [link](https://example.com)"
        )
        self.assertListEqual([("link", "https://example.com")], matches)

    def test_extract_markdown_multilinks(self):
        matches = extract_markdown_links(
            "This is a text with a normal [link](https://example.com) and [another one](https://dev.link.com/dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://example.com"),
                ("another one", "https://dev.link.com/dev"),
            ],
            matches,
        )


if __name__ == "__main__":
    unittest.main()
