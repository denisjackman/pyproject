'''
    pdf to doc converter
'''
from pdf2docx import Converter

INPUT_PDF_FILE = "Z:/temp/The_Fifth_Edition_Gamemasters_Survival_Guide_-_v1.8.pdf"
OUTPUT_DOC_FILE = "Z:/temp/example.docx"


def convert_pdf_to_docx(pdf_file: str, doc_file: str):
    '''
        convert pdf to docx
    '''
    cv = Converter(pdf_file)
    cv.convert(doc_file, start=0, end=None)
    cv.close()


def main():
    ''' main '''
    convert_pdf_to_docx(INPUT_PDF_FILE, OUTPUT_DOC_FILE)


if __name__ == '__main__':
    main()
