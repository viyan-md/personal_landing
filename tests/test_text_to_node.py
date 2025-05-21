import unittest
from src.nodes.text.textnode import TextNode, TextType
from src.utils.markdown_parser import text_to_textnodes

class TestTextToNode(unittest.TestCase):
    def test_text_to_textnodes_full(self):
        input_text = (
            "This is **text** with an *italic* word and a `code block` and "
            "an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and "
            "a [link](https://boot.dev)"
        )
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertListEqual(text_to_textnodes(input_text), expected)