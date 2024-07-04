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
