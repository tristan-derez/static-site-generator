import unittest
from htmlnode import HTMLNode, LEAFNode, ParentNode


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

    def test_parentnode_with_children(self):
        tag = "div"
        props = {'class': 'main'}
        node = ParentNode(tag, [LEAFNode("p", "hey!"), LEAFNode("b", "wow"), LEAFNode("a", 'link', {"href": "https://example.com"})], props)
        self.assertEqual(node.to_html(), f'<div class="main"><p>hey!</p><b>wow</b><a href="https://example.com">link</a></div>')

    def test_to_html_with_children(self):
        child_node = LEAFNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LEAFNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LEAFNode("b", "Bold text"),
                LEAFNode(None, "Normal text"),
                LEAFNode("i", "italic text"),
                LEAFNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LEAFNode("b", "Bold text"),
                LEAFNode(None, "Normal text"),
                LEAFNode("i", "italic text"),
                LEAFNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


if __name__ == "__main__":
    unittest.main()