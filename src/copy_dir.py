import os
import shutil


def is_image(file_path):
    image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".tiff"]
    file_extension = os.path.splitext(file_path)[1].lower()
    return file_extension in image_extensions


def copy_directory_folder(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        dest_path = os.path.join(dest_dir, item)

        if os.path.isfile(src_path):
            if is_image(src_path):
                images_folder = os.path.join(dest_dir, "images")
                if not os.path.exists(images_folder):
                    os.mkdir(images_folder)
                shutil.copy(src_path, os.path.join(images_folder, item))
                print(f"Copied image: {src_path} to {images_folder}")
            else:
                shutil.copy(src_path, dest_path)
                print(f"Copied file: {src_path} to {dest_path}")
        elif os.path.isdir(src_path):
            copy_directory_folder(src_path, dest_path)
