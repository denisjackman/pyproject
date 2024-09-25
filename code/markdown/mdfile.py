''' write markdown to a file '''
# Python script to write markdown into a file

# Define the markdown content

MARKDOWN_CONTENT = """
# Sample Markdown File

## Headers

### This is a Level 3 Header

This file demonstrates some basic Markdown formatting.

## Lists

### Unordered List:
- Item 1
- Item 2
  - Nested Item 2.1
  - Nested Item 2.2
- Item 3

### Ordered List:
1. First Item
2. Second Item
   1. Sub-item 2.1
   2. Sub-item 2.2
3. Third Item

## Links

You can create a [link to Google](https://www.google.com) like this.

## Table

Here is a table:

| Header 1 | Header 2 | Header 3 |
| -------- | -------- | -------- |
| Row 1, Col 1 | Row 1, Col 2 | Row 1, Col 3 |
| Row 2, Col 1 | Row 2, Col 2 | Row 2, Col 3 |
| Row 3, Col 1 | Row 3, Col 2 | Row 3, Col 3 |

## Conclusion

That's a quick example of a Markdown file!
"""


def main():
    ''' main function '''
    # Write the markdown content to a file
    file_name = "sample_markdown.md"

    with open(file_name,
              "w",
              encoding='utf-8-sig') as markdown_file:
        markdown_file.write(MARKDOWN_CONTENT)

    print(f"Markdown file '{file_name}' created successfully.")


if __name__ == '__main__':
    main()
