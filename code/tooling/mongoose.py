''' mongoose tool '''
import os
import sys
import zipfile36 as zipfile
import rarfile
from tqdm import tqdm

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.utilities.fileutility import walk_through
from jackmanimation.utilities.fileutility import getargs


def unzip(zipfile_path, unzip_path, unzip_verbose=False):
    '''unzip'''
    if unzip_verbose:
        print(f'[-] unzip {zipfile_path} to {unzip_path}')
    with zipfile.ZipFile(zipfile_path, 'r') as zip_ref:
        zip_ref.extractall(unzip_path)


def unrar(rarfile_path, unrar_path, unrar_verbose=False):
    '''unrar'''
    rarfile__err_count = 0
    if unrar_verbose:
        print(f'[-] unrar {rarfile_path} to {unrar_path}')
    try:
        with rarfile.RarFile(rarfile_path) as rar_ref:
            rar_ref.extractall(unrar_path)
    except rarfile.RarCannotExec:
        rarfile__err_count += 1
    except rarfile.NeedFirstVolume:
        rarfile__err_count += 1


def main():
    '''main function'''
    print('[-] mongoose tool main starting')
    print('[+] mongoose tool getting args')
    mongoose_mainargs = getargs()
    if mongoose_mainargs["verbosemode"]:
        print(f'[-] {mongoose_mainargs}')
    mongoose_filelist = walk_through(mongoose_mainargs)
    if mongoose_mainargs["verbosemode"]:
        print(f'[-] {len(mongoose_filelist)} files found')
    for mongoose_file in tqdm(mongoose_filelist,
                              total=len(mongoose_filelist),
                              unit=' mongoose_file'):
        if os.path.splitext(mongoose_file)[1] == '.zip':
            unzip(mongoose_file,
                  mongoose_mainargs["targetdirectory"],
                  mongoose_mainargs["verbosemode"])
        if os.path.splitext(mongoose_file)[1] == '.rar':
            unrar(mongoose_file,
                  "Y:\\playspace\\library",
                  mongoose_mainargs["verbosemode"])

    print('[-] mongoose tool main finished')


if __name__ == '__main__':
    print('[=] mongoose tool starting')
    main()
    print('[=] mongoose tool finished')
