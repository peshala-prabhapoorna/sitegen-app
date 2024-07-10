import os
import shutil


from copystatic import copy_dir
from gencontent import generate_page


static_path = "./static"
public_path = "./public"


from_path = "./content/index.md"
template_path = "./template.html"
dest_path = "./public"


def main():
    print("deleting public directory...")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)

    print("copying static files to public directory...")
    copy_dir(static_path, public_path)

    generate_page(from_path, template_path, dest_path)


main()
