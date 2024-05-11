''' core refresh search module '''
# import sys
# import getopt
import csv

FILENAME = "C:/Users/Denis/Downloads/CMDB Wiki Pages.csv"
CONFLUENCE = 'https://confluence.app.betfair/display/'


def cmdb_read_csv_file(crcf_filename):
    ''' read csv file '''
    crcf_result = []
    with open(crcf_filename,
              'r',
              encoding='utf-8-sig') as crcf_csvfile:
        crcf_data = csv.reader(crcf_csvfile, delimiter=',')
        for row in crcf_data:
            crcf_result.append(row)
    return crcf_result


def main():
    ''' main function '''
    print('[-] cmdb_remap started')
    main_tlalist = cmdb_read_csv_file(FILENAME)
    count = 0
    for main_item in main_tlalist:
        if CONFLUENCE in main_item[2]:
            count += 1
            print(main_item[2])
    print(f'Total entries: {count} {len(main_tlalist)}')
    print('[-] cmdb_remap finished')


if __name__ == '__main__':
    main()
