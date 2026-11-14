import re

from enum import Enum

from htmlnode import ParentNode, HTLMNode, LeafNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, text_node_to_html_node, TextType

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown: str) -> list[str]:
    raw_blocks = markdown.split('\n\n')
    blocks = []

    for block in raw_blocks:
        stripped_block = block.strip()
        if stripped_block != "":
            blocks.append(stripped_block)

    return blocks

def block_to_block_type(block: str) -> BlockType:
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    
    lines = block.split("\n")

    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    
    if all(line.startswith(f"{index + 1}. ") for index, line in enumerate(lines)):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown: str) -> ParentNode:
    splited_blocks = markdown_to_blocks(markdown)

    md_children_nodes = []

    for block in splited_blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.QUOTE:
            cleaned_quote = " ".join(line[2:] for line in block.splitlines())
            html_nodes = text_to_html_nodes(cleaned_quote)
            new_node = ParentNode("blockquote", html_nodes)

        elif block_type == BlockType.UNORDERED_LIST:
            children_items = []

            for line in block.splitlines():
                html_nodes = text_to_html_nodes(line[2:])
                children_items.append(ParentNode("li", html_nodes))

            new_node = ParentNode("ul", children_items)

        elif block_type == BlockType.ORDERED_LIST:
            children_items = []

            for line in block.splitlines():
                html_nodes = text_to_html_nodes(line[3:])
                children_items.append(ParentNode("li", html_nodes))

            new_node = ParentNode("ol", children_items)
            
        elif block_type == BlockType.CODE:
            text_node = TextNode(block[3:-3].removeprefix("\n"), TextType.CODE)
            code_leaf = text_node_to_html_node(text_node)
            new_node = ParentNode("pre", [code_leaf])

        elif block_type == BlockType.HEADING:
            count = len(block) - len(block.lstrip("#"))
            cleaned_text = block[count + 1:]
            html_nodes = text_to_html_nodes(cleaned_text)

            new_node = ParentNode(f"h{count}", html_nodes)
            
        elif block_type == BlockType.PARAGRAPH:
            html_nodes = text_to_html_nodes(block.replace("\n", " "))
            new_node = ParentNode("p", html_nodes)
    
        md_children_nodes.append(new_node)

    return ParentNode("div", md_children_nodes)

def text_to_html_nodes(text: str) -> list[LeafNode]:
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]