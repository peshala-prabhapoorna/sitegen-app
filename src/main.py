import os
import shutil


from copystatic import copy_dir


static_path = "static"
public_path = "public"


def main():
    print("deleting public directory...")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)

    print("copying static files to public directory...")
    copy_dir(static_path, public_path)


main()
