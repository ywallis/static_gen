from typing import override
from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: list["HTMLNode"],
        props: dict[str, str] | None = None,
    ) -> None:
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("all parent nodes should have a tag")
        if self.children is None:
            raise ValueError("all parent nodes should have children")

        return f"<{self.tag}>{''.join(map(lambda x: x.to_html(), self.children))}</{self.tag}>"
