'''
    extract stuff from a pdf file
'''
import os
import sys
import PyPDF2
from tqdm import tqdm
# pylint: disable=C0413
sys.path.append(os.path.realpath('..'))
from djmodule.djutilities.fileutility import walk_through
from djmodule.djutilities.fileutility import extract_file_extension

TARGETDIRECTORY = r"Z:\library"
TARGETSTRING = "Python"
def unique
def main():
    '''
        main routine
    '''
    print('[+] Starting project file running ')
    totallist = []
    commands = {"verbosemode":False, "deletemode":False, "startdirectory":TARGETDIRECTORY}
    totallist.extend(walk_through(commands))
    pdflist = []
    print(f"[-] Records found {len(totallist):,}")

    for item in tqdm(totallist, total=len(totallist), unit=' item'):
        tmpext = extract_file_extension(item)
        if tmpext == '.pdf':
            if 'site-packages' not in item:
                pdflist.append(item)
    print(f'[-] Total PDF files is {len(pdflist):,}')
    print('[-] Checking PDF files ')
    print(f'[-] Target string is {TARGETSTRING}')
    targetlist = []
    errorlist = []
    for pdfitem in tqdm(pdflist, total=len(pdflist), unit=' item'):
        with open(pdfitem, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            try:
                pagecount = len(pdf_reader.pages)
            except Exception as err:
                errorlist.append(f'[-] Error {err} in {pdfitem}')
                continue
            for page in range(pagecount):
                pagetext = pdf_reader.pages[page]
                try:
                    text = pagetext.extract_text()
                    if TARGETSTRING in text:
                        targetlist.append(pdfitem)
                except Exception as err:
                    errorlist.append(f'[-] Error {err} in {pdfitem}')
                    continue
    print(f'[-] Total PDF files with target string is {len(targetlist):,}')

    for item in targetlist:
        print(f'[-] Found PDF file with target string {item}')
    for erritem in errorlist:
        print(f'[-] Error {erritem}')
    print('[+] Finishing project file running ')

if __name__ == '__main__':
  