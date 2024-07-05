import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text.split(delimiter)
        if len(text) % 2 == 0:
            raise Exception(f"Invalid markdown syntax: '{node.text}'")

        nodes_from_text = []
        for i in range(len(text)):
            if text[i] == "":
                continue
            if i % 2 == 0:
                nodes_from_text.append(TextNode(text[i], TextType.TEXT))
            else:
                nodes_from_text.append(TextNode(text[i], text_type))

        new_nodes.extend(nodes_from_text)

    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        # extract the image links from text, split text and images and add
        # them as separate nodes
        text = old_node.text
        image_links = extract_markdown_images(text)
        if len(image_links) == 0:
            new_nodes.append(old_node)
            continue
        for image_link in image_links:
            # add text preceding a image link to new_nodes
            sections = text.split(f"![{image_link[0]}]({image_link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown: image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            # add the image node to new_nodes
            new_nodes.append(
                TextNode(image_link[0], TextType.IMAGE, image_link[1])
            )

            text = sections[1]

        # add the trailing text part after the last image link to new_nodes
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes


def extract_markdown_images(text):
    image_links = re.findall(r"!\[(.*?)\]\((.*?)\)", text)

    return image_links


def extract_markdown_links(text):
    links = re.findall(r"\[(.*?)\]\((.*?)\)", text)

    return links
