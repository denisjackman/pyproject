'''
    extract stuff from a pdf file
'''
import PyPDF4


def main():
    '''
        main routine
    '''
    with open(r"Z:/pyproject/code/viscous/chapter3/data/ANONOPS_The_Press_Release.pdf",  # noqa: E501
              'rb') as pdf_file:
        pdf_reader = PyPDF4.PdfFileReader(pdf_file)
        page = pdf_reader.getPage(0)
        print(page.extractText())


if __name__ == '__main__':
    main()
