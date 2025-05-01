import re

from inline_markdown import(
    text_to_node
)
from textnode import(
    TextNode,
    TextType,
    text_node_to_html_node
)
from htmlnode import(
    ParentNode
)

from block_markdown import(
    BlockType,
    markdown_to_blocks,
    block_to_block
)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_children = []
    for block in blocks:
        match block_to_block(block):
            case BlockType.PARAGRAPH:
                parent = get_html_paragraph(block)
                html_children.append(parent)
            case BlockType.HEADING:
                parent = get_html_heading(block)
                html_children.append(parent)
            case BlockType.QUOTE:
                parent = get_html_quote(block)
                html_children.append(parent)
            case BlockType.CODE:
                parent = get_html_code(block)
                html_children.append(parent)
            case BlockType.UNORDERED:
                parent = get_html_unordered_li(block)
                html_children.append(parent)
            case BlockType.ORDERED:
                parent = get_html_ordered_li(block)
                html_children.append(parent)
    return ParentNode("div", html_children)

def text_to_children(block, type=None):
    html = []
    if type == BlockType.CODE:
        nodes = [TextNode(block, TextType.TEXT)]
    else:
        nodes = text_to_node(block)
    for node in nodes:
        html.append(text_node_to_html_node(node))
    return html

def get_html_paragraph(block):
    block = " ".join(block.split("\n"))
    children = text_to_children(block)
    return  ParentNode("p",children)

def get_html_heading(block):
    block = block.split()
    header = len(block[0])
    text = " ".join(block[1:])
    children = text_to_children(text)
    return ParentNode(f"h{header}",children)

def get_html_quote(block):
    children = text_to_children(block[2:])
    return ParentNode("blockquote",children)

def get_html_code(block):
    block = block.split("\n")
    block = "\n".join(block[1:-1]) + "\n"
    children = text_to_children(block, BlockType.CODE)
    parent = [ParentNode("code", children)]
    return ParentNode("pre", parent)

def get_html_ordered_li(block):
    children_li = get_li(block, BlockType.ORDERED)
    return ParentNode("ol", children_li)

def get_html_unordered_li(block):
    children_li = get_li(block, BlockType.UNORDERED)
    return ParentNode("ul", children_li)

def get_li(block,type):
    children_li = []
    items = block.split("\n")
    for item in items:
        if type == BlockType.ORDERED:
            num = re.findall(r"^\d+. ", item)
            num = len(num[0])
            li = ParentNode("li", text_to_children(item[num:]))
        else:
            li = ParentNode("li", text_to_children(item[2:]))
        children_li.append(li)
    return children_li
