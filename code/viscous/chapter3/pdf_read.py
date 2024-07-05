''' pdf reader '''
import os
import argparse
import sys
from pypdf import PdfReader

RUN_NAME = os.path.basename(__file__)


def print_meta(filename):
    ''' print metadata '''
    with open(filename, 'rb') as pdf_file:
        pdf_file = PdfReader(pdf_file)
        doc_info = pdf_file.getDocumentInfo()
        print(f'[*] PDF MetaData For: {str(filename)}')
        for meta_item in doc_info:
            print(f'[+] {meta_item}: {doc_info[meta_item]}')


def main():
    ''' main '''
    print(f'[*] {RUN_NAME} starting')
    parser = argparse.ArgumentParser(description='PDF MetaData Reader')
    parser.add_argument('-F',
                        '--file',
                        type=str,
                        metavar='filename',
                        required=True,
                        help='PDF file name')
    arg = parser.parse_args()
    filename = arg.file
    if filename is None:
        print(f'[-] {RUN_NAME} requires a PDF file name')
        sys.exit()
    else:
        print_meta(filename)
    print(f'[*] {RUN_NAME} ending')


if __name__ == '__main__':
    main()
