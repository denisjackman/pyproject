'''
armadillo.py

This is a os utility tool

'''
import os
import sys
import zipfile36 as zipfile

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.utilities.fileutility import walk_through
from jackmanimation.utilities.fileutility import getargs

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.01 $"
__date__ = "$Date: 2022/07/28 01:17:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"

ARMA_TARGET_DIR = 't:'


def main():
    '''
        this is the main function
    '''
    print("[=] armadillo starting up")
    arma_mainargs = getargs()
    print("[+] armadillo getting args")
    print(f'[-] {arma_mainargs}')
    print("[+] armadillo walking through files")
    arma_filelist = walk_through(arma_mainargs)
    print(f'[-] {len(arma_filelist)} files found')
    for arma_file in arma_filelist:
        try:
            with zipfile.ZipFile(arma_file) as archive:
                archive.extractall(path=ARMA_TARGET_DIR)
        except:  # pylint: disable=bare-except
            continue
    print('[=] armadillo shutting down')


if __name__ == '__main__':
    main()
