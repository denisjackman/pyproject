#!/usr/bin/python
# -*- coding: utf-8 -*-
''' mongoose tool '''
import os
import sys
import zipfile36 as zipfile
import rarfile

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.utilities.fileutility import walk_through
from jackmanimation.utilities.fileutility import getargs

def unzip(zipfile_path, unzip_path):
    '''unzip'''
    print(f'[-] unzip {zipfile_path} to {unzip_path}')
    with zipfile.ZipFile(zipfile_path, 'r') as zip_ref:
        zip_ref.extractall(unzip_path)

def unrar(rarfile_path, unrar_path):
    '''unrar'''
    print(f'[-] unrar {rarfile_path} to {unrar_path}')
    with rarfile.RarFile(rarfile_path) as rar_ref:
        rar_ref.extractall(unrar_path)

def main():
    '''main function'''
    print('[-] mongoose tool main starting')
    print('[+] mongoose tool getting args')
    mongoose_mainargs = getargs()
    if mongoose_mainargs["verbosemode"]:
        print(f'[-] {mongoose_mainargs}')
    moongoose_filelist = walk_through(mongoose_mainargs)
    if mongoose_mainargs["verbosemode"]:
        print(f'[-] {len(moongoose_filelist)} files found')
    for mongoose_file in moongoose_filelist:
        print(f'[-] {mongoose_file}')
        if os.path.splitext(mongoose_file)[1] == '.zip':
            unzip(mongoose_file, mongoose_mainargs["targetdirectory"])
    print('[-] mongoose tool main finished')

if __name__ == '__main__':
    print('[=] mongoose tool starting')
    main()
    print('[=] mongoose tool finished')
