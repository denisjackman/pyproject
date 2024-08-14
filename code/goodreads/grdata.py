''' Good reads data fixer'''
import time
import pandas as pd
import isbntools.app as isbn_app

DATA_FILE = 'Z:/Store/goodreads_library_export.csv'
OUTPUT_FILE = 'Z:/Store/goodreads_DJ_new_fixed.csv'
BOOKS_FILE = 'Z:/Store/books.csv'
NOT_FOUND = 'Z:/Store/notfound.csv'


def write_item_list(item_list):
    ''' This is the write item list function'''
    print('[o] This is the write item list function starting')
    result = []
    for item in item_list:
        record = {'Title': item["Title"],
                  'Author': item['Author'],
                  'ISBN': item['ISBN'],
                  'My Rating': 5,
                  'Average Rating': item['Average Rating'],
                  'Publisher': item['Publisher'],
                  'Binding': item['Binding'],
                  'Year Published': item['Year Published'],
                  'Original Publication Year': item['Original Publication Year'],
                  'Date Read': item['Date Added'],
                  'Date Added': item['Date Added'],
                  'Bookshelves': item['Bookshelves'],
                  'My Review': item['My Review']}
        result.append(record)
    print('[o] This is the write item list function ending')
    return result


def convert_books(cbbooks_list):
    ''' This is the convert books function'''
    print('[o] This is the convert books function starting')
    result = []
    for item in cbbooks_list:
        date_read = f'01/02/{item["Year"]}'
        isbn_number = ''

        try:
            isbn_number = isbn_app.isbn_from_words(item['Title'])
        except Exception as my_error:
            isbn_number = ''
            time.sleep(30)

        record = {'Title': item['Title'],
                  'Author': item['Author'],
                  'ISBN': f'{isbn_number}',
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
        result.append(record)
    print('[o] This is the convert books function ending')
    return result


def csv_file_reader(csv_data_file):
    ''' This is the csv file reader function'''
    print('[o] This is the csv file reader function starting')
    result = pd.read_csv(csv_data_file)
    csv_reader = result.to_dict(orient='records')
    print('[o] This is the csv file reader function ending')
    return csv_reader


def csv_file_writer(write_list, csv_file_name):
    ''' This is the csv file writer function'''
    print('[o] This is the csv file writer function starting')
    df = pd.DataFrame(write_list)
    df.to_csv(csv_file_name, index=False)
    print('[o] This is the csv file writer function ending')


def main():
    ''' This is the main function'''
    print('[-] This is the main function starting')
    # Variables
    new_list = []
    # old_list = []
    save_list = []
    # record = {}
    count = 0
    save_count = 0
    book_meta = ''

    # Load the csv files
    input_csv_file = csv_file_reader(DATA_FILE)
    notfound_file = csv_file_reader(NOT_FOUND)
    books_list = csv_file_reader(BOOKS_FILE)

    # old_list = write_item_list(input_csv_file)
    new_list = convert_books(books_list)

    for item in new_list:
        if item['ISBN'] == '':
            save_count += 1
        else:
            save_list.append(item)

    try:
        book_meta = isbn_app.meta(notfound_file[0]['ISBN'])
    except Exception as my_error:
        print(f'[-] This is the error: {my_error} for {notfound_file[0]["ISBN"]}')
        book_meta = 'not found'
        time.sleep(30)

    csv_file_writer(save_list, OUTPUT_FILE)

    print(f'[-] This is the count: {count}')
    print(f'[-] This is the saved count: {save_count}')
    print(f'[-] This is the input_csv_file length: {len(input_csv_file)}')
    print(f'[-] This is the notfound_file length: {len(notfound_file)}')
    print(f'[-] This is the books_list length: {len(books_list)}')
    print(f'[-] This is the new_list length: {len(new_list)}')
    print(f'[-] This is the save_list length: {len(save_list)}\n\n')
    print(f'[-] This is the book_meta: {book_meta}\n\n')
    print('[-] This is the main function ending')


if __name__ == '__main__':
    print('[+] This is the goodreads program starting')
    main()
    print('[+] This is the goodreads program ending')
