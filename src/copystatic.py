import os
import shutil


def copy_dir(src, dst):
    os.mkdir(dst)

    paths = os.listdir(src)
    for path in paths:
        src_path = f"{src}/{path}"
        dst_path = f"{dst}/{path}"

        if os.path.isdir(src_path):
            copy_dir(src_path, dst_path)
        else:
            shutil.copy(src_path, dst_path)
            print(f"{src_path} -> {dst_path}")
