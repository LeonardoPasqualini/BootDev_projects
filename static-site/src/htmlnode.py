class HTMLNode:
    def __init__(self,
                 tag: str | None = None,
                 value: str | None = None,
                 children: list | None = None, 
                 props: dict | None = None):
        """_summary_
        Args:
            tag (str | None, optional): the HTML tag. Defaults to None.
            value (str | None, optional): the HTML value. Defaults to None.
            children (list | None, optional): A list of childrens. Defaults to None.
            props (dict | None, optional): A dictionary of properties. Defaults to None.
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        if self.props is None or self.props == {}:
            return ""
        props_html = ""
        for key, value in self.props.items():
            props_html += f' {key}="{value}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"