#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
pangolin.py

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

PANGOLIN_TARGET_DIR = 't:'

def validate_file_contents(vfc_file1, vfc_file2):
    ''' validate_file_contents '''
    try:
        with open(vfc_file1, 'rb') as vfc_f1, open(vfc_file2, 'rb') as vfc_f2:
            vfc_contents1 = vfc_f1.read()
            vfc_contents2 = vfc_f2.read()
    except: # pylint: disable=bare-except
        return False

    return vfc_contents1 == vfc_contents2

def main():
    '''
        this is the main function
    '''
    print("[=] pangolin starting up")
    pango_mainargs = getargs()
    print("[+] pangolin getting args")
    print(f'[-] {pango_mainargs}')
    print("[+] pangolin walking through files")
    pango_filelist = walk_through(pango_mainargs)
    compare_list = pango_filelist
    print(f'[-] {len(pango_filelist)} files found')
    print("[+] pangolin validating files")

    duplicate_count = 0
    list_store = compare_list
    for item in tqdm(pango_filelist, total=len(pango_filelist), unit=' item'):
        for pango_file in tqdm(compare_list, total=len(compare_list), unit=' item'):
            if pango_file != item:
                if validate_file_contents(pango_file, item):
                    #print(f'[-] {pango_file} is a duplicate of {item}')
                    list_store.remove(pango_file)
                    duplicate_count += 1
        compare_list = list_store

    print(f'[-] {duplicate_count} duplicates found')
    print(f'[-] {len(compare_list)} unique files found')
    print('[=] pangolin shutting down')

if __name__ == '__main__':
    main()
