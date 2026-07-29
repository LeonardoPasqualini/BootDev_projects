import os

from markdown_blocks import markdown_to_blocks
from markdow_to_html import markdown_to_html_node


def extract_title(markdown: str) -> str:
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            return block.split("# ")[1].strip()
    raise Exception("No title found in markdown")

def read_file(path: str) -> str:
    with open(path, 'r') as file:
        return file.read()

def write_file(path: str, content: str) -> None:
    dir_path = os.path.dirname(path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    with open(path, 'w') as file:
        file.write(content)

def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    markdown = read_file(from_path)
    title = extract_title(markdown)
    md_html_node = markdown_to_html_node(markdown).to_html()
    
    template = read_file(template_path)
    template = template.replace('{{ Title }}', title)
    template = template.replace('{{ Content }}', md_html_node)
    
    write_file(dest_path, template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # content/blog/tom/index.md
    # public/blog/tom/index.html
    if os.path.isfile(dir_path_content):
        dest_dir_path = dest_dir_path.replace(".md", ".html")
        return generate_page(dir_path_content, template_path, dest_dir_path)
    
    list_dir = os.listdir(dir_path_content)
    
    for path in list_dir:
        new_dir_path = os.path.join(dir_path_content, path)
        new_dest_path = os.path.join(dest_dir_path, path)
        generate_pages_recursive(new_dir_path, template_path, new_dest_path)
        