import unittest
from src.core.markdown_to_html_parser import markdown_to_html

class TestMarkdownToHtml(unittest.TestCase):

    def test_heading(self):
        md = "# Heading"
        node = markdown_to_html(md)
        self.assertEqual(node.to_html(), "<div><h1>Heading</h1></div>")

    def test_paragraph(self):
        md = "This is a simple paragraph."
        node = markdown_to_html(md)
        self.assertEqual(node.to_html(), "<div><p>This is a simple paragraph.</p></div>")

    def test_blockquote(self):
        md = "> This is a quote."
        node = markdown_to_html(md)
        self.assertEqual(node.to_html(), "<div><blockquote>This is a quote.</blockquote></div>")

    def test_code_block(self):
        md = "```\nCode stays _unchanged_ **here**\n```"
        node = markdown_to_html(md)
        self.assertEqual(
            node.to_html(),
            "<div><pre><code>Code stays _unchanged_ **here**</code></pre></div>"
        )

    def test_ordered_list(self):
        md = "1. First item\n2. Second item"
        node = markdown_to_html(md)
        self.assertEqual(
            node.to_html(),
            "<div><ol><li>First item</li><li>Second item</li></ol></div>"
        )

    def test_unordered_list(self):
        md = "- Apple\n- Banana"
        node = markdown_to_html(md)
        self.assertEqual(
            node.to_html(),
            "<div><ul><li>Apple</li><li>Banana</li></ul></div>"
        )

    def test_multiple_paragraphs(self):
        md = "First paragraph.\n\nSecond paragraph."
        node = markdown_to_html(md)
        self.assertEqual(
            node.to_html(),
            "<div><p>First paragraph.</p><p>Second paragraph.</p></div>"
        )

    def test_inline_formatting(self):
        md = "This has **bold**, _italic_, and `code`."
        node = markdown_to_html(md)
        self.assertEqual(
            node.to_html(),
            "<div><p>This has <b>bold</b>, <i>italic</i>, and <code>code</code>.</p></div>"
        )

    def test_mixed_blocks(self):
        md = """# Header

This is a **bold** paragraph.

- List item one
- List item two

> A quote
"""
        expected_html = (
            "<div>"
            "<h1>Header</h1>"
            "<p>This is a <b>bold</b> paragraph.</p>"
            "<ul><li>List item one</li><li>List item two</li></ul>"
            "<blockquote>A quote</blockquote>"
            "</div>"
        )
        node = markdown_to_html(md)
        self.assertEqual(node.to_html(), expected_html)

