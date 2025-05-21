import os
from core.markdown_to_html_parser import markdown_to_html

def extract_title(markdown:str):
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    
    raise Exception("No h1 header found")

def write_to_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def generate_page(basepath, from_path, dest_path, template_path="template.html"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, "r") as file:
        markdown = file.read()
    with open(template_path, "r") as file:
        template = file.read()

    title = extract_title(markdown)
    html_string = markdown_to_html(markdown).to_html()

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_string)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')


    write_to_file(dest_path, template)

def md_to_html(name):
    pre, _ = os.path.splitext(name)
    return pre + ".html"

def generate_pages_recursively(basepath, source, destination, template_path="template.html"):
    with os.scandir(source) as d:
        for e in d:
            new_source = os.path.join(source, e.name)
            new_destination = os.path.join(destination, e.name)
    
            if e.is_dir():
                generate_pages_recursively(basepath, new_source, new_destination)
            else:
                generate_page(basepath=basepath, from_path=new_source, dest_path=md_to_html(new_destination))


    