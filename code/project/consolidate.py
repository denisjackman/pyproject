''' this is a file consolidation script'''
import os
import sys
import pandas as pd

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.utilities.fileutility import walk_through

CONSOLIDATE_DIR = 'Z:/Store/target/'


def main():
    '''Main function'''
    print('[+] Main Function Starting...')
    consolidate_files()
    print('[+] Main Function Finished.')


def consolidate_files():
    '''Consolidate files function'''
    print('[-] Consolidate Files Function Starting...')
    cf_mainargs = {"verbosemode": False,
                   "deletemode": False,
                   "startdirectory": CONSOLIDATE_DIR,
                   "targetdirectory": CONSOLIDATE_DIR}
    cf_filelist = walk_through(cf_mainargs)
    cf_full = []
    cf_csv = []
    cf_doc = []
    cf_pdf = []
    for item in cf_filelist:
        if '_csv.csv' in item:
            cf_csv.append(item)
        if '_pdf.csv' in item:
            cf_pdf.append(item)
        if '_doc.csv' in item:
            cf_doc.append(item)
        if '_full.csv' in item:
            cf_full.append(item)

    cf_write_to_csv(cf_pdf, f'{CONSOLIDATE_DIR}fulllist_pdf.csv')
    cf_write_to_csv(cf_doc, f'{CONSOLIDATE_DIR}fulllist_doc.csv')
    cf_write_to_csv(cf_csv, f'{CONSOLIDATE_DIR}fulllist_csv.csv')
    cf_write_to_csv(cf_full, f'{CONSOLIDATE_DIR}fullist_full.csv')
    print('[-] Consolidate Files Function Finished.')


def cf_write_to_csv(cf_writelist, cf_writefile):
    '''Write to csv function'''
    print('[-] Write to CSV Function Starting...')
    df = pd.concat(
        [pd.read_csv(f) for f in cf_writelist],
        ignore_index=True)
    df.to_csv(cf_writefile, encoding='utf-8', index=False)
    print('[-] Write to CSV Function Finished.')


if __name__ == '__main__':
    main()
