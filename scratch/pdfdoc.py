'''
    pdf to doc converter
'''
from pdf2docx import parse, Converter


def convert_pdf_to_docx(pdf_file: str, doc_file: str):
    '''
        convert pdf to docx
    '''
    cv = Converter(pdf_file)
    cv.convert(doc_file, start=0, end=None)
    cv.close()

def main():
    ''' main '''
    convert_pdf_to_docx("test.pdf", "newtest.docx")
 
if __name__ == '__main__':
    main()