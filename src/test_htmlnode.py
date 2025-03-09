import unittest

from objects import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
            "p",
            "test_text",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        node2 = HTMLNode(
            "p",
            "test_text",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode(
            "p",
            "test_text",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        node2 = HTMLNode(
            "p",
            "test_text2",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode(
            "p",
            "test_text",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )

        self.assertEqual(
            node.props_to_html(), 'href="https://www.google.com" target="_blank"'
        )


if __name__ == "__main__":
    unittest.main()
