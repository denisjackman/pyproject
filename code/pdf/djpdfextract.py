'''
    extract stuff from a pdf file
'''
import pypdf


def main():
    '''
        main routine
    '''
    with open(r"Z:/pyproject/code/viscous/chapter3/data/ANONOPS_The_Press_Release.pdf",
              'rb') as pdf_file:
        pdf_reader = pypdf.PdfReader(pdf_file)
        page = pdf_reader.pages[0]
        print(page.extract_text())


if __name__ == '__main__':
    main()
