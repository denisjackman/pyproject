''' Pictures module for Jackmanimation project'''
import os
import sys

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.utilities.fileutility import walk_through

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.00 $"
__date__ = "$Date: 2024/01/22 12:48:00 $"
__copyright__ = "Copyright (c) 2024 Denis J Jackman"
__license__ = "Python"
TARGET_DIR = 'X:/Pictures/'
PROJECT_FILE = 'Z:/Store/target/picturelist'


def main():
    '''Main function'''
    print('[-] Main Function Starting...')
    picture_mainargs = {"verbosemode": False,
                        "deletemode": False,
                        "startdirectory": TARGET_DIR,
                        "targetdirectory": TARGET_DIR}
    picture_filelist = walk_through(picture_mainargs)
    jpg_filelist = picture_sift_files_ext(picture_filelist, ['.jpg',
                                                             '.jpeg',
                                                             '.png',
                                                             '.gif'])
    aae_filelist = picture_sift_files_ext(picture_filelist, ['.aae',
                                                             '.heic',
                                                             '.db',
                                                             '.webp'])
    mov_filelist = picture_sift_files_ext(picture_filelist, ['.mov',
                                                             '.mp4',
                                                             '.avi'])
    copy_filelist = picture_sift_files(picture_filelist, ['Copy'])
    type_list = pictures_get_types(picture_filelist)
    print(f'[*] {len(picture_filelist)} files found')
    print(f'[*] {len(type_list)} file extension files found')
    print(f'[*] {type_list} types found')
    print(f'[*] {len(jpg_filelist)} JPG files found')
    print(f'[*] {len(aae_filelist)} AAE files found')
    print(f'[*] {len(mov_filelist)} MOV files found')
    print(f'[*] {len(copy_filelist)} Copy files found')
    for item in aae_filelist:
        print(f'\t[=] {item}')
        pictures_remove_file(item, True, True)
    for item in copy_filelist:
        print(f'\t[#] {item}')
        pictures_remove_file(item, True, True)
    print('[-] Main Function Finished.')


def pictures_remove_file(picture_remove_file,
                         verbose_mode=False,
                         delete_mode=False):
    '''Remove file function'''
    if verbose_mode:
        print('[-] Remove File Function Starting...')
    if delete_mode:
        if verbose_mode:
            print(f'[-] Removing {picture_remove_file}')
        if os.path.exists(picture_remove_file):
            try:
                os.remove(picture_remove_file)
            except OSError as error:
                print(f'[-] Error: {error}')
    if verbose_mode:
        print('[-] Remove File Function Finished.')


def pictures_get_types(picture_seach_list):
    '''Get types function'''
    result = []
    for item in picture_seach_list:
        tempstr = os.path.splitext(item)[1]
        if tempstr.lower() not in result:
            result.append(tempstr.lower())
    return result


def picture_sift_files_ext(picture_sift_list, picture_search_list):
    '''Sift files function'''
    print('[+] Sift Files Function Starting...')
    result = []
    for item in picture_sift_list:
        tempstr = os.path.splitext(item)[1]
        if tempstr.lower() in picture_search_list:
            result.append(item)
    print('[+] Sift Files Function Finished.')
    return result


def picture_sift_files(picture_sift_list, picture_search_list):
    '''Sift files function'''
    print('[+] Sift Files Function Starting...')
    result = []
    for item in picture_sift_list:
        tempstr = os.path.splitext(item)[0]
        for search_item in picture_search_list:
            if search_item.lower() in tempstr.lower():
                result.append(item)
    print('[+] Sift Files Function Finished.')
    return result


if __name__ == '__main__':
    main()
