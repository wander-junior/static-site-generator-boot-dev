import os

from markdown_blocks import markdown_to_html_node

def extract_title(markdown: str) -> str:
    markdown_lines = markdown.splitlines()

    for line in markdown_lines:
        if line.startswith("# "):
            return line.removeprefix("# ").strip()

    raise ValueError("No header in file")

def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with (
        open(from_path) as from_file, 
        open(template_path) as template_file,
        open(dest_path, "w") as destination_file
    ):
        markdown_content = from_file.read()
        template_content = template_file.read()

        html_markdown = markdown_to_html_node(markdown_content).to_html()
        page_title = extract_title(markdown_content)

        resulting_html = (
            template_content
            .replace("{{ Title }}", page_title)
            .replace("{{ Content }}", html_markdown)
            .replace('href="/', f'href="{basepath}')
            .replace('src="/', f'src="{basepath}')
        )

        destination_file.write(resulting_html)

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str, basepath: str):
    if os.path.isfile(dir_path_content):
        generate_page(dir_path_content, template_path, dest_dir_path + "/index.html", basepath)

    else:
        dir_contents = os.listdir(dir_path_content)
        for content in dir_contents:
            full_path = os.path.join(dir_path_content, content)
            
            if os.path.isfile(full_path) == False:
                new_destination = os.path.join(dest_dir_path, content)
                generate_pages_recursive(full_path, template_path, new_destination, basepath)
            else:
                generate_pages_recursive(full_path, template_path, dest_dir_path, basepath)        
