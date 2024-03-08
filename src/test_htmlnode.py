import unittest
from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()