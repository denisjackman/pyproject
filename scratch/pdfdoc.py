'''
    pdf to doc converter
'''
from pdf2docx import parse
from typing import tuple


def convert_pdf_to_docx(input_file: str, output_file: str, pages: tuple = None) -> None:
    '''
        convert pdf to docx
    '''

    if pages:
        pages = [int(i) for i in list(pages) if i.isnumeric()]
    result = parse(pdf_file=input_file,
                   docx_with_path=output_file, pages=pages)
    summary = {
        "File": input_file, "Pages": str(pages), "Output File": output_file
    }
    # Printing Summary
    print("## Summary ########################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
    print("###################################################################")
    return result    

def main():
    ''' main '''
    convert_pdf_to_docx(input_file="test.pdf", output_file="test.docx")

if __name__ == '__main__':
    main()

