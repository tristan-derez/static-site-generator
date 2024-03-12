import os
import shutil

from copy_dir import copy_directory_folder
from generate_page import generate_pages_recursive


def main():
    src_dir = "./static"
    dest_dir = "./public"

    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
        print(f"Deleted contents of {dest_dir}")

    copy_directory_folder(src_dir, dest_dir)

    content_dir = "./content"
    template_path = "./template.html"

    generate_pages_recursive(content_dir, template_path, dest_dir)

    print("Site generation completed successfully.")


main()
