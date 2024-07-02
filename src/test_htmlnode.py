import unittest

from htmlnode import HTMLNode, LeafNode


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
                "HTMLNode:\n"
                "tag     : a\n"
                "value   : link here\n"
                "children: None\n"
                "props   : {'href': 'https://lavenderleit.dev', 'rel': "
                "'external'}"
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
                "HTMLNode:\n"
                "tag     : p\n"
                "value   : this is a paragraph with <b>bold</b> text.\n"
                "children: [HTMLNode:\n"
                "tag     : b\n"
                "value   : bold\n"
                "children: None\n"
                "props   : {'id': 'bold_id', 'class': 'bold_class'}]\n"
                "props   : {'id': 'para_id', 'class': 'para_class'}"
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


if __name__ == "__main__":
    unittest.main()
