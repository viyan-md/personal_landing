from src.nodes.html.htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list["HTMLNode"], props: dict | None = None):
        super().__init__(tag = tag, value = None, children = children, props = props)

    def to_html(self):
        if not self.tag:
            raise ValueError("parent node must have a tag")
        elif not self.children:
            raise ValueError("parent node must have children")
        
        def generate_html_str(node_list):
            return "" if not node_list else node_list[0].to_html() + generate_html_str(node_list[1:])
        
        html_str = f"<{self.tag}{self.props_to_html()}>{generate_html_str(self.children)}</{self.tag}>"

        return html_str


