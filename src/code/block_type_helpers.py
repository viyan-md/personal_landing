import re

def is_valid_ordered_list(block:str):
    if not block.strip():
        return True
    
    lines = block.strip().splitlines()
    ol_pattern = re.compile(r"^(\d+)\.\s+")

    for expected_index, line in enumerate(lines, start=1):
        m = ol_pattern.match(line)

        if not m:
            return False
        
        number = int(m.group(1))
        
        if number != expected_index:
            return False

    return True

def is_valid_unordered_list(block: str):
    lines = block.splitlines()
    ul_pattern = re.compile(r"^- \s*")
    return all(ul_pattern.match(line) for line in lines if line.strip() != "")

def get_block_type(block):
    code_pattern = re.compile(r"^```")
    heading_pattern = re.compile(r"^#{1,6}\s+")
    quote_pattern =re.compile(r"^>\s+")

    if code_pattern.match(block):
        return "code"
    if heading_pattern.match(block):
        return "heading"
    if quote_pattern.match(block):
        return "quote"
    if is_valid_ordered_list(block):
        return "ordered_list"
    if is_valid_unordered_list(block):
        return "unordered_list"
    return "paragraph"