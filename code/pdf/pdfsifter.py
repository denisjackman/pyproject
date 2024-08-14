'''
    extract stuff from a pdf file
'''
import os
import sys
import pypdf
from tqdm import tqdm
# pylint: disable=C0413
sys.path.append(os.path.realpath('..\\..'))
from jackmanimation.utilities.fileutility import walk_through
from jackmanimation.utilities.fileutility import extract_file_extension

TARGETDIRECTORY = r"Z:\Library"
TARGETSTRING = "Python"
DEBUGMODE = True


def debug_mode(debugstring):
    ''' debug mode'''
    if DEBUGMODE:
        with open(r'Z:\Resources\development\debug.txt',
                  'a',
                  encoding='utf-8-sig') as debug_file:
            debug_file.write(f'[*] {debugstring}\n')


def unique(sortlist):
    ''' sort a list for unique items '''
    result = []
    listset = set(sortlist)
    result = list(listset)
    return result


def main():
    '''
        main routine
    '''
    print('[+] Starting project file running ')

    totallist = []
    pdflist = []
    targetlist = []
    errorlist = []

    totallist.extend(walk_through({"verbosemode": False, "deletemode": False, "startdirectory": TARGETDIRECTORY}))
    print(f"[-] Records found {len(totallist):,}")
    for item in tqdm(totallist, total=len(totallist), unit=' item'):
        tmpext = extract_file_extension(item)
        if tmpext == '.pdf':
            if 'site-packages' not in item:
                pdflist.append(item)
    print(f'[-] Total PDF files is {len(pdflist):,}')
    print('[-] Checking PDF files ')
    print(f'[-] Target string is {TARGETSTRING}')
    for pdfitem in tqdm(pdflist, total=len(pdflist), unit=' item'):
        with open(pdfitem, 'rb') as pdf_file:
            pdf_reader = pypdf.PdfReader(pdf_file, strict=False)
            print(f"[*] PDF file is {pdfitem} --")
            if pdf_reader.metadata is None:
                debug_mode(f"[*] PDF file is {pdfitem} -- title (NO TITLE) --")
            else:
                debug_mode(f"[*] PDF file is {pdfitem} -- title {pdf_reader.metadata.title} --")
            try:
                pagecount = len(pdf_reader.pages)
            except Exception as err:
                debug_mode(f'[=] Error {err} in {pdfitem}')
                errorlist.append(f'[-] Error {err} in {pdfitem}')
                continue
            for page in range(pagecount):
                try:
                    pagetext = pdf_reader.pages[page]
                    text = pagetext.extract_text()
                    if TARGETSTRING in text:
                        targetlist.append(pdfitem)
                        debug_mode(f"[-] Found target string {TARGETSTRING} in {pdfitem} ")
                except Exception as err:
                    debug_mode(f'[=] Parsing Error {err} in {pdfitem}')
                    errorlist.append(f'[-] Error {err} in {pdfitem}')
                    continue

    targetlist = unique(targetlist)
    errorlist = unique(errorlist)

    print(f'[-] Total PDF files with target string is {len(targetlist):,}')

    for item in tqdm(targetlist, total=len(targetlist), unit=' item'):
        print(f'[-] Found PDF file with target string {item}')

    for erritem in tqdm(errorlist, total=len(errorlist), unit=' item'):
        print(f'[-] Error {erritem}')
    print('[+] Finishing project file running ')


if __name__ == '__main__':
    main()
