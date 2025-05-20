import unittest
from src.textnode import TextNode, TextType
from src.utility_funcs import split_nodes_link  

class TestSplitNodesLink(unittest.TestCase):
    def test_split_links_basic(self):
        node = TextNode(
            "Link to [Google](https://google.com)",
            TextType.TEXT,
        )
        result = split_nodes_link([node])
        self.assertListEqual(
            result,
            [
                TextNode("Link to ", TextType.TEXT),
                TextNode("Google", TextType.LINK, "https://google.com"),
            ],
        )

    def test_multiple_links(self):
        node = TextNode(
            "Visit [A](urlA) or [B](urlB)",
            TextType.TEXT,
        )
        result = split_nodes_link([node])
        self.assertEqual(len(result), 4)
        self.assertEqual(result[1].text_type, TextType.LINK)
        self.assertEqual(result[3].url, "urlB")

    def test_non_text_node_untouched(self):
        nodes = [
            TextNode("hello", TextType.BOLD),
            TextNode("[alt](link)", TextType.TEXT)
        ]
        result = split_nodes_link(nodes)
        self.assertEqual(result[0].text_type, TextType.BOLD)
        self.assertEqual(result[1].text_type, TextType.LINK)
