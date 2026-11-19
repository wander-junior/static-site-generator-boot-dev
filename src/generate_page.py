from markdown_blocks import markdown_to_html_node

def extract_title(markdown: str) -> str:
    markdown_lines = markdown.splitlines()

    for line in markdown_lines:
        if line.startswith("# "):
            return line.removeprefix("# ").strip()

    raise ValueError("No header in file")

def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

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
        )

        destination_file.write(resulting_html)