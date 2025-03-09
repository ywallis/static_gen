import unittest

from objects import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_eq_with_links(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.com")
        self.assertEqual(node, node2)

    def test_different_types(self):
        node = TextNode("Text1", TextType.NORMAL)
        node2 = TextNode("Text1", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_urls(self):
        node = TextNode("Text1", TextType.LINK, "www.com")
        node2 = TextNode("Text1", TextType.LINK, "www.ch")
        self.assertNotEqual(node, node2)

    def test_urls_1_is_none(self):
        node = TextNode("Text1", TextType.LINK)
        node2 = TextNode("Text1", TextType.LINK, "www.ch")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
