from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, 
                 tag: str, 
                 children: list[HTMLNode], 
                 props: dict | None = None):
        super().__init__(tag, None, children, props)
        
    def to_html(self) -> str:
        if self.tag == None or self.tag == "":
            raise ValueError("ParentNode must have a non-empty tag")
        if not self.children:
            raise ValueError("ParentNode must have at least one child")
        string_html = f"<{self.tag}{self.props_to_html()}>"
        for chield in self.children:
            string_html += chield.to_html()
        string_html += f"</{self.tag}>"
        return string_html
        