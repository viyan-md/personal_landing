import unittest
from src.nodes.text.textnode import TextNode, TextType
from src.utils.markdown_parser import split_nodes_image 

class TestSplitNodesImage(unittest.TestCase):
    def test_split_images_basic(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
        )

    def test_multiple_images(self):
        node = TextNode(
            "Here ![one](url1) and ![two](url2)",
            TextType.TEXT,
        )
        result = split_nodes_image([node])
        self.assertEqual(len(result), 4)
        self.assertEqual(result[1].text, "one")
        self.assertEqual(result[1].text_type, TextType.IMAGE)
        self.assertEqual(result[3].text, "two")
        self.assertEqual(result[3].url, "url2")

    def test_image_with_other_node(self):
        nodes = [
            TextNode("![alt](url)", TextType.TEXT),
            TextNode("unchanged", TextType.BOLD)
        ]
        result = split_nodes_image(nodes)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].text_type, TextType.IMAGE)
        self.assertEqual(result[1].text_type, TextType.BOLD)

