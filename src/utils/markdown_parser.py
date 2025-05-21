import re
from src.nodes.text.textnode import TextNode, TextType
from src.code.block_type_helpers import get_block_type

def split_nodes_delimiter(old_nodes: list["TextNode"], delimiter: str, text_type: TextType):
    
    split_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            split_nodes.append(node)
            continue

        blocks = node.text.split(delimiter) #fix to skip empty strings

        def process_block(index, value):
            if index % 2 == 1: return TextNode(text=value, text_type=text_type)
            else: return TextNode(text=value, text_type=TextType.TEXT)

        split_nodes.extend(map(lambda t: process_block(*t), enumerate(blocks)))

    return split_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    split_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            split_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)

        if not images:
            split_nodes.append(node)
            continue

        for alt, url in images:
            delimiter = f"![{alt}]({url})"
            parts = text.split(delimiter, 1)
            before = parts[0]
            after = parts[1] if len(parts) > 1 else ""

            if before:
                split_nodes.append(TextNode(before, TextType.TEXT))

            split_nodes.append(TextNode(alt, TextType.IMAGE, url))

            text = after

        if text:
            split_nodes.append(TextNode(text, TextType.TEXT))

    return split_nodes

def split_nodes_link(old_nodes):
    split_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            split_nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)

        if not links:
            split_nodes.append(node)
            continue

        for label, url in links:
            delimiter = f"[{label}]({url})"
            parts = text.split(delimiter, 1)
            before = parts[0]
            after = parts[1] if len(parts) > 1 else ""

            if before:
                split_nodes.append(TextNode(before, TextType.TEXT))
            split_nodes.append(TextNode(label, TextType.LINK, url))

            text = after

        if text:
            split_nodes.append(TextNode(text, TextType.TEXT))

    return split_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    return nodes

def markdown_to_blocks(markdown: str):
    return [block.strip() for block in markdown.split("\n\n") if block.strip()]

def block_to_block_type(block):
    return get_block_type(block)

def get_header_tag(block):
    return f"h{len(block.split(" ", maxsplit=1))}"













