import re
from textnode import TextType, TextNode

def text_to_node(text):
    node = [TextNode(text, TextType.TEXT)]
    bold = split_nodes_delimiter(node, "*", TextType.BOLD)
    italic = split_nodes_delimiter(bold, "_", TextType.ITALIC)
    code = split_nodes_delimiter(italic, "`", TextType.CODE)
    image = split_nodes_image(code)
    link = split_nodes_link(image)
    return link


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        devide_node = old_node.text.split(delimiter)
        if len(devide_node) % 2 != 1:
            raise ValueError("Invalid markdown syntax: Section not closed")
        new_split = []
        for i, text in enumerate(devide_node):
            if text == "":
                continue
            if i % 2 == 0:
                new_split.append(TextNode(text,TextType.TEXT))
            else:
                new_split.append(TextNode(text,text_type))
        new_nodes.extend(new_split)
    return new_nodes

def extract_markdown_images(text):
    #Tips regex r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    return matches

def extract_markdown_links(text):
    #Tips regex r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(r"\[(.*?)\]\((.*?)\)",text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        text = old_node.text
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            split_text = text.split(f"![{image[0]}]({image[1]})", 1)
            if len(split_text) != 2:
                raise ValueError("Invalid markdown syntax: Image section not closed")
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], TextType.TEXT,))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            text = split_text[1]
        if text != "":
            new_nodes.append(TextNode(text,TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)
        text = old_node.text
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            split_text = text.split(f"[{link[0]}]({link[1]})", 1)
            if len(split_text) != 2:
                raise ValueError("Invalid markdown syntax: Link section not closed")
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            text = split_text[1]
        if text != "":
            new_nodes.append(TextNode(text,TextType.TEXT))
    return new_nodes

'''
Lambda just for fun but not easy to read :s

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if text_type == old_node.text_type:
            new_nodes.append(old_node)
            continue
        devide_node = old_node.text.split(delimiter)
        if len(devide_node) % 2 != 1:
            raise ValueError("Invalid markdown syntax: Section not closed")
        new_nodes.extend(map(lambda text: convertion(text, text_type), enumerate(devide_node)))
    return list(filter(lambda x: x, new_nodes))

def convertion(text, text_type):
    print(text)
    if text[1] == "":
        return None
    if text[0] % 2 == 1:
        return TextNode(text[1],text_type)
    return TextNode(text[1],TextType.TEXT)
'''
