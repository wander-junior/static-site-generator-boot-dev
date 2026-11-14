from markdown_blocks import markdown_to_html_node 

def main():
    markdown = """
> This is a
> blockquote block

this is paragraph text

"""

    print(markdown_to_html_node(markdown).to_html())

main()