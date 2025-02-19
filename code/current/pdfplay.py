'''My daily pyton code habit code '''
from pypdf import PdfReader
PDF_FILENAME = r"Z:/pyproject/code/"\
                "viscous/chapter3/data/"\
                "ANONOPS_The_Press_Release.pdf"


def main():
    ''' This is the main function '''
    print("Starting")
    reader = PdfReader(PDF_FILENAME)
    if len(reader.pages) > 0:
        page = reader.pages[0]
        text = page.extract_text()
        print("-------------------------------")
        print(text)
        print("-------------------------------")
    print(f"Number of pages: {len(reader.pages)}")
    print("Done")


if __name__ == '__main__':
    main()
