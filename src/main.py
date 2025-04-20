#from textnode import TextNode, TextType
from htmlnode import ParentNode, LeafNode

def main():
    props = {
        "name": "subject",
        "type": "submit",
        "value": "HTML",
        "formaction": "/action_page2.php"
    }

    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("button", "HTML", props),
            LeafNode(None, "Normal text"),
        ],
    )
    node.to_html()


if __name__ == "__main__":
    main()
