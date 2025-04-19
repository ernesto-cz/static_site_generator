import unittest

from textnode import TextNode, TextType


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
        node2 = TextNode("This is a text node", TextType.NORMAL)
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


if __name__ == "__main__":
    unittest.main()
