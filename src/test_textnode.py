import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
