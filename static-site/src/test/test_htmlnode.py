import unittest
from src.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_none_att(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)
        
        
    def test_porps_to_html_eq(self):
        node = HTMLNode(props = {"href": "https://www.exemple.com", "target": "_blank"})
        s = node.props_to_html()
        self.assertEqual(s, ' href="https://www.exemple.com" target="_blank"')
        
    def test_repr_eq(self):
        node = HTMLNode("a", "this is a link", None, {"href": "https://www.exemple.com", "target": "_blank"})
        self.assertEqual(node.__repr__(), 'HTMLNode(a, this is a link, None,  href="https://www.exemple.com" target="_blank")')
    

if __name__ == "__main__":
    unittest.main()