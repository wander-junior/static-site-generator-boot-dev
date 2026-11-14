from markdown_blocks import block_to_block_type 

def main():
    text = """```
        Blabla
    ``` Blabla"""

    print(block_to_block_type(text))

main()