from inline_markdown import extract_markdown_links

def main():
    print(extract_markdown_links("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"))


main()