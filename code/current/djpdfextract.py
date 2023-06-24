'''
    extract stuff from a pdf file
'''
import PyPDF2

def main():
    '''
        main routine
    '''
    with open("y:/house-data/Backed Projects — Kickstarter.pdf", 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        page = pdf_reader.getPage(0)
        print(page.extractText())

if __name__ == '__main__':
    main()
