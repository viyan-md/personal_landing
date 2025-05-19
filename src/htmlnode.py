class HTMLNode:
    def __init__(
            self, 
            tag: str | None = None, 
            value: str | None = None, 
            children: list["HTMLNode"] | None = None, 
            props: dict[str, str] | None = None
        ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_prop = ""

        if self.props:
            for prop, value in self.props.items():
                html_prop += f' {prop}="{value}"'
        
        return html_prop

    def __eq__(self, target):
        if not isinstance(target, HTMLNode):
            raise NotImplementedError
        
        return (self.tag == target.tag
                and self.value == target.value
                and self.children == target.children
                and self.props == target.props)
    
    def __repr__(self):
        return f"Tag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps: {self.props}"
    





        
