''' Good reads data fixer'''
import csv
import pandas as pd
import isbntools.app as isbn_app

DATA_FILE = 'X:/goodreads_library_export.csv'
SAMPLE_FILE = 'X:/sample_export.csv'
OUTPUT_FILE = 'X:/goodreads_DJ_fixed.csv'
BOOKS_FILE = 'X:/books.csv'

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
def write_item_list(item_list):
    ''' This is the write item list function'''
    print('[*] This is the write item list function starting')
    result = []
    for item in item_list:
        if item['My Rating'] == '0':
            count = +1
            my_rating = item['Average Rating']
        else:
            my_rating = item['My Rating']
        if item['Date Read'] == '':
            date_read = item['Date Added']
        else:
            date_read = item['Date Read']
        record = {'Title': item["Title"],
                  'Author': item['Author'], 
                  'ISBN': item['ISBN'],
                  'My Rating': item['ISBN'],
                  'Average Rating': my_rating,
                  'Publisher': item['Publisher'],
                  'Binding': item['Binding'],
                  'Year Published': item['Year Published'],
                  'Original Publication Year': item['Original Publication Year'],
                  'Date Read': date_read,
                  'Date Added': item['Date Added'],
                  'Bookshelves': item['Bookshelves'],
                  'My Review': item['My Review']}
        result.append(record)
    print('[*] This is the write item list function ending')
    return result

def main():
    ''' This is the main function'''
    print('[*] This is the main function starting')
    # Variables
    new_list = []
    save_list = []
    record = {}
    count = 0
    save_count = 0
    # Load the csv files
    input_csv_file = csv_file_reader(DATA_FILE)
    sample_csv_file = csv_file_reader(SAMPLE_FILE)
    books_list = csv_file_reader(BOOKS_FILE)

    print(f'[*] This is the input_csv_file length: {len(input_csv_file)}')
    print(f'[*] This is the sample_csv_file length: {len(sample_csv_file)}')
    print(f'[*] This is the books_list length: {len(books_list)}')
    found_count = 0
    for item in books_list:
        found = False
        for lookup in input_csv_file:
            if item['Title'] == lookup['Title']:
                found = True
                found_count += 1
                break
        if found:
            print(f'[*] This is in the lookup: {item["Title"], lookup["ISBN"]}')

    new_list = write_item_list(input_csv_file)
    for item in books_list:
        date_read = f'01/02/{item["Year"]}'
        isbn_number = isbn_app.isbn_from_words(item['Title'])
        record = {'Title': item['Title'],
                'Author': item['Author'], 
                'ISBN': isbn_number,
                'My Rating': 5,
                'Average Rating': 5,
                'Publisher': '',
                'Binding': '',
                'Year Published': '',
                'Original Publication Year': '',
                'Date Read': date_read,
                'Date Added': date_read,
                'Bookshelves': '',
                'My Review': ''}
        new_list.append(record)
    print(f'[*] This is the new_list length: {len(new_list)}')
    print(f'[*] This is the found_count: {found_count}')
    for item in new_list:
        if item['ISBN'] == '':
            save_count += 1
        else:
            save_list.append(item)
            
    df = pd.DataFrame(save_list)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f'[*] This is the count: {count}')
    print(f'[*] This is the saved count: {save_count}')
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
