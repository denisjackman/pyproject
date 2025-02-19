'''
enchilda.py

This is a os utility tool

'''
import os
import sys
from tqdm import tqdm

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.utilities.fileutility import walk_through
from jackmanimation.utilities.fileutility import getargs

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.01 $"
__date__ = "$Date: 2022/07/28 01:17:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"


def main():
    '''
        this is the main function
    '''
    print("[=] enchilda starting up")
    enchilda_mainargs = getargs()
    pdf_count = 0
    delete_count = 0
    print("[+] enchilda getting args")
    print(f'[-] {enchilda_mainargs}')
    print("[+] enchilda walking through files")
    enchilda_filelist = walk_through(enchilda_mainargs)
    print(f'[-] {len(enchilda_filelist)} files found')
    for enchilda_file in tqdm(enchilda_filelist,
                              total=len(enchilda_filelist),
                              unit=' enchilda_file'):
        if os.path.splitext(enchilda_file)[1] == '.pdf':
            pdf_count += 1
        else:
            delete_count += 1
            os.remove(enchilda_file)
    print(f'[-] {pdf_count} pdf files found')
    print(f'[-] {delete_count} delete files found')
    print('[=] enchilda shutting down')


if __name__ == '__main__':
    main()
