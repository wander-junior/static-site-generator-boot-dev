import os
import shutil
import sys

from generate_page import generate_pages_recursive

def copy_folder(source: str, destination: str, initial: bool = True):
    if os.path.exists(source) == False:
        raise ValueError(f"Invalid Source Path: {source}")

    if os.path.exists(destination) == False:
        os.mkdir(destination)
    else:
        if os.path.isfile(destination):
            raise ValueError(f"Destination {destination} is not a directory")
        if initial:
            shutil.rmtree(destination)
            os.mkdir(destination)

    if os.path.isfile(source):
        print(f"Pasting {source} into {destination}")
        shutil.copy(source, destination)
    else:
        source_contents = os.listdir(source)
        for content in source_contents:
            full_path = os.path.join(source, content)
            
            if os.path.isfile(full_path) == False:
                new_destination = os.path.join(destination, content)
                copy_folder(full_path, new_destination, False)
            else:
                copy_folder(full_path, destination, False)

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    copy_folder("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

main()