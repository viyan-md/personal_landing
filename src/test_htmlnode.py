import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode(
            tag="div",
            value="Hello, World!",
            children=[HTMLNode(tag="p", value="Child paragraph")],
            props={"class": "container", "id": "main"}
        )
        
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello, World!")
        self.assertIsInstance(node.children, list)
        self.assertEqual(node.children[0].tag, "p")
        self.assertEqual(node.children[0].value, "Child paragraph")
        self.assertEqual(node.props, {"class": "container", "id": "main"})
        
        node_minimal = HTMLNode(tag="div", value="Hello")
        self.assertEqual(node_minimal.tag, "div")
        self.assertEqual(node_minimal.value, "Hello")
        self.assertIsNone(node_minimal.children)
        self.assertIsNone(node_minimal.props)

    def test_eq(self):
        node = HTMLNode(
            tag="h1",
            value="Big Header",
            props={"class": "main_header"}
        )
        node2 = HTMLNode(
            tag="h1",
            value="Big Header",
            props={"class": "main_header"}
        )
        self.assertEqual(node, node2)
        self.assertEqual(node.children, node2.children)

    def test_eq_false(self):
        node = HTMLNode(
            tag="h2",
            value="Small Header",
            props={"class": "main_header"}
        )
        node2 = HTMLNode(
            tag="h1",
            value="Big Header",
            props={"class": "small_header"}
        )

        self.assertNotEqual(node, node2)
        self.assertNotEqual(node.tag, node2.tag)
        self.assertNotEqual(node.props, node2.props)

    def test_eq_false2(self):
        node = HTMLNode(
            tag="a",
            value="read here",
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        node2 = HTMLNode()
    
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node.tag, node2.tag)
        self.assertNotEqual(node.props, node2.props)

    def test_props_to_html(self):
        node = HTMLNode(
            tag="p",
            value="read here",
            props={"text-align": "left"}
        )
        node2 = HTMLNode()

        self.assertEqual(node.props_to_html(), ' text-align="left"')
        self.assertEqual(node2.props_to_html(), "")

    def test_eq_repr(self):
        node = HTMLNode(
            tag="a",
            value="read here",
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        node2 = HTMLNode()

        self.assertEqual(node.__repr__(), "Tag: a\nValue: read here\nChildren: None\nProps: {'href': 'https://www.google.com', 'target': '_blank'}")
        self.assertEqual(node2.__repr__(), "Tag: None\nValue: None\nChildren: None\nProps: None")
    


if __name__ == "__main__":
    unittest.main()