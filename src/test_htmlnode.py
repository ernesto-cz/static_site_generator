import unittest

from htmlnode import HTMLNode

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
