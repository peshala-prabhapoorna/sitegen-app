import os
import re


from markdown_blocks import markdown_to_html_node


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    paths = os.listdir(dir_path_content)
    for path in paths:
        full_path_content = f"{dir_path_content}/{path}"
        full_path_dest = f"{dest_dir_path}/{path}"

        if os.path.isdir(full_path_content):
            generate_pages_recursive(
                full_path_content, template_path, full_path_dest
            )
        else:
            generate_page(full_path_content, template_path, dest_dir_path)


def extract_title(markdown):
    title = re.match(r"^# (.+)$", markdown, re.MULTILINE).group(1)
    if not title:
        raise Exception("invalid markdown: document has not title")

    return title.strip()


def generate_page(from_path, template_path, dest_path):
    print(
        f"generating page from {from_path} to {dest_path} using "
        f"{template_path}"
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
