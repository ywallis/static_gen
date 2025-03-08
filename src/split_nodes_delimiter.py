from textnode import TextNode, TextType

# pseudocode:
# only process .normal nodes
# if len node.split(delimiter) == 3
#


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
