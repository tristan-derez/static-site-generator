import unittest
from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq_different_text(self):
        node = TextNode("This is a text node", "bold")
        node_diff_text = TextNode("Different text", "bold")
        self.assertNotEqual(node, node_diff_text)

    def test_not_eq_different_text_type(self):
        node = TextNode("This is a text node", "bold")
        node_diff_type = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node_diff_type)

    def test_not_eq_none_url(self):
        node_with_url = TextNode(
            "This is a text node", "bold", url="https://example.com"
        )
        node_without_url = TextNode("This is a text node", "bold")
        self.assertNotEqual(node_with_url, node_without_url)

    def test_eq_same_url(self):
        node_with_url1 = TextNode(
            "This is a text node", "bold", url="https://example.com"
        )
        node_with_url2 = TextNode(
            "This is a text node", "bold", url="https://example.com"
        )
        self.assertEqual(node_with_url1, node_with_url2)

    def test_str_representation(self):
        node = TextNode("This is a text node", "bold", url="https://example.com")
        expected_str = "TextNode('This is a text node', 'bold', 'https://example.com')"
        self.assertEqual(str(node), expected_str)


if __name__ == "__main__":
    unittest.main()
