from leafnode import LeafNode
from textnode import TextNode, TextType
from htmlnode import HTMLNode


def text_node_to_html_node(text_node: TextNode) -> HTMLNode:
    match text_node.text_type:
        case TextType.NORMAL:
            return LeafNode(tag=None, value=text_node.text, children=None)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text, children=None)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text, children=None)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text, children=None)
        case TextType.LINK:
            return LeafNode(
                tag="a",
                value=text_node.text,
                props={"href": f"{text_node.url}"},
            )
        case TextType.IMAGE:
            return LeafNode(
                tag="img",
                value="",
                props={"src": f"{text_node.url}", "alt": f"{text_node.text}"},
            )
        case _:
            raise Exception("invalid text type detected")
