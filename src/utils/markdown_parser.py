import re
from enums.types import BlockType
from nodes.html.leafnode import LeafNode
from nodes.text.textnode import TextNode, TextType
from code.block_type_helpers import get_block_type, block_patterns

def from_txt_to_html(text_node: "TextNode"):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("text type not supported")

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
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    return nodes

def markdown_to_blocks(markdown: str):
    return [block.strip() for block in markdown.split("\n\n") if block.strip()]

def block_to_block_type(block):
    return get_block_type(block)

def get_heading_level(block):
    match = re.match(r"^(#{1,6})\s+", block)
    if not match:
        raise ValueError("Invalid heading format")
    return len(match.group(1))

def block_type_tag(block, type):
    match type:
        case BlockType.PARAGRAPH:
            return "p"
        case BlockType.HEADING:
            return get_heading_level(block)
        case BlockType.QUOTE:
            return "blockquote"
        case BlockType.CODE:
            return "pre"
        case BlockType.ORDERED_LIST:
            return "ol"
        case BlockType.UNORDERED_LIST:
            return "ul"

def strip_code_block(block: str) -> str:
    lines = block.strip().splitlines()

    if lines and lines[0].strip() == "```":
        lines = lines[1:]
    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]

    return "\n".join(lines)

def strip_block_syntax(block: str, block_type: str) -> str:
    if block_type == "code":
        return strip_code_block(block)
    elif block_type == "heading":
        return re.sub(r"^#{1,6}\s+", "", block.strip())
    elif block_type == "ordered_list":
        return "\n".join(re.sub(r"^\d+\.\s+", "", line) for line in block.strip().splitlines())
    elif block_type == "unordered_list":
        return "\n".join(re.sub(r"^- \s*", "", line) for line in block.strip().splitlines())
    elif block_type == "quote":
        return "\n".join(re.sub(r"^>\s+", "", line) for line in block.strip().splitlines())
    elif block_type == "paragraph":
        return block.strip()
    else:
        return block

def text_to_children(text: str):
    html_nodes = []
    for line in text.splitlines():
        text_nodes = text_to_textnodes(line)
        for text_node in text_nodes:
            html_nodes.append(from_txt_to_html(text_node))
    return html_nodes

    








