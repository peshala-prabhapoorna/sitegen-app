import re

from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    title = re.match(r"^# (.+)$", markdown, re.MULTILINE).group(1)
    if not title:
        raise Exception("invalid markdown: document has no title")

    return title.strip()


def generate_page(markdown, template_path):
    print("generating page")

    template = None
    with open(template_path, "r") as file:
        template = file.read()

    node = markdown_to_html_node(markdown)
    html = node.to_html()
    title = extract_title(markdown)

    titled_template = template.replace("{{ Title }}", title)
    html_page = titled_template.replace("{{ Content }}", html)

    return html_page
