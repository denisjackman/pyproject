'''My daily pyton code habit code '''
from PyPDF4 import PdfFileReader
PDF_FILENAME =  r"y:/pyproject/code/viscous/chapter3/data/ANONOPS_The_Press_Release.pdf"
def main():
    ''' This is the main function '''
    print("Starting")
    reader = PdfFileReader(PDF_FILENAME)
    for page in reader.pages:
        print("-------------------------------")
        print(page.extractText())
        print("-------------------------------")
    print(f"Number of pages: {len(reader.pages)}")
    print("Done")

if __name__ == '__main__':
    main()
