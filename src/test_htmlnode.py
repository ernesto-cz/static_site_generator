import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        props = {
        "href": "https://www.google.com",
        "target": "_blank",
        }
        node = HTMLNode("p","Test Text",None,props)
        self.assertEqual(
            f'HTMLNode(p, Test Text, children: None, {props})',
            repr(node)
        )

    def test_values(self):
        props = {
        "href": "https://www.google.com",
        "target": "_blank",
        }
        node = HTMLNode("div","Test Text",None,props)
        self.assertEqual(
            node.tag,
            "div"
        )
        self.assertEqual(
            node.value,
            "Test Text"
        )
        self.assertEqual(
            node.children,
            None
        )
        self.assertEqual(
            node.props,
            props
        )

    def test_props(self):
        props = {
        "href": "https://www.google.com",
        "target": "_blank",
        }
        node = HTMLNode("p","Test Text",None,props)
        self.assertEqual(
            ' href="https://www.google.com" target="_blank"',
            node.props_to_html()
        )

    def test_props2(self):
        node = HTMLNode("p","Test Text",None,None)
        self.assertEqual(
            '',
            node.props_to_html()
        )

    def test_props3(self):
        props =  {
        "href": "https://www.google.com",
        "id": "myHeader",
        "target": "_parent",
        "width": "500",
        "height": "600",
        "src": "img_psyduck.png"
        }
        node = HTMLNode("p","Test Text",None,props)
        self.assertEqual(
            ' href="https://www.google.com" id="myHeader" target="_parent" width="500" height="600" src="img_psyduck.png"',
            node.props_to_html()
        )

    def test_to_html(self):
        #cm for context manager
        node = HTMLNode("p","Test Text",None,None)
        with self.assertRaises(NotImplementedError) as cm:
            node.to_html()
        self.assertEqual(
            "🛠️ still working on it 🐍",
            str(cm.exception)
        )

class TestLeafNode(unittest.TestCase):
    def test_repr(self):
        props = {
        "href": "https://www.google.com",
        "target": "_blank",
        }
        node = LeafNode("p","Test Text",props)
        self.assertEqual(
            f'LeafNode(p, Test Text, {props})',
            repr(node)
        )

    def test_values(self):
        props = {
        "href": "https://www.google.com",
        "target": "_blank",
        }
        node = LeafNode("div","Test Text", props)
        self.assertEqual(
            node.tag,
            "div"
        )
        self.assertEqual(
            node.value,
            "Test Text"
        )
        self.assertEqual(
            node.children,
            None
        )
        self.assertEqual(
            node.props,
            props
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(
            node.to_html(),
            "<p>Hello, world!</p>"
        )

    def test_leaf_to_html_a(self):
        props = {
            "href": "https://www.google.com"
        }
        node = LeafNode("a", "Click me!", props)
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>'
        )

    def test_leaf_to_html_button(self):
        #Expected output
        #<button name="subject" type="submit" value="HTML" formaction="/action_page2.php">HTML</button>
        props = {
            "name": "subject",
            "type": "submit",
            "value": "HTML",
            "formaction": "/action_page2.php"
        }
        node = LeafNode("button", "HTML", props)
        self.assertEqual(
            node.to_html(),
            (
                '<button name="subject"'
                ' type="submit"'
                ' value="HTML"'
                ' formaction="/action_page2.php">'
                'HTML'
                '</button>'
            )
        )

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError) as cm:
            node.to_html()
        self.assertEqual(
            str(cm.exception),
            "All leaf nodes must have a value"
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

class TetsParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_seven_grandchildren(self):
        props = {
            "name": "subject",
            "type": "submit",
            "value": "HTML",
            "formaction": "/action_page2.php"
        }
        greategrandchild_node = LeafNode("button", "HTML", props)
        grandchild_nodes = [
            LeafNode("li", "Item 1"),
            LeafNode("li", "Item 2"),
            LeafNode("li", "Item 3"),
            ParentNode("li", [greategrandchild_node]),
            LeafNode("li", "Item 5"),
            LeafNode("li", "Item 6"),
            LeafNode("li", "Item 7")
        ]
        child_node = ParentNode("ul", grandchild_nodes)
        parent_node = ParentNode("section", [child_node])

        self.assertEqual(
            parent_node.to_html(),
            "<section><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li>"
            '<li><button name="subject" type="submit" value="HTML" formaction="/action_page2.php">HTML</button></li>'
            "<li>Item 5</li><li>Item 6</li><li>Item 7</li></ul></section>"
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ],
            )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ],
            )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )



if __name__ == "__main__":
    unittest.main()
