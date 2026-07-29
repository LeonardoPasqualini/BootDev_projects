import unittest

from src.generate_page import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# This is header"
        self.assertEqual(extract_title(markdown), "This is header")
        
        markdown = """
Some text before header

# This is header

some text after header
"""
        
        self.assertEqual(extract_title(markdown), "This is header")