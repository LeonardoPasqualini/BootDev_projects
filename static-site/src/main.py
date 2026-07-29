import pathlib
from generate_page import generate_pages_recursive
from textnode import TextType, TextNode
from copy_files import move_static_to_public
def main():
    # text_node: TextNode = TextNode("this is an anchor text", TextType.LINK, "https://www.boot.dev")
    content_path = pathlib.Path("./content")
    template_path = pathlib.Path("./template.html")
    public_path = pathlib.Path("./public")
    
    # content_path = "./content"
    # template_path = "./template.html"
    # public_path = "./public"
        
    # content_md_path = "./content/index.md"
    # template_path = "./template.html"
    # public_path = "./public/index.html"
    
    # print(text_node)
    move_static_to_public()
    
    generate_pages_recursive(content_path, template_path, public_path)
main()