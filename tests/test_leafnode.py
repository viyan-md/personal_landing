import unittest
from src.nodes.html.leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_init_no_children(self):
        leaf = LeafNode(tag="span", value="Hello", props={"class": "highlight"})
        self.assertEqual(leaf.tag, "span")
        self.assertEqual(leaf.value, "Hello")
        self.assertIsNone(leaf.children)  
        self.assertEqual(leaf.props, {"class": "highlight"})

    def test_to_html_with_tag_and_value(self):
        leaf = LeafNode(tag="b", value="Bold Text")
        expected_html = "<b>Bold Text</b>"
        self.assertEqual(leaf.to_html(), expected_html)

    def test_to_html_with_props(self):
        leaf = LeafNode(tag="a", value="Click here", props={"href": "https://example.com"})
        expected_html = '<a href="https://example.com">Click here</a>'
        self.assertEqual(leaf.to_html(), expected_html)

    def test_to_html_without_tag(self):
        leaf = LeafNode(tag=None, value="Just text")
        self.assertEqual(leaf.to_html(), "Just text")

    def test_to_html_raises_error_when_value_missing(self):
        leaf = LeafNode(tag="p", value="")
        with self.assertRaises(ValueError):
            leaf.to_html()

