

from htmlnode import HTMLNode
from inline_markdown import text_to_textnodes
from leaf_node import LeafNode
from parent_node import ParentNode
from markdown_blocks import BlockType, block_to_block_type, markdown_to_blocks
from textnode import TextNode, TextType, text_node_to_html_node


def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    blocks_node = []
    
    for block in blocks:
        block_node: HTMLNode = block_to_html_node(block)
        blocks_node.append(block_node)
       
    return ParentNode('div', blocks_node)
        
        
def block_to_html_node(block: str) -> ParentNode:
    block_type = block_to_block_type(block)
    
    match block_type:
        case BlockType.PARAGRAPH:
            return paragraph_to_html_node(block)
        case BlockType.HEADING:
            return heading_to_html_node(block)
        case BlockType.CODE:
            return clean_code_block(block)
        case BlockType.QUOTE:
            return quote_to_html_node(block)
        case BlockType.UNORDERED_LIST:
            return unoredered_list_to_html_node(block)
        case BlockType.ORDERED_LIST:
            return ordered_list_to_html_node(block)
        
def text_to_children(text: str) -> list[LeafNode]:
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    
    return children

def paragraph_to_html_node(block: str) -> ParentNode:
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block: str) -> ParentNode:
    heading_level = block.count("#")
    if heading_level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {heading_level}")
    
    tag = f"h{heading_level}"
    text = block[heading_level + 1 :]
    children = text_to_children(text)
    
    return ParentNode(tag, children)

def clean_code_block(block: str) -> str:
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    
    s = block.split('\n')
    text = '\n'.join(s[1:-1]) + '\n'
    text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(text_node)
    code_block = ParentNode("code", [child])
    
    return ParentNode("pre", [code_block])

def quote_to_html_node(block: str) -> ParentNode:
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    
    return ParentNode("blockquote", children)

def unoredered_list_to_html_node(block: str) -> ParentNode:
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
        
    return ParentNode("ul", html_items)

def ordered_list_to_html_node(block: str) -> ParentNode:
    items = block.split("\n")
    html_items = []
    for item in items:
        parts = item.split(". ", 1)
        text = parts[1]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
        
    return ParentNode("ol", html_items)
