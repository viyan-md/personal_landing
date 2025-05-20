import unittest
from textnode import TextNode, TextType
from utility_funcs import split_nodes_delimiter 

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_no_delimiter(self):
        node = TextNode("Just plain text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "Just plain text")
        self.assertEqual(result[0].text_type, TextType.TEXT)

    def test_simple_bold(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " text")
        self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_simple_italic(self):
        node = TextNode("This is _italic_ text", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[1].text_type, TextType.ITALIC)
        self.assertEqual(result[1].text, "italic")

    def test_code_delimiter(self):
        node = TextNode("Here is `code` example", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[1].text, "code")

    def test_multiple_same_delimiters(self):
        node = TextNode("Multiple **bold** and **bold2** here", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[3].text, "bold2")
        self.assertEqual(result[3].text_type, TextType.BOLD)

    def test_nodes_with_non_text_types_unchanged(self):
        nodes = [
            TextNode("normal text", TextType.TEXT),
            TextNode("already bold", TextType.BOLD),
            TextNode("more text", TextType.TEXT),
        ]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        # The bold node should remain unchanged
        self.assertTrue(any(n.text == "already bold" and n.text_type == TextType.BOLD for n in result))

    def test_empty_string(self):
        node = TextNode("", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "")
        self.assertEqual(result[0].text_type, TextType.TEXT)

    def test_delimiter_at_start_and_end(self):
        node = TextNode("**bold start** and **bold end**", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result[0].text, "")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "bold start")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[-2].text, "bold end")
        self.assertEqual(result[-2].text_type, TextType.BOLD)

    def test_multiple_nodes_input(self):
        nodes = [
            TextNode("Here is **bold**", TextType.TEXT),
            TextNode(" and here is _italic_", TextType.TEXT)
        ]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        # After splitting bold, result length should be 4
        self.assertEqual(len(result), 4)
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[1].text, "bold")
        # The italic delimiter is untouched here, so last node text still contains "_italic_"
        self.assertTrue("_italic_" in result[3].text)

    def test_chained_splitting(self):
        # Simulate splitting bold first, then italic on same text
        nodes = [TextNode("This is **bold** and _italic_ text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        result = split_nodes_delimiter(result, "_", TextType.ITALIC)

        # There should be nodes with TEXT, BOLD, ITALIC, and TEXT types in order
        types_in_order = [node.text_type for node in result]
        expected_types = [TextType.TEXT, TextType.BOLD, TextType.TEXT, TextType.ITALIC, TextType.TEXT]
        self.assertEqual(types_in_order, expected_types)

