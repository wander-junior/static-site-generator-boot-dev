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
