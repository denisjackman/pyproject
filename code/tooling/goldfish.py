''' This is a find files utility'''
import os
import sys
import datetime
from tqdm import tqdm
# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.utilities.fileutility import walk_through
from jackmanimation.utilities.fileutility import getargs

SEARCH_LIST = [".DS_Store",
               ".AppleDouble",
               "Thumbs.db",
               ".pydevproject"]


def main():
    ''' main '''
    gf_now = datetime.datetime.now()
    gf_date = f'{gf_now.year}{gf_now.month}{gf_now.day}'
    gf_files = []
    gf_filename = f'T:goldfish_{gf_date}.txt'
    delete_filename = f'T:goldfish_delete_{gf_date}.txt'
    delete_files = []
    print('[*] goldfish main starting up')

    if 'Thumbs.db' in SEARCH_LIST:
        print('[-] Thumbs.db found')

    print('[-] goldfish main getting args')
    goldfish_command_args = getargs()
    print('[-] goldfish main walking through files')
    goldfish_filelist = walk_through(goldfish_command_args)
    print(f'[-] {len(goldfish_filelist)} files found')
    for goldfish_file in tqdm(goldfish_filelist,
                              total=len(goldfish_filelist),
                              unit=' goldfish_file'):
        if os.path.basename(goldfish_file) in SEARCH_LIST:
            delete_files.append(goldfish_file)
        if os.path.splitext(goldfish_file)[1] == ".pdf":
            gf_files.append(goldfish_file)
    print(f'[-] {len(gf_files)} pdf files found')
    print(f'[-] {len(delete_files)} delete files found')

    with open(gf_filename,
              'w',
              encoding='utf-8-sig') as goldfishfile:
        print('[-] goldfish main walking through files')
        for gf_file in tqdm(gf_files,
                            total=len(gf_files),
                            unit=' gf_file'):
            goldfishfile.write(f'{gf_date},{gf_file}\n')

    with open(delete_filename,
              'w',
              encoding='utf-8-sig') as deletefile:
        print('[-] goldfish main walking through files')
        for delete_file in tqdm(delete_files,
                                total=len(delete_files),
                                unit=' delete_file'):
            deletefile.write(f'{gf_date},{delete_file}\n')

    print('[*] goldfish main shutting down')


if __name__ == "__main__":
    print('[+] goldfish starting up')
    main()
    print('[+] goldfish shutting down')
