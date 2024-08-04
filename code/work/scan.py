'''
    This is a scanner for environments.
    It is used to scan the environment and record the environment information.
'''
import os
import csv
import zipfile36 as zipfile
from tqdm import tqdm

SCAN_ZIP_DIRECTORY = 'z:/work/store'
SCAN_UNPACK_DIRECTORY = 'z:/work/store/unpack'
SCAN_DEBUG = False


def scan_walk_through(swt_command_args):
    """
    walk_through function:

        :param : swt_command_args - a list of the command arguments

        :return: a list of files that have been found

    This walks through a directory and returns the name and path of each file.
    It takes one param which is the starting point directory for the search.
    It returns nothing.
    It utilises check_file function to further check the file.
    """
    swt_start_dir = swt_command_args["startdirectory"]
    swt_verbose_mode = swt_command_args["verbosemode"]
    if swt_verbose_mode:
        print(f"[o] Starting walk through {swt_start_dir}")
    swt_result = []
    if swt_verbose_mode:
        print(f"[o] Searching for files in {swt_start_dir}")
    for root, _, files in os.walk(swt_start_dir, topdown=False):
        for name in tqdm(files,
                         total=len(files),
                         unit=' files'):
            swt_result.append(os.path.join(root, name))
    if swt_verbose_mode:
        print(f"[o] Finished walk through {swt_start_dir}")
    return swt_result


def scan_start():
    '''
        This function is used to start the scan.
    '''
    if SCAN_DEBUG:
        print('[+] Checking for unpack directory')
    if not os.path.exists(SCAN_UNPACK_DIRECTORY):
        if SCAN_DEBUG:
            print('[+] creating unpack directory')
        os.makedirs(SCAN_UNPACK_DIRECTORY)
    if SCAN_DEBUG:
        print('[+] Checking for zipfiles')
    ss_filelist = scan_walk_through({"verbosemode": SCAN_DEBUG,
                                    "startdirectory": SCAN_ZIP_DIRECTORY})
    for ss_item in ss_filelist:
        if ss_item.endswith('.zip'):
            scan_zip(ss_item)


def scan_zip(sz_filename):
    ''' unzip a file passed to us '''
    if SCAN_DEBUG:
        print(f'[+] unpacking {sz_filename}')
    with zipfile.ZipFile(sz_filename, 'r') as sz_zip_ref:
        sz_zip_ref.extractall(SCAN_UNPACK_DIRECTORY)
    if SCAN_DEBUG:
        print(f'[+] unpacked {sz_filename}')


def scan_process():
    ''' process the files in the unpack directory '''
    result = []
    sp_filelist = scan_walk_through({"verbosemode": SCAN_DEBUG,
                                    "startdirectory": SCAN_UNPACK_DIRECTORY})
    for sp_item in sp_filelist:
        if sp_item.find('tla_facts', 0) != -1:
            if sp_item.find('defaults.yml', 0) == -1:
                if sp_item.endswith('.yml'):
                    temp_str = sp_item.split('\\')
                    result.append({"Service": temp_str[1],
                                   "Environment": temp_str[3].split(".")[0]})
    return result


def main():
    '''
        This is the main function of the scanner.
    '''
    print('[-] Scanner Starting')
    print('[-] Scanner Startup')
    # scan_start()
    main_list = scan_process()
    fieldnames = ['Service', 'Environment']
    with open(f'{SCAN_ZIP_DIRECTORY}/environments.csv',
              'w',
              newline='',
              encoding='utf-8-sig') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(main_list)
    print('[-] Scanner is done.')


if __name__ == '__main__':
    main()
