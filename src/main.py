import os
import shutil

from copy_dir import copy_directory_folder
from generate_page import generate_page


def main():
    src_dir = "./static"
    dest_dir = "./public"

    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
        print(f"Deleted contents of {dest_dir}")

    copy_directory_folder(src_dir, dest_dir)

    source_path = "./content/index.md"
    template_path = "./template.html"
    destination_path = "./public/index.html"

    generate_page(source_path, template_path, destination_path)


main()
