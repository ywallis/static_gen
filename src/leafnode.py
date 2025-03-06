from typing import override
from htmlnode import HTMLNode

class LeafNode(HTMLNode):

    def __init__(self, tag: str | None = None, value: str | None = None, children: list["HTMLNode"] | None = None, props: dict[str, str] | None = None) -> None:
        super().__init__(tag, value, children, props)
        if value is None:
            raise ValueError("leaf nodes must have a value")


    @override
    def to_html(self):
        if self.tag is None:
            return self.value

        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
