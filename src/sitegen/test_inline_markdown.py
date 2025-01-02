import unittest

from .textnode import TextNode, TextType
from .inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
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

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**",
            TextType.TEXT,
        )
        self.assertListEqual(
            split_nodes_delimiter([node], "**", TextType.BOLD),
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
        )

    def test_split_nodes_delimiter_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
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


class TestExtractUrl(unittest.TestCase):
    def test_extract_markdown_image(self):
        text = (
            "This is text with an ![image](https://picsum.photos/200/300)"
            " and ![another](https://picsum.photos/200)"
        )
        self.assertEqual(
            extract_markdown_images(text),
            [
                ("image", "https://picsum.photos/200/300"),
                ("another", "https://picsum.photos/200"),
            ],
        )

    def test_extract_markdown_links(self):
        text = (
            "This is text with a [link](https://www.example.com) and "
            "[another](https://www.example.com/another)"
        )
        self.assertEqual(
            extract_markdown_links(text),
            [
                ("link", "https://www.example.com"),
                ("another", "https://www.example.com/another"),
            ],
        )


class TestSplitImagesLinks(unittest.TestCase):
    def test_split_nodes_just_image(self):
        node = TextNode(
            "![image](https://picsum.photos/200/300)", TextType.TEXT
        )
        self.assertEqual(
            split_nodes_image([node]),
            [
                TextNode(
                    "image", TextType.IMAGE, "https://picsum.photos/200/300"
                )
            ],
        )

    def test_split_nodes_images(self):
        node = TextNode(
            "This is text with an ![image](https://picsum.photos/200/300) and"
            " another ![second image](https://picsum.photos/200) last words.",
            TextType.TEXT,
        )
        self.assertEqual(
            split_nodes_image([node]),
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode(
                    "image", TextType.IMAGE, "https://picsum.photos/200/300"
                ),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://picsum.photos/200"
                ),
                TextNode(" last words.", TextType.TEXT),
            ],
        )

    def test_split_nodes_image_no_link(self):
        node1 = TextNode("This text has no image link in it.", TextType.TEXT)
        node2 = TextNode(
            "Text with [link](https://example.com/) here.", TextType.LINK
        )
        self.assertEqual(
            split_nodes_image([node1, node2]),
            [
                TextNode("This text has no image link in it.", TextType.TEXT),
                TextNode(
                    "Text with [link](https://example.com/) here.",
                    TextType.LINK,
                ),
            ],
        )

    def test_split_nodes_image_multi_nodes(self):
        node1 = TextNode(
            "![image](https://picsum.photos/200/300)", TextType.TEXT
        )
        node2 = TextNode("This text has no image link in it.", TextType.TEXT)
        node3 = TextNode(
            "This is text with an ![image](https://picsum.photos/200/300) and"
            " another ![second image](https://picsum.photos/200) last words.",
            TextType.TEXT,
        )
        self.assertEqual(
            split_nodes_image([node1, node2, node3]),
            [
                TextNode(
                    "image", TextType.IMAGE, "https://picsum.photos/200/300"
                ),
                TextNode("This text has no image link in it.", TextType.TEXT),
                TextNode("This is text with an ", TextType.TEXT),
                TextNode(
                    "image", TextType.IMAGE, "https://picsum.photos/200/300"
                ),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://picsum.photos/200"
                ),
                TextNode(" last words.", TextType.TEXT),
            ],
        )


class TestSplitLinks(unittest.TestCase):
    def test_split_nodes_just_link(self):
        node = TextNode("[link](https://example.com/)", TextType.TEXT)
        self.assertEqual(
            split_nodes_link([node]),
            [TextNode("link", TextType.LINK, "https://example.com/")],
        )

    def test_split_nodes_links(self):
        node = TextNode(
            "This is text with an [link](https://example.com/) and"
            " another [link](https://example.com/) last words.",
            TextType.TEXT,
        )
        self.assertEqual(
            split_nodes_link([node]),
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com/"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com/"),
                TextNode(" last words.", TextType.TEXT),
            ],
        )

    def test_split_nodes_link_no_link(self):
        node1 = TextNode("This text has no link link in it.", TextType.TEXT)
        node2 = TextNode(
            "Text with [link](https://example.com/) here.", TextType.LINK
        )
        self.assertEqual(
            split_nodes_link([node1, node2]),
            [
                TextNode("This text has no link link in it.", TextType.TEXT),
                TextNode(
                    "Text with [link](https://example.com/) here.",
                    TextType.LINK,
                ),
            ],
        )

    def test_split_nodes_link_multi_nodes(self):
        node1 = TextNode("[link](https://example.com/)", TextType.TEXT)
        node2 = TextNode("This text has no link link in it.", TextType.TEXT)
        node3 = TextNode(
            "This is text with an [link](https://example.com/) and"
            " another [link](https://example.com/) last words.",
            TextType.TEXT,
        )
        self.assertEqual(
            split_nodes_link([node1, node2, node3]),
            [
                TextNode("link", TextType.LINK, "https://example.com/"),
                TextNode("This text has no link link in it.", TextType.TEXT),
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com/"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com/"),
                TextNode(" last words.", TextType.TEXT),
            ],
        )


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = (
            "This is **text** with an *italic* word and a `code block` and an"
            " ![image](https://storage.googleapis.com/qvault-webapp-dynamic-"
            "assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode(
                    "image",
                    TextType.IMAGE,
                    (
                        "https://storage.googleapis.com/qvault-webapp-dynamic"
                        "-assets/course_assets/zjjcJKZ.png"
                    ),
                ),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
        )
