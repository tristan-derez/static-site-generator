import unittest
from htmlnode import HTMLNode, LEAFNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://example.com"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://example.com"',
        )

    def test_props_to_html_without_props(self):
        node = HTMLNode("div", "Content", None, None)
        result = node.props_to_html()
        self.assertEqual(result, '')

    def test_leafnode_no_value(self):
        with self.assertRaises(ValueError):
            LEAFNode("p", value=None)

    def test_leafnode_no_props(self):
        value = "hey! i'm a text"
        node = LEAFNode("p", value)
        self.assertEqual(node.to_html(), f"<p>{value}</p>")

    def test_leafnode_no_tag(self):
        value = "hey! i'm a text"
        node = LEAFNode(None, value)
        self.assertEqual(node.to_html(), f"{value}")

    def test_leafnode_with_props(self):
        tag = "a"
        value = "hey! i'm a link"
        props = {'href': 'https://example.com', 'target': '_blank'}
        node = LEAFNode(tag, value, props)
        self.assertEqual(node.to_html(), f'<{tag} href="https://example.com" target="_blank">{value}</{tag}>')


if __name__ == "__main__":
    unittest.main()