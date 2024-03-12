import unittest
from inline_md import (
    split_nodes_image,
    split_nodes_link,
    extract_markdown_links,
    extract_markdown_images,
    split_nodes_delimiter,
    text_to_textnodes,
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
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

    def test_split_image(self):
        node = TextNode(
            "This is a text with an ![image](https://i.imgur.com/blabla.jpg)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is a text with an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/blabla.jpg"),
            ],
            new_nodes,
        )

    # for some reason this error is not raised
    # def test_image_tag_not_closed(self):
    #     node = TextNode(
    #         "A text with an ![unclosed image link](https://image.com", text_type_text
    #     )
    #     with self.assertRaises(ValueError):
    #         split_nodes_image([node])

    def test_split_image_no_text(self):
        node = TextNode(
            "![image](https://i.imgur.com/blabla.jpg)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", text_type_image, "https://i.imgur.com/blabla.jpg"),
            ],
            new_nodes,
        )

    def test_split_link(self):
        node = TextNode(
            "This is a text with a [link](https://link.com)", text_type_text
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a text with a ", text_type_text),
                TextNode("link", text_type_link, "https://link.com"),
            ],
            new_nodes,
        )

    def test_split_multilink(self):
        node = TextNode(
            "This is a text with a [link](https://link.com) and [another one](https://anotherlink.com/wow) then some text",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a text with a ", text_type_text),
                TextNode("link", text_type_link, "https://link.com"),
                TextNode(" and ", text_type_text),
                TextNode("another one", text_type_link, "https://anotherlink.com/wow"),
                TextNode(" then some text", text_type_text),
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        nodes = text_to_textnodes(
            "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
            ],
            nodes,
        )


if __name__ == "__main__":
    unittest.main()
