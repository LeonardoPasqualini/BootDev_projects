import unittest
from src.parent_node import ParentNode
from src.leaf_node import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        
    def test_rise_parent_without_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        self.assertRaises(ValueError, parent_node.to_html)
        parent_node = ParentNode("", [child_node])
        self.assertRaises(ValueError, parent_node.to_html)
        
    def test_rise_parent_without_children(self):
        parent_node = ParentNode("span", None)
        self.assertRaises(ValueError, parent_node.to_html)
        parent_node = ParentNode("span", [])
        self.assertRaises(ValueError, parent_node.to_html)