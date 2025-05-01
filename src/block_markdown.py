from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quoute"
    UNORDERED = "unordered_list"
    ORDERED = "ordered_list"


def block_to_block(block):
    match block:
        case _ if (match := re.findall("(^|\n)- ", block)):
            return unorder_list_block(match, block)
        case _ if (match := re.findall("^#+ ", block)):
            return heading_block(match, block)
        case _ if (match := re.findall("(^|\n)`{3}", block)):
            return code_block(match, block)
        case _ if (match := re.findall("^>", block)):
            return quote_block(match, block)
        case _ if (match := re.findall(r"(^|\n)\d+. ", block)):
            return order_list_block(match, block)
        case _:
            return BlockType.PARAGRAPH

def unorder_list_block(match, block):
    block = block.split("\n")
    for i, line in enumerate(block, 1):
        if line[0] != "-":
            raise ValueError(f'Invalid syntax: Unordered list - missing "- " at begingin of line {i}')
    return BlockType.UNORDERED

def order_list_block(match, block):
    block = block.split("\n")
    for i, line in enumerate(block, 1):
        item_number = int(re.findall(r"\d+", line)[0])
        if int(item_number) != i:
            raise ValueError(f'Invalid syntax: Order list line number mistmach - current line is {item_number}, but expected {i}.')
    return BlockType.ORDERED

def heading_block(match, block):
    if len(match[0]) > 7:
        raise ValueError('Invalid synstax: Heading level must be between 1 and 6 (e.g., "#" to "######")')
    return BlockType.HEADING

def code_block(match, block):
    if len(match) % 2 != 0 :
        return BlockType.PARAGRAPH
    block = block.split("\n")
    for line in block:
        if line[0:3] == "```" and len(line) > 3:
            raise ValueError("Invalid syntax: Code level to open or close most be 3 (e.g., ```)")
    return BlockType.CODE

def quote_block(match, block):
    if block[1] == ">":
        raise ValueError("Invalid syntax: Code level to open or close most be 1 (e.g., >)")
    return BlockType.QUOTE

def markdown_to_blocks(markdown):
    split_space = markdown.split("\n")
    new_block = []
    paragraph = ""
    for line in split_space:
        #new_line = line.strip()
        if line == "":
            if paragraph != "":
                new_block.append(paragraph)
                paragraph = ""
        else:
            if paragraph == "":
                paragraph += line
            else:
                paragraph += "\n" + line
    return new_block
