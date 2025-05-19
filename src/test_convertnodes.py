import unittest
from convertnodes import ConvertNodes
from textnode import TextNode, TextType
from leafnode import LeafNode

class TestConvertNodes(unittest.TestCase):
    def test_text_conversion(self):
        node = TextNode("plain text", TextType.TEXT)
        result = ConvertNodes.from_txt_to_html(node)
        self.assertIsInstance(result, LeafNode)
        self.assertIsNone(result.tag)
        self.assertEqual(result.value, "plain text")
        self.assertIsNone(result.props)

    def test_bold_conversion(self):
        node = TextNode("bold", TextType.BOLD)
        result = ConvertNodes.from_txt_to_html(node)
        self.assertEqual(result.tag, "b")
        self.assertEqual(result.value, "bold")

    def test_italic_conversion(self):
        node = TextNode("italic", TextType.ITALIC)
        result = ConvertNodes.from_txt_to_html(node)
        self.assertEqual(result.tag, "i")
        self.assertEqual(result.value, "italic")

    def test_code_conversion(self):
        node = TextNode("code", TextType.CODE)
        result = ConvertNodes.from_txt_to_html(node)
        self.assertEqual(result.tag, "code")
        self.assertEqual(result.value, "code")

    def test_link_conversion(self):
        node = TextNode("link text", TextType.LINK, url="https://example.com")
        result = ConvertNodes.from_txt_to_html(node)
        self.assertEqual(result.tag, "a")
        self.assertEqual(result.value, "link text")
        self.assertEqual(result.props, {"href": "https://example.com"})

    def test_image_conversion(self):
        node = TextNode("alt text", TextType.IMAGE, url="https://img.com/image.png")
        result = ConvertNodes.from_txt_to_html(node)
        self.assertEqual(result.tag, "img")
        self.assertEqual(result.value, "")
        self.assertEqual(result.props, {"src": "https://img.com/image.png", "alt": "alt text"})



if __name__ == "__main__":
    unittest.main()