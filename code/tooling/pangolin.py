#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
pangolin.py

This is a os utility tool

'''
import os
import sys
import hashlib
from tqdm import tqdm
# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
#from jackmanimation.utilities.fileutility import walk_through
from jackmanimation.utilities.fileutility import getargs

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.01 $"
__date__ = "$Date: 2022/07/28 01:17:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"

PANGOLIN_TARGET_DIR = 'G:/Duplicates/'

def find_duplicate_files(directory_path):
    """Steps through a directory of files and compares each file to find duplicates and delete the duplicates.

    Args:
    directory_path (str): The path to the directory to scan for duplicates.
    """

    # Create a dictionary to store the hashes of the files.
    file_hashes = {}
    count = 0
    file_count = 0
    # Iterate through all the files in the directory.
    print('[*] find_duplicate_file starting up')
    print(f'[-] {directory_path}')
    print(f'[-] {PANGOLIN_TARGET_DIR}')
    print('[-] find_duplicate_file walking through files')
    for root, directories, files in os.walk(directory_path):
        for item_file in tqdm(files, total=len(files), unit=' item_file'):        
            file_count += 1
            # Calculate the hash of the file.
            file_path = os.path.join(root, item_file)
            try:
                file_hash = hashlib.md5(open(file_path, "rb").read()).hexdigest() #pylint: disable=consider-using-with
            except OSError:
                print(f'[-] {file_path} already exists in {PANGOLIN_TARGET_DIR}')

            # If the hash is already in the dictionary, the file is a duplicate.
            if file_hash in file_hashes:
                print(f'[0] Duplicate found: {file_path} {file_hashes[file_hash]}')
                count += 1
                # file name with extension
                file_name = os.path.basename(file_path)
                new_target = os.path.join(PANGOLIN_TARGET_DIR, file_name)
                try:
                    os.rename(file_path, new_target)
                except WindowsError:
                    os.remove(new_target)
                    os.rename(file_path, new_target)
            else:
                file_hashes[file_hash] = file_path
    print(f'[-] {count} duplicates found')
    print(f'[-] {file_count} files found')
    print('[*] find_duplicate_file completed')

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
    find_duplicate_files(pango_mainargs["startdirectory"])
#    print("[+] pangolin walking through files")
#    pango_filelist = walk_through(pango_mainargs)
#    compare_list = pango_filelist
#    print(f'[-] {len(pango_filelist)} files found')
#    print("[+] pangolin validating files")
#    total_duplicates = 0
#    loop_count = 0
#    for item in tqdm(pango_filelist, total=len(pango_filelist), unit=' item'):
#        duplicate_count = 0
#        list_store = compare_list
#        for pango_file in tqdm(compare_list, total=len(compare_list), unit=' item'):
#            if pango_file != item:
#                if validate_file_contents(pango_file, item):
#                    list_store.remove(pango_file)
#                    duplicate_count += 1
#                    total_duplicates += 1
#        if duplicate_count == 0:
#            break
#        compare_list = list_store
#
#    print(f'[-] {loop_count} iterations')
#    print(f'[-] {total_duplicates} duplicates found')
#    print(f'[-] {len(compare_list)} unique files found')
    print('[=] pangolin shutting down')

if __name__ == '__main__':
    main()
