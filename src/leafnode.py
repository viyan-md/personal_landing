from src.htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str, props: dict | None = None):
        super().__init__(tag = tag, value = value, children = None, props = props)

    def to_html(self):
        if not self.value:
            raise ValueError("leaf node must have a value")

        if not self.tag: 
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"