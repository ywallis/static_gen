import unittest
from leafnode import LeafNode
from parentnode import ParentNode


class TestHTMLNode(unittest.TestCase):
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

    def test_to_html_many_children(self):
        child_1 = LeafNode("div", "front")
        child_2 = LeafNode("div", "back")
        child_3 = LeafNode("div", "left")
        parent = ParentNode("div", [child_1, child_2, child_3])

        self.assertEqual(
            parent.to_html(), "<div><div>front</div><div>back</div><div>left</div></div>"
        )
