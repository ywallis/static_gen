import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter


class TestSplitNodeDelimiter(unittest.TestCase):
    def test_split_code(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.NORMAL),
            ],
        )
        
    def test_split_code_multiple(self):
        node = TextNode("This is text with 2 `code` in `block` words", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with 2 ", TextType.NORMAL),
                TextNode("code", TextType.CODE),
                TextNode(" in ", TextType.NORMAL),
                TextNode("block", TextType.CODE),
                TextNode(" words", TextType.NORMAL),
            ],
        )

    def test_split_bold(self):
        node = TextNode("This is text with a **bold block** word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("bold block", TextType.BOLD),
                TextNode(" word", TextType.NORMAL),
            ],
        )

    def test_split_italic(self):
        node = TextNode("This is text with an _italic block_ word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("italic block", TextType.ITALIC),
                TextNode(" word", TextType.NORMAL),
            ],
        )

    def test_split_code_invalid(self):
        node = TextNode(
            "This is text with an invalid `code block word", TextType.NORMAL
        )
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)
