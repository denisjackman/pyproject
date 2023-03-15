'''My daily pyton code habit code '''
from PyPDF2 import PdfReader
PDF_FILENAME = "sample-50-MB-pdf-file.pdf"
def main():
    ''' This is the main function '''
    print("Starting")
    reader = PdfReader(PDF_FILENAME)
    for page in reader.pages:
        print("-------------------------------")
        print(page.extract_text())
        print("-------------------------------")
    print(f"Number of pages: {len(reader.pages)}")
    print("Done")
    
if __name__ == '__main__':
    main()
