'''
    pdf to doc converter
'''
from pdf2docx import Converter


def convert_pdf_to_docx(pdf_file: str, doc_file: str):
    '''
        convert pdf to docx
    '''
    cv = Converter(pdf_file)
    cv.convert(doc_file, start=0, end=None)
    cv.close()

def main():
    ''' main '''
    convert_pdf_to_docx("y:/house-data/Coop-0064.pdf", "Y:/house-data/coop0064.docx")

if __name__ == '__main__':
    main()
