# -*- coding: utf-8 -*-
''' pdf to text conversion '''
from PyPDF2 import PdfReader

INPUTFILE = "y:/Resources/reference/python-reference.pdf"
OUTPUTFILE = "Y:/Resources/development/output.txt"


def convertpdftotxt(inputfile, outputfile, verbosemode = False):
    '''Converts PDF file to text file'''
    if verbosemode:
        print("[-] Converting PDF to text")
        print(f"[-] inputfile {inputfile}")
        print(f"[-] outputfile {outputfile}")
    pdfread = PdfReader(inputfile)
    pdfpages = len(pdfread.pages)
    if verbosemode:
        print(f"number of pages {pdfpages}")
    for item in range(pdfpages):
        pageObj = pdfread.pages[item]
        with open(outputfile, 'a+', encoding='utf-8-sig') as outfile:
            outfile.write((pageObj.extract_text()))
        if verbosemode:
            print(pageObj.extract_text()) #This just provides the overview of what is being added to your output, you can remove it if want

def main():
    '''Main function'''
    convertpdftotxt(INPUTFILE, OUTPUTFILE)

if __name__ == '__main__':
    main()
