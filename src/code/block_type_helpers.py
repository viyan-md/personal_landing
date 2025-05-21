import re

block_patterns = {
    "code": re.compile(r"^```"),
    "heading": re.compile(r"^#{1,6}\s+"),
    "ordered_list": re.compile(r"^(\d+)\.\s+"),
    "unordered_list": re.compile(r"^- \s*"),
    "quote": re.compile(r"^>\s+")
}

def is_valid_ordered_list(block:str):
    if not block.strip():
        return True
    
    lines = block.strip().splitlines()

    for expected_index, line in enumerate(lines, start=1):
        m = block_patterns["ordered_list"].match(line)

        if not m:
            return False
        
        number = int(m.group(1))
        
        if number != expected_index:
            return False

    return True

def is_valid_unordered_list(block: str):
    lines = block.splitlines()
    return all(block_patterns["unordered_list"].match(line) for line in lines if line.strip() != "")

def get_block_type(block):
    if block_patterns["code"].match(block):
        return "code"
    if block_patterns["heading"].match(block):
        return "heading"
    if block_patterns["quote"].match(block):
        return "quote"
    if is_valid_ordered_list(block):
        return "ordered_list"
    if is_valid_unordered_list(block):
        return "unordered_list"
    return "paragraph"