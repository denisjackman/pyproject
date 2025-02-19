''' pdf to doc converter '''
from pdf2docx import Converter

PDFFILE = "z:/store/pdf/derelict-sites-register.pdf"
DOCFILE = "z:/store/derelict-sites-register.docx"


def main():
    '''main function '''
    cv = Converter(PDFFILE)
    cv.convert(DOCFILE)
    cv.close()


if __name__ == "__main__":
    main()
