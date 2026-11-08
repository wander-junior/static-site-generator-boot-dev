import unittest

from htmlnode import HTLMNode, LeafNode, ParentNode

class TestHTLMNode(unittest.TestCase):
    # HTMLNode

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

    # LeafNode

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_img(self):
        node = LeafNode("img", "", {"src": "cat.png", "alt": "A cat"})
        self.assertEqual(node.to_html(), '<img src="cat.png" alt="A cat" />')

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Website", {"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Website</a>')

    def test_leaf_to_html_none_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    # ParentNode

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode("span", "child1")
        child_node2 = LeafNode("span", "child2")

        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child1</span><span>child2</span></div>",
        )
        
    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


if __name__ == "__main__":
    unittest.main()
