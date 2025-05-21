from utils.static_to_public import copy_static_to_public
from utils.html_generator import generate_pages_recursively

def main():
    copy_static_to_public()

    generate_pages_recursively("content", "public")
    
main()