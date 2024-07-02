class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError(
            "method should be implemented by child classes"
        )

    def props_to_html(self):
        props_str = str()
        for attribute, value in self.props.items():
            props_str = f'{props_str} {attribute}="{value}"'
        return props_str

    def __repr__(self):
        return (
            f"HTMLNode:\n"
            f"tag     : {self.tag}\n"
            f"value   : {self.value}\n"
            f"children: {self.children}\n"
            f"props   : {self.props}"
        )


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: LeafNode must have a value")

        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
