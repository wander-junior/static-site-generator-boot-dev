import re

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    splited_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            splited_nodes.append(node)
        else:
            splited_text = node.text.split(delimiter)

            if (len(splited_text) % 2) == 0:
                raise ValueError(f"Matching closing delimiter {delimiter} not found on {node.text}")
            
            for index, text in enumerate(splited_text):
                if text != "":
                    if (index % 2) == 0:
                        splited_nodes.append(TextNode(text, TextType.TEXT))
                    
                    else:
                        splited_nodes.append(TextNode(text, text_type))

    return splited_nodes

def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    splited_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            splited_nodes.append(node)

        else:
            images = extract_markdown_images(node.text)

            node_text = node.text

            for image_alt, image_url in images:
                sections = node_text.split(f"![{image_alt}]({image_url})", 1)
                
                if sections[0] != "":
                    splited_nodes.append(TextNode(sections[0], TextType.TEXT))

                splited_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))

                node_text = sections[1]

    return splited_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    splited_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            splited_nodes.append(node)

        else:
            links = extract_markdown_links(node.text)

            node_text = node.text

            for link_alt, link_url in links:
                sections = node_text.split(f"[{link_alt}]({link_url})", 1)
                
                if sections[0] != "":
                    splited_nodes.append(TextNode(sections[0], TextType.TEXT))

                splited_nodes.append(TextNode(link_alt, TextType.LINK, link_url))

                node_text = sections[1]

    return splited_nodes