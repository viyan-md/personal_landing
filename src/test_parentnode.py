import unittest

from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):

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

    def test_multiple_children(self):
        child1 = LeafNode("i", "italic")
        child2 = LeafNode(None, "plain text")
        child3 = LeafNode("b", "bold")
        parent = ParentNode("p", [child1, child2, child3])
        self.assertEqual(
            parent.to_html(),
            "<p><i>italic</i>plain text<b>bold</b></p>"
        )

    def test_nested_parent_nodes(self):
        inner = ParentNode("span", [LeafNode("em", "nested")])
        outer = ParentNode("section", [inner])
        self.assertEqual(
            outer.to_html(),
            "<section><span><em>nested</em></span></section>"
        )

    def test_props_rendering(self):
        child = LeafNode("b", "bold")
        parent = ParentNode("div", [child], props={"class": "highlight", "id": "main"})
        self.assertEqual(
            parent.to_html(),
            '<div class="highlight" id="main"><b>bold</b></div>'
        )

    def test_missing_tag_raises(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("b", "error")]).to_html()

    def test_missing_children_raises(self):
        with self.assertRaises(ValueError):
            ParentNode("div", []).to_html()

    def test_deeply_nested(self):
        node = ParentNode(
            "div",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                ParentNode("span", [
                    LeafNode("i", "italic text"),
                    LeafNode(None, "after italic")
                ])
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<div><b>Bold text</b>Normal text<span><i>italic text</i>after italic</span></div>"
        )


if __name__ == "__main__":
    unittest.main()