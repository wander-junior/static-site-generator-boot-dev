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