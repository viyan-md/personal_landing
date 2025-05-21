from src.utils.markdown_parser import markdown_to_blocks, block_to_block_type

def markdown_to_html(markdown):
    md_blocks = markdown_to_blocks(markdown)

    for block in md_blocks:
        block_type = block_to_block_type(block)