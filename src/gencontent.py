import os
import re


from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    title = re.match(r"^# (.+)$", markdown, re.MULTILINE).group(1)
    if not title:
        raise Exception("invalid markdown: document has not title")

    return title.strip()


def generate_page(from_path, template_path, dest_path):
    print(
        f"generating page from {from_path} to {dest_path} using "
        "{template_path}"
    )

    markdown = None
    with open(from_path, "r") as file:
        markdown = file.read()

    template = None
    with open(template_path, "r") as file:
        template = file.read()

    node = markdown_to_html_node(markdown)
    html = node.to_html()
    title = extract_title(markdown)

    titled_template = template.replace("{{ Title }}", title)
    html_page = titled_template.replace("{{ Content }}", html)

    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    with open(f"{dest_path}/index.html", "w") as file:
        file.write(html_page)
