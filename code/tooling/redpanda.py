'''
redpanda.py

This is a os utility tool

Which takes all the files in one directory and renames them into another directory

'''
import os
import sys

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.utilities.fileutility import walk_through

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.01 $"
__date__ = "$Date: 2022/07/28 01:17:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"

RP_TARGET_DIR = 'Z:/Chatgpt/store'
RP_SOURCE_DIR = 'C:/Users/denis/Downloads'
RP_NAME = 'chatgpt-20241223-'


def main():
    '''
        this is the main function
    '''
    rp_mainargs = {"verbosemode": False,
                   "deletemode": False,
                   "startdirectory": RP_SOURCE_DIR}
    print("[=] red panda starting up")
    print("[+] red panda walking through files")
    rp_filelist = walk_through(rp_mainargs)
    print(f'[-] {len(rp_filelist)} files found')
    count = 1
    for rp_file in rp_filelist:
        rp_ext = os.path.splitext(rp_file)
        if rp_ext[1] != '.ini':
            rp_new_file = f'{RP_SOURCE_DIR}/{RP_NAME}{count:0>{3}}{rp_ext[1]}'
            print(rp_new_file)
            os.replace(rp_file, rp_new_file)
        count += 1

    print('[=] red panda shutting down')


if __name__ == '__main__':
    main()
