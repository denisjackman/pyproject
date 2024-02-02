import os
import sys
import pandas as pd

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
                        "targetdirectory": TARGET_DIR,}
    picture_filelist = walk_through(picture_mainargs)
    jpg_filelist = picture_sift_files(picture_filelist, ['.jpg', '.jpeg', '.png','.gif'])
    aae_filelist = picture_sift_files(picture_filelist, ['.aae','.heic','.db','.webp'])
    mov_filelist = picture_sift_files(picture_filelist, ['.mov','.mp4','.avi'])
    type_list = pictures_get_types(picture_filelist)
    print(f'[*] {len(picture_filelist)} files found')
    print(f'[*] {len(type_list)} file extension files found')
    print(f'[*] {type_list} types found')
    print(f'[*] {len(jpg_filelist)} JPG files found')
    print(f'[*] {len(aae_filelist)} AAE files found')
    print(f'[*] {len(mov_filelist)} MOV files found')
    
    print('[-] Main Function Finished.')

def pictures_get_types(picture_seach_list):
    '''Get types function'''
    result = []
    for item in picture_seach_list:
        tempstr = os.path.splitext(item)[1]
        if tempstr.lower() not in result:
            result.append(tempstr.lower())
    return result

def picture_sift_files(picture_sift_list, picture_search_list):
    '''Sift files function'''
    print('[+] Sift Files Function Starting...')
    result = []
    for item in picture_sift_list:
        tempstr = os.path.splitext(item)[1]
        if tempstr.lower() in picture_search_list:
            result.append(item)
    print('[+] Sift Files Function Finished.')
    return result

if __name__ == '__main__':
    main()