from nodes.html.leafnode import LeafNode
from nodes.html.parentnode import ParentNode
from utils.markdown_parser import markdown_to_blocks, block_to_block_type, strip_block_syntax, get_heading_level, text_to_children

def markdown_to_html(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        type = block_to_block_type(block)
        clean_text = strip_block_syntax(block, type)
        
        if type == "heading":
            level = get_heading_level(block)
            children.append(ParentNode(tag=f"h{level}", children=text_to_children(clean_text))) 
        elif type == "paragraph":
            children.append(ParentNode(tag="p", children=text_to_children(clean_text)))
        elif type == "quote":
            children.append(ParentNode(tag="blockquote", children=text_to_children(clean_text))) 
        elif type == "code":
            node = ParentNode(tag="pre", children=[LeafNode("code", value=clean_text)])
            children.append(node)
        elif type in ("unordered_list", "ordered_list"):
            tag = "ol" if type == "ordered_list" else "ul"
            list_lines = clean_text.splitlines()
            list_nodes = [ParentNode(tag="li", children=text_to_children(line)) for line in list_lines]
            children.append(ParentNode(tag=tag, children=list_nodes))
    
    return ParentNode("div", children=children)
        




