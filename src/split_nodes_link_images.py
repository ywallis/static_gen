from textnode import TextNode, TextType
from extract_regex import extract_markdown_links, extract_markdown_images


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

