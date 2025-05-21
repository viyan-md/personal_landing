import sys
from utils.static_to_public import copy_static_to_public
from utils.html_generator import generate_pages_recursively

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    copy_static_to_public()

    generate_pages_recursively(basepath=basepath, source="content", destination="docs")
    
main()