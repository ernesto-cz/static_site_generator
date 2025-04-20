import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.test.com")
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node",TextType.LINK, "http://www.test.com")
        node2 = TextNode("This is a text node",TextType.LINK, "http://www.test.com")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("Test", TextType.LINK, "http://www.test.com")
        self.assertEqual(
            "TextNode(Test, link, http://www.test.com)", repr(node)
        )

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_invalid_text_type(self):
        node = TextNode("This is a text node", "tonto")
        with self.assertRaises(ValueError) as cm:
            text_node_to_html_node(node)
        self.assertEqual(
            str(cm.exception),
            f"Invalid text type: {node.text_type}"
        )

        def test_text_leaf_repr(self):
            props = {
                "src": "httpe://www.google.com",
                "alt": "This is a text node"
            }
            node = TextNode(props["alt"], TextType.IMAGE, props["src"])
            html_node = text_node_to_html_node(node)
            self.assertEqual(
                repr(html_node),
                (
                    'LeafNode(img, This is a text node, '
                    '{"src": "httpe://www.google.com"})'
                )
            )

if __name__ == "__main__":
    unittest.main()
