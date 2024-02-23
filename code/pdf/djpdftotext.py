# -*- coding: utf-8 -*-
''' pdf to text conversion '''
from PyPDF4 import PdfFileReader

INPUTFILE = r"y:/pyproject/code/viscous/chapter3/data/ANONOPS_The_Press_Release.pdf"
OUTPUTFILE = r"Z:/Resources/development/anon.txt"


def convertpdftotxt(inputfile, outputfile, verbosemode = False):
    '''Converts PDF file to text file'''
    if verbosemode:
        print("[-] Converting PDF to text")
        print(f"[-] inputfile {inputfile}")
        print(f"[-] outputfile {outputfile}")
    pdfread = PdfFileReader(inputfile)
    pdfpages = len(pdfread.pages)
    if verbosemode:
        print(f"number of pages {pdfpages}")
    for item in range(pdfpages):
        pageObj = pdfread.pages[item]
        with open(outputfile, 'a+', encoding='utf-8-sig') as outfile:
            outfile.write((pageObj.extractText()))
        if verbosemode:
            print(pageObj.extractText()) #This just provides the overview of what is being added to your output, you can remove it if want

def main():
    '''Main function'''
    convertpdftotxt(INPUTFILE, OUTPUTFILE)

if __name__ == '__main__':
    main()
