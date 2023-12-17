''' Good reads data fixer'''
import csv
import pandas as pd

DATA_FILE = 'X:/goodreads_library_export.csv'
SAMPLE_FILE = 'X:/sample_export.csv'
OUTPUT_FILE = 'X:/goodreads_DJ_fixed.csv'

def main():
    ''' This is the main function'''
    print('[*] This is the main function starting')
    input_csv_file = csv_file_reader(DATA_FILE)
    sample_csv_file = csv_file_reader(SAMPLE_FILE)

    print('[*] This is the main function ending')

def csv_file_reader(csv_data_file):
    ''' This is the csv file reader function'''
    print('[*] This is the csv file reader function starting')
    result = pd.read_csv(csv_data_file)
    csv_reader = result.to_dict(orient='records')
    return csv_reader

def csv_file_writer(dict_data, csv_file_name):
    ''' This is the csv file writer function'''
    print('[*] This is the csv file writer function starting')
    with open(csv_file_name, 'w', encoding='utf-8-sig') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=dict_data.keys())
        writer.writeheader()
        writer.writerow(dict_data)
    print('[*] This is the csv file writer function ending')

if __name__ == '__main__':
    print('[+] This is the goodreads program starting')
    main()
    print('[+] This is the goodreads program ending')
