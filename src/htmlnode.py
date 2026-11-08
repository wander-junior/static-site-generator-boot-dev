class HTLMNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None or self.props == {}:
            return ""

        return_string = ""

        for key, value in self.props.items():
            return_string += f' {key}="{value}"'

        return return_string

    def __repr__(self):
        children_string = ""

        if self.children is not None:
            children_string += "\n"
            for child in self.children:
                children_string += f"\t{repr(child)}"
        else:
            children_string += "None"

        return f"Tag = {self.tag}\nValue = {self.value}\nChildren = {children_string}\nProps = {self.props_to_html()}"

class LeafNode(HTLMNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")

        if self.tag is None or self.tag == "":
            return self.value

        if self.tag == "img":
            return f"<{self.tag}{self.props_to_html()} />"

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"Tag = {self.tag}\nValue = {self.value}\nProps = {self.props_to_html()}"

class ParentNode(HTLMNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None or self.tag == "":
            raise ValueError("All parent nodes must have a tag")

        if self.children is None or len(self.children) == 0:
            raise ValueError("All parent nodes must have a children")

        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"