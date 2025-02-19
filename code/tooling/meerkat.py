'''
meerkat.py

This is a os utility tool

'''
import os
import sys
# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.utilities.fileutility import walk_through
from jackmanimation.utilities.fileutility import getargs

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.01 $"
__date__ = "$Date: 2022/07/28 01:17:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"

TARGET_DIR = 't:'


def main():
    '''
        this is the main function
    '''
    print("[=] meerkat starting up")
    newlist = []
    mainargs = getargs()
    print("[+] meerkat getting args")
    print(f'[-] {mainargs}')
    print("[+] meerkat walking through files")
    filelist = walk_through(mainargs)
    print(f'[-] {len(filelist)} files found')
    print(f'[-] {filelist[0]}')
    for file in filelist:
        if file.endswith('.jpg') or file.endswith('.png'):
            newlist.append(file)
    print(f'[-] {len(newlist)} images found')
    print(f'[-] {newlist[0]}')
    print('[=] meerkat shutting down')


if __name__ == '__main__':
    main()
