''' Good reads data fixer'''
import csv
import pandas as pd

DATA_FILE = 'X:/goodreads_library_export.csv'
SAMPLE_FILE = 'X:/sample_export.csv'
OUTPUT_FILE = 'X:/goodreads_DJ_fixed.csv'

# title
# author
# isbn
# My Rating = if 0 then use Average Rating
# Average Rating
# Publisher
# Binding
# Year Published
# Original Publication Year
# Date Read if none should be year added 
# Date Added
# Shelves
# Bookshelves
# My Review

def main():
    ''' This is the main function'''
    print('[*] This is the main function starting')
    input_csv_file = csv_file_reader(DATA_FILE)
    sample_csv_file = csv_file_reader(SAMPLE_FILE)
    count = 0
    print(f'[*] This is the input_csv_file length: {len(input_csv_file)}')
    print(f'[*] This is the sample_csv_file length: {len(sample_csv_file)}')
    for item in input_csv_file:
        if item['My Rating'] == '0':
            count = +1
    print(f'[*] This is the count: {count}')
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
