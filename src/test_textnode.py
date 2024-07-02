import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_ineq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This has a url", "link", "https://url.xyz")
        self.assertEqual(
            repr(node), "TextNode(This has a url, link, https://url.xyz)"
        )


if __name__ == "__main__":
    unittest.main()
