import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_list = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue
        
        text_list = node.text.split(delimiter)
        
        if len(text_list) % 2 == 0:
            raise ValueError(f'The text "{node.text}" don\'t have the given delimiter or is missing a close delimiter')

        for i in range(len(text_list)):
            if i % 2 == 0:
                if text_list[i] != "":
                    new_list.append(TextNode(text_list[i], TextType.TEXT))
            else:
                new_list.append(TextNode(text_list[i], text_type))
    
    return new_list
                
def extract_markdown_images(text: str) -> list[tuple]:
    if not text:
        return []
    match_alt = re.findall(r"\!\[(.*?)\]", text)
    match_link = re.findall(r"\((.*?)\)", text)
    return list(zip(match_alt, match_link))

def extract_markdown_links(text: str) -> list[tuple]:
    if not text:
        return []
    match_alt = re.findall(r"(?<!!)\[(.*?)\]", text)
    match_link = re.findall(r"\((.*?)\)", text)
    return list(zip(match_alt, match_link))

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_list = []
    
    for node in old_nodes:
        
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_list.append(node)
            continue
        
        section = node.text
        for i in range(len(images)):
            alt, link = images[i]
            split_text = section.split(f"![{alt}]({link})", 1)
            
            if split_text[0] != "":
                new_list.append(TextNode(split_text[0], TextType.TEXT))
            
            new_list.append(TextNode(alt, TextType.IMAGE, link))
            
            if split_text[1] != "" and i == len(images) - 1:
                new_list.append(TextNode(split_text[1], TextType.TEXT))
                
            section = split_text[1]
            
    return new_list

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_list = []
    
    for node in old_nodes:
        
        links = extract_markdown_links(node.text)
        
        if len(links) == 0:
            new_list.append(node)
            continue
        
        section = node.text
        for i in range(len(links)):
            alt, link = links[i]
            split_text = section.split(f"[{alt}]({link})", 1)
            
            if split_text[0] != "":
                new_list.append(TextNode(split_text[0], TextType.TEXT))
            
            new_list.append(TextNode(alt, TextType.LINK, link))
            
            if split_text[1] != "" and i == len(links) - 1:
                new_list.append(TextNode(split_text[1], TextType.TEXT))
            section = split_text[1]
            
    return new_list


def text_to_textnodes(text: str) -> list[TextNode]:
    text_node = [TextNode(text, TextType.TEXT)]
    new_list = split_nodes_delimiter(text_node, "**", TextType.BOLD)
    new_list = split_nodes_delimiter(new_list, "`", TextType.CODE)
    new_list = split_nodes_delimiter(new_list, "_", TextType.ITALIC)
    new_list = split_nodes_image(new_list)
    new_list = split_nodes_link(new_list)
    return new_list