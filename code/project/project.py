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

TARGET_DIR_LIST = ['Y:/', 'Z:/', 'X:/', 'C:/']
PROJECT_FILE = 'Z:/Store/target/projectlist'

def main():
    '''Main function'''
    print('[-] Main Function Starting...')
    for item in TARGET_DIR_LIST:
        process_files(item)
    process_files(TARGET_DIR_LIST[0])
    print('[-] Main Function Finished.')

def process_files(pf_target):
    '''Process files function'''
    print('[-] Process Files Function Starting...')
    pf_target_name = f'{PROJECT_FILE}_{pf_target[0]}'
    print(f'[-] Target Directory: {pf_target_name}')
    #writer = pd.ExcelWriter(f'{pf_target_name}.xlsx', engine='xlsxwriter') # pylint: disable=abstract-class-instantiated
    project_mainargs = {"verbosemode": False,
                        "deletemode": False,
                        "startdirectory": pf_target,
                        "targetdirectory": pf_target,}
    project_filelist = walk_through(project_mainargs)
    final_filelist = sift_files(project_filelist, ['.csv', '.xlsx'])
    pdf_filelist = sift_files(project_filelist, ['.pdf'])
    doc_filelist = sift_files(project_filelist, ['.docx', '.doc'])
    write_to_csv(project_filelist, f'{pf_target_name}_full.csv')
    write_to_csv(final_filelist, f'{pf_target_name}_csv.csv')
    write_to_csv(pdf_filelist, f'{pf_target_name}_pdf.csv')
    write_to_csv(doc_filelist, f'{pf_target_name}_doc.csv')
    print(f'[-] {len(project_filelist)} files found')
    print(f'[-] {len(final_filelist)} excel files found')
    print(f'[-] {len(pdf_filelist)} pdf files found')
    print(f'[-] {len(doc_filelist)} word files found')
    #writer.close()
    print('[-] Process Files Function Finished.')

def write_to_excel(writelist, writefile, writesheetname):
    '''Write to excel function'''
    print('[-] Write to Excel Function Starting...')
    df = pd.DataFrame(writelist)
    df.to_excel(writefile, sheet_name=writesheetname, index=False)
    print('[-] Write to Excel Function Finished.')

def write_to_csv(writelist, writefile):
    '''Write to csv function'''
    print('[-] Write to CSV Function Starting...')
    df = pd.DataFrame(writelist)
    df.to_csv(writefile,  encoding='utf-8',index=False)
    print('[-] Write to CSV Function Finished.')

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