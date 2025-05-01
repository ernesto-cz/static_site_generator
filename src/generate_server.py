import re
import os

from markdown_html import(
    markdown_to_html_node
)

def extract_title(markdown):
    header = re.findall(r"^# .+", markdown)[0]
    if not header.startswith("#"):
        raise ValueError("Markdown file does not contain a H1 (#) header.")
    return header[2:].strip()

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        md = file.read()
    title = extract_title(md)
    with open(template_path) as file:
        template = file.read()
    html = markdown_to_html_node(md).to_html()
    template = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    if not os.path.isdir(dest_path):
        dirs_path = dest_path.rsplit("/", 1)[0]
        os.makedirs(dirs_path, exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    names = os.listdir(dir_path_content)
    for name in names:
        from_path = os.path.join(dir_path_content, name)
        dest_path = os.path.join(dest_dir_path, name)
        if name == '.DS_Store':
            continue
        if os.path.isfile(from_path):
            html_name = f"{name.split('.')[0]}.html"
            dest_path = os.path.join(dest_dir_path, html_name)
            generate_page(from_path, template_path, dest_path)
        if os.path.isdir(from_path):
            os.mkdir(dest_path)
            generate_pages_recursive(from_path, template_path, dest_path)
    return
