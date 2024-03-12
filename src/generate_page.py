import os

from block_md import markdown_to_html_node
from pathlib import Path


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.strip().startswith("#"):
            return line.strip()[1:].strip()
    raise Exception("Invalid markdown: no h1 header found")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown_content = f.read()

    with open(template_path, "r") as f:
        template_content = f.read()

    html_content = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)
    final_html = template_content.replace("{{ Title }}", title).replace(
        "{{ Content }}", html_content
    )

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(final_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        full_path = os.path.join(dir_path_content, entry)
        if os.path.isfile(full_path) and entry.endswith(".md"):
            generate_page(
                full_path,
                template_path,
                os.path.join(dest_dir_path, f"{Path(entry).stem}.html"),
            )
        elif os.path.isdir(full_path):
            sub_dest_dir_path = os.path.join(dest_dir_path, entry)
            generate_pages_recursive(full_path, template_path, sub_dest_dir_path)
