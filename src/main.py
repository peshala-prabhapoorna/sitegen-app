import os
import shutil


from copystatic import copy_dir
from gencontent import generate_pages_recursive


static_path = "./static"
public_path = "./public"


dir_path_content = "./content"
template_path = "./template.html"
dest_dir_path = "./public"


def main():
    print("deleting public directory...")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)

    print("copying static files to public directory...")
    copy_dir(static_path, public_path)

    generate_pages_recursive(dir_path_content, template_path, dest_dir_path)


main()
