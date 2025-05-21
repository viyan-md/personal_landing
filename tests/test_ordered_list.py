import unittest
from src.code.block_type_helpers import is_valid_ordered_list  

class TestIsValidOrderedList(unittest.TestCase):
    def test_valid_ordered_list(self):
        block = "1. First item\n2. Second item\n3. Third item"
        self.assertTrue(is_valid_ordered_list(block))

    def test_invalid_order_numbering(self):
        block = "1. First item\n3. Second item\n4. Third item"
        self.assertFalse(is_valid_ordered_list(block))

    def test_invalid_format_missing_dot(self):
        block = "1 First item\n2. Second item\n3. Third item"
        self.assertFalse(is_valid_ordered_list(block))

    def test_empty_block(self):
        block = ""
        self.assertTrue(is_valid_ordered_list(block))

    def test_non_numeric_index(self):
        block = "one. First item\n2. Second item"
        self.assertFalse(is_valid_ordered_list(block))

    def test_extra_spaces(self):
        block = "1.   First item\n2. Second item\n3.  Third item"
        self.assertTrue(is_valid_ordered_list(block))

    def test_trailing_whitespace(self):
        block = "1. First item \n2. Second item\n3. Third item"
        self.assertTrue(is_valid_ordered_list(block))

