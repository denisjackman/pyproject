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

TARGET_DIR = 'Z:'
PROJECT_FILE = 'Z:/Store/target/z_projectlist.xlsx'

def main():
    '''Main function'''
    print('[-] Main Function Starting...')
    writer = pd.ExcelWriter(PROJECT_FILE, engine='xlsxwriter') # pylint: disable=abstract-class-instantiated
    project_mainargs = {"verbosemode": False,
                        "deletemode": False,
                        "startdirectory": TARGET_DIR,
                        "targetdirectory": TARGET_DIR}
    project_filelist = walk_through(project_mainargs)
    final_filelist = sift_files(project_filelist, ['.csv', '.xlsx'])
    pdf_filelist = sift_files(project_filelist, ['.pdf'])
    doc_filelist = sift_files(project_filelist, ['.docx', '.doc'])
    write_to_excel(project_filelist, writer, 'all files')
    write_to_excel(final_filelist, writer, 'csv files')
    write_to_excel(pdf_filelist, writer, 'pdf files')
    write_to_excel(doc_filelist, writer, 'doc files')
    print(f'[-] {len(project_filelist)} files found')
    print(f'[-] {len(final_filelist)} excel files found')
    print(f'[-] {len(pdf_filelist)} pdf files found')
    print(f'[-] {len(doc_filelist)} word files found')
    print('[-] Main Function Finished.')
    writer.close()

def write_to_excel(writelist, writefile, writesheetname):
    '''Write to excel function'''
    print('[-] Write to Excel Function Starting...')
    df = pd.DataFrame(writelist)
    df.to_excel(writefile, sheet_name=writesheetname)
    print('[-] Write to Excel Function Finished.')

def sift_files(sift_list, search_list):
    '''Sift files function'''
    print('[-] Sift Files Function Starting...')
    result = []
    for item in sift_list:
        tempstr = os.path.splitext(item)[1]
        if tempstr in search_list:
            result.append(item)
    print('[-] Sift Files Function Finished.')
    return result

if __name__ == '__main__':
    print('[+] Project python script starting.')
    main()
    print('[+] Project python script completed.')
