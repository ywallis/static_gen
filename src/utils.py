import re

from objects import TextNode, TextType, HTMLNode, LeafNode


def extract_markdown_images(text: str):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text: str):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
        else:
            blocks = node.text.split(delimiter)
            if len(blocks) % 2 == 0:
                raise Exception("Invalid markdown syntax")
            new_nodes.extend(
                [
                    (
                        TextNode(block, text_type)
                        if i % 2 != 0
                        else TextNode(block, TextType.NORMAL)
                    )
                    for i, block in enumerate(blocks)
                ]
            )

    return new_nodes


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for old_node in old_nodes:
        # Skip non-text nodes
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue

        images = extract_markdown_images(old_node.text)

        if not images:
            # If no images found, keep the original node
            new_nodes.append(old_node)
            continue

        # Process the text with images
        remaining_text = old_node.text

        for image_alt, image_url in images:
            # Split at the current image
            parts = remaining_text.split(f"![{image_alt}]({image_url})", 1)

            # Add text before image if not empty
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.NORMAL))

            # Add the image node
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))

            # Update remaining text
            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""

        # Add any remaining text after the last image
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.NORMAL))

    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for old_node in old_nodes:
        # Skip non-text nodes
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue

        links = extract_markdown_links(old_node.text)

        if not links:
            # If no images found, keep the original node
            new_nodes.append(old_node)
            continue

        # Process the text with images
        remaining_text = old_node.text

        for link_alt, link_url in links:
            # Split at the current image
            parts = remaining_text.split(f"[{link_alt}]({link_url})", 1)

            # Add text before image if not empty
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.NORMAL))

            # Add the image node
            new_nodes.append(TextNode(link_alt, TextType.LINK, link_url))

            # Update remaining text
            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""

        # Add any remaining text after the last image
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.NORMAL))

    return new_nodes


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


def text_to_textnode(text: str):
    node = TextNode(text=text, text_type=TextType.NORMAL)
    bold = split_nodes_delimiter([node], "**", TextType.BOLD)
    italic = split_nodes_delimiter(bold, "_", TextType.ITALIC)
    code = split_nodes_delimiter(italic, "`", TextType.CODE)
    links = split_nodes_link(code)
    images = split_nodes_image(links)
    return images
