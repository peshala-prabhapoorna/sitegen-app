import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            tag="a",
            value="link here",
            props={"href": "https://lavenderleit.dev", "rel": "external"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://lavenderleit.dev" rel="external"',
        )

    def test_repr(self):
        node = HTMLNode(
            tag="a",
            value="link here",
            props={"href": "https://lavenderleit.dev", "rel": "external"},
        )
        self.assertEqual(
            repr(node),
            (
                "HTMLNode(a, link here, None, "
                "{'href': 'https://lavenderleit.dev', 'rel': 'external'})"
            ),
        )

    def test_repr_with_child(self):
        child_node = HTMLNode(
            tag="b",
            value="bold",
            props={"id": "bold_id", "class": "bold_class"},
        )
        node = HTMLNode(
            tag="p",
            value="this is a paragraph with <b>bold</b> text.",
            children=[child_node],
            props={"id": "para_id", "class": "para_class"},
        )
        self.assertEqual(
            repr(node),
            (
                "HTMLNode(p, this is a paragraph with <b>bold</b> text., "
                "[HTMLNode(b, bold, None, "
                "{'id': 'bold_id', 'class': 'bold_class'})], "
                "{'id': 'para_id', 'class': 'para_class'})"
            ),
        )


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        leaf = LeafNode(
            "p",
            "this is a leaf node",
            {"id": "para_id", "class": "para_class"},
        )
        self.assertEqual(
            leaf.to_html(),
            '<p id="para_id" class="para_class">this is a leaf node</p>',
        )

    def test_repr(self):
        leaf = LeafNode(
            "p",
            "this is a leaf node",
            {"id": "para_id", "class": "para_class"},
        )
        self.assertEqual(
            repr(leaf),
            (
                "LeafNode(p, this is a leaf node, "
                "{'id': 'para_id', 'class': 'para_class'})"
            ),
        )


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html_with_nested(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text", {"id": "bold_id"}),
                LeafNode(None, "Normal text"),
                ParentNode(
                    "a",
                    [
                        LeafNode("i", "italic text", {"color": "red"}),
                        LeafNode(None, "Normal text"),
                    ],
                    {"href": "https://lavenderleit.dev"},
                ),
                LeafNode(None, "Normal text"),
            ],
            {"id": "p_out_id", "class": "p_out_class"},
        )
        self.assertEqual(
            node.to_html(),
            (
                '<p id="p_out_id" class="p_out_class"><b id="bold_id">'
                'Bold text</b>Normal text<a href="https://lavenderleit.dev">'
                '<i color="red">italic text</i>Normal text</a>Normal text</p>'
            ),
        )


if __name__ == "__main__":
    unittest.main()
