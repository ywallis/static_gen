from textnode import TextNode, TextType
from htmlnode import HTMLNode


def main():
    test = TextNode("test", TextType.NORMAL, "www.cm")
    print(test)
    html = HTMLNode(
        "p",
        "test_text",
        None,
        {
            "href": "https://www.google.com",
            "target": "_blank",
        },
    )
    print(html)

    print(html.props_to_html())

if __name__ == "__main__":
    main()
