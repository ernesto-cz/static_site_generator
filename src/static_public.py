import os
import shutil

def source_to_destination(source, destination):
    delete_content_destination(destination)
    copy_content_source(source, destination)

def delete_content_destination(path):
    if not os.path.isdir(path):
        raise ValueError(f"Invalid path: {path!r} - must be a directory.")
    path = f"{path}." if path[-1] == "/" else f"{path}/."
    shutil.rmtree(path, ignore_errors=True)

def copy_content_source(source, destination):
    names = os.listdir(source)
    for name in names:
        from_path = os.path.join(source, name)
        dest_path = os.path.join(destination, name)
        if name == '.DS_Store':
            continue
        if os.path.isfile(from_path):
            shutil.copy(from_path,dest_path)
        if os.path.isdir(from_path):
            os.mkdir(dest_path)
            copy_content_source(from_path,dest_path)


"""
Good idea to print the tree using items :D

def copy_content_source(source, destination):
    items = {}
    names = os.listdir(source)
    for name in names:
        if name == '.DS_Store':
            continue
        if destination not in items:
            items[destination] = {}
        if os.path.isfile(f"{source}{name}"):
            items[destination]["file"] = name
            shutil.copy(f"{source}{name}",f"{destination}{name}")
        if os.path.isdir(f"{source}{name}"):
            os.mkdir(f"{destination}{name}")
            items[destination]["dir"] = copy_content_source(f"{source}{name}/",f"{destination}{name}/")
    return items
"""
