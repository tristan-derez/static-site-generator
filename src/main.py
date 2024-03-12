import os
import shutil

from copy_dir import copy_directory_folder


def main():
    src_dir = "./static"
    dest_dir = "./public"

    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
        print(f"Deleted contents of {dest_dir}")

    copy_directory_folder(src_dir, dest_dir)


main()
