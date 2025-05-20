from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list["TextNode"], delimiter: str, text_type: TextType):
    split_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            split_nodes.append(node)
            continue

        blocks = node.text.split(delimiter)

        def process_block(index, value):
            if index % 2 == 1: return TextNode(text=value, text_type=text_type)
            else: return TextNode(text=value, text_type=TextType.TEXT)

        split_nodes.extend(map(lambda t: process_block(*t), enumerate(blocks)))

    return split_nodes
        