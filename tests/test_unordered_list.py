import unittest
from src.code.block_type_helpers import is_valid_unordered_list 

class TestIsValidUnorderedList(unittest.TestCase):
    def test_valid_unordered_list(self):
        block = "- Item one\n- Item two\n- Item three"
        self.assertTrue(is_valid_unordered_list(block))

    def test_invalid_missing_dash(self):
        block = "- Item one\nItem two\n- Item three"
        self.assertFalse(is_valid_unordered_list(block))

    def test_invalid_missing_space(self):
        block = "-Item one\n- Item two"
        self.assertFalse(is_valid_unordered_list(block))

    def test_empty_block(self):
        block = ""
        self.assertTrue(is_valid_unordered_list(block))  

    def test_whitespace_lines(self):
        block = "- Item one\n\n- Item two\n  \n- Item three"
        self.assertTrue(is_valid_unordered_list(block))

    def test_lines_with_only_spaces(self):
        block = "   \n- Item one\n - Item two\n- Item three"
        self.assertFalse(is_valid_unordered_list(block))
