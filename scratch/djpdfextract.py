'''
    extract stuff from a pdf file
'''
import PyPDF2

def main():
    '''
        main routine
    '''
    pdf_file = open("y:/house-data/Backed Projects — Kickstarter.pdf", 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    page = pdf_reader.getPage(0)
    print(page.extractText())
    pdf_file.close()

if __name__ == '__main__':
    main()
