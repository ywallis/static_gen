from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType
from split_nodes_link_images import split_nodes_link, split_nodes_image


def text_to_textnode(text: str):
    node = TextNode(text=text, text_type=TextType.NORMAL)
    bold = split_nodes_delimiter([node], "**", TextType.BOLD)
    italic = split_nodes_delimiter(bold, "_", TextType.ITALIC)
    code = split_nodes_delimiter(italic, "`", TextType.CODE)
    links = split_nodes_link(code)
    images = split_nodes_image(links)
    return images
