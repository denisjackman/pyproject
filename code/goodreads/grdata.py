''' Good reads data fixer'''
import csv
import pandas as pd

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

def main():
    ''' This is the main function'''
    print('[*] This is the main function starting')
    # Variables
    new_list = []
    record = {}
    count = 0
    # Load the csv files
    input_csv_file = csv_file_reader(DATA_FILE)
    sample_csv_file = csv_file_reader(SAMPLE_FILE)
    books_list = csv_file_reader(BOOKS_FILE)

    print(f'[*] This is the input_csv_file length: {len(input_csv_file)}')
    print(f'[*] This is the sample_csv_file length: {len(sample_csv_file)}')
    print(f'[*] This is the books_list length: {len(books_list)}')
    for item in input_csv_file:
        title = item['Title']
        author = item['Author']
        isbn = item['ISBN']
        if item['My Rating'] == '0':
            count = +1
            my_rating = item['Average Rating']
        else:
            my_rating = item['My Rating']
        publisher = item['Publisher']
        binding = item['Binding']
        year_published = item['Year Published']
        original_publication_year = item['Original Publication Year']
        if item['Date Read'] == '':
            date_read = item['Date Added']
        else:
            date_read = item['Date Read']
        date_added = item['Date Added']
        bookshelves = item['Bookshelves']
        my_review = item['My Review']
        record = {'Title': title,
                  'Author': author, 
                  'ISBN': isbn,
                  'My Rating': my_rating,
                  'Average Rating': my_rating,
                  'Publisher': publisher,
                  'Binding': binding,
                  'Year Published': year_published,
                  'Original Publication Year': original_publication_year,
                  'Date Read': date_read,
                  'Date Added': date_added,
                  'Bookshelves': bookshelves,
                  'My Review': my_review}
        new_list.append(record)
    for item in books_list:
        title = item['Title']
        author = item['Author']
        isbn = 'ISBN'
        my_rating = 5
        publisher = ''
        binding = ''
        year_published = ''
        original_publication_year = ''
        date_read = f'01/02/{item["Year"]}'
        date_added = date_read
        bookshelves = ''
        my_review = ''
        record = {'Title': title,
                'Author': author, 
                'ISBN': isbn,
                'My Rating': my_rating,
                'Average Rating': my_rating,
                'Publisher': publisher,
                'Binding': binding,
                'Year Published': year_published,
                'Original Publication Year': original_publication_year,
                'Date Read': date_read,
                'Date Added': date_added,
                'Bookshelves': bookshelves,
                'My Review': my_review}
        new_list.append(record)
    print(f'[*] This is the new_list length: {len(new_list)}')
    print(f'[*] This is the count: {count}')
    df = pd.DataFrame(new_list)
    df.to_csv(OUTPUT_FILE, index=False)
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
