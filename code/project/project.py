'''Project python script'''
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

TARGET_DIR = 'G:'
TARGET_FILE = 'Z:/Store/target/filelist.xlsx'
PROJECT_FILE = 'Z:/Store/target/projectlist.xlsx'

def main():
    '''Main function'''
    print('[-] Main Function Starting...')
    project_mainargs = {"verbosemode": False,
                        "deletemode": False,
                        "startdirectory": TARGET_DIR,
                        "targetdirectory": TARGET_DIR}
    project_filelist = walk_through(project_mainargs)
    print(f'[-] {len(project_filelist)} files found')
    df = pd.DataFrame(project_filelist)
    writer = pd.ExcelWriter(PROJECT_FILE, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='all files')
    final_filelist = sift_files(project_filelist)
    print(f'[-] {len(final_filelist)} files found')
    df = pd.DataFrame(final_filelist)
    df.to_excel(writer, sheet_name='xl files')
    writer.close()
    print('[-] Main Function Finished.')

def sift_files(sift_list):
    '''Sift files function'''
    print('[-] Sift Files Function Starting...')
    result = []
    for item in sift_list:
        if item.endswith('.csv') or item.endswith('.xlsx'):
            result.append(item)
    print('[-] Sift Files Function Finished.')
    return result
  
if __name__ == '__main__':
    print('[+] Project python script starting.')
    main()
    print('[+] Project python script completed.')
