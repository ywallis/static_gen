from enum import Enum


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other) -> bool:
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict[str, str] = {},
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is not None:
            return " ".join([f'{key}="{value}"' for key, value in self.props.items()])

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, other):
        return vars(self) == vars(other)


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict[str, str] = {},
    ) -> None:
        super().__init__(tag, value, children, props)
        if value is None:
            raise ValueError("leaf nodes must have a value")

    def to_html(self):
        if self.tag is None:
            return self.value

        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: list["HTMLNode"],
        props: dict[str, str] = {},
    ) -> None:
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("all parent nodes should have a tag")
        if self.children is None:
            raise ValueError("all parent nodes should have children")

        return f"<{self.tag}>{''.join(map(lambda x: x.to_html(), self.children))}</{self.tag}>"
