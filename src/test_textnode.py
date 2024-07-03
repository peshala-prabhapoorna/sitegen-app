import unittest

from textnode import TextNode, TextType, split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_ineq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This has a url", TextType.LINK, "https://url.xyz")
        self.assertEqual(
            repr(node),
            "TextNode(This has a url, TextType.LINK, https://url.xyz)",
        )


class TestSplitNodeFn(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([node], "`", TextType.CODE),
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([node], "**", TextType.BOLD),
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_split_nodes_delimiter_italic(self):
        node = TextNode("This is text with a *italicized* word", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([node], "*", TextType.ITALIC),
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("italicized", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_split_nodes_delimiter_multi(self):
        node1 = TextNode("This is text with a **bolded** word", TextType.TEXT)
        node2 = TextNode("italicized text", TextType.ITALIC)
        node3 = TextNode("link here", TextType.LINK, "https://boot.dev")
        node4 = TextNode(
            "This is another text with a **another bolded** word",
            TextType.TEXT,
        )
        self.assertEqual(
            split_nodes_delimiter(
                [node1, node2, node3, node4], "**", TextType.BOLD
            ),
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
                TextNode("italicized text", TextType.ITALIC),
                TextNode("link here", TextType.LINK, "https://boot.dev"),
                TextNode("This is another text with a ", TextType.TEXT),
                TextNode("another bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
        )


if __name__ == "__main__":
    unittest.main()
