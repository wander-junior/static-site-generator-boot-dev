import unittest

from htmlnode import HTLMNode

class TestHTLMNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTLMNode()
        props_to_html = node.props_to_html()
        expected_response = ""

        self.assertEqual(props_to_html, expected_response)

    def test_props_to_html_filled(self):
        node = HTLMNode(props = {"href": "https://www.google.com"})
        props_to_html = node.props_to_html()
        expected_response = ' href="https://www.google.com"'

        self.assertEqual(props_to_html, expected_response)

    def test_props_to_html_filled2(self):
        node = HTLMNode(props = {"href": "https://www.google.com","target": "_blank"})
        props_to_html = node.props_to_html()
        expected_response = ' href="https://www.google.com" target="_blank"'

        self.assertEqual(props_to_html, expected_response)

    def test_repr_empty(self):
        node = HTLMNode()
        actual_repr = repr(node)
        expected_response = "Tag = None\nValue = None\nChildren = None\nProps = "

        self.assertEqual(actual_repr, expected_response)


    def test_repr_tag_and_value(self):
        node = HTLMNode("p", "Some paragraph")
        actual_repr = repr(node)
        expected_response = "Tag = p\nValue = Some paragraph\nChildren = None\nProps = "

        self.assertEqual(actual_repr, expected_response)


    def test_repr_props(self):
        node = HTLMNode(props = {"href": "https://www.google.com"})
        actual_repr = repr(node)
        expected_response = 'Tag = None\nValue = None\nChildren = None\nProps =  href="https://www.google.com"'

        self.assertEqual(actual_repr, expected_response)

    def test_repr_children(self):
        children_node = HTLMNode()
        node = HTLMNode(children = [children_node])
        actual_repr = repr(node)
        children_response = "Tag = None\nValue = None\nChildren = None\nProps = "
        expected_response = f"Tag = None\nValue = None\nChildren = \n\t{children_response}\nProps = "

        self.assertEqual(actual_repr, expected_response)