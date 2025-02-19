'''
this is a script to sift a goodreads csv file for books

'''
import csv
import json
import pandas as pd

DATAFILE = 'Z:/Resources/excel/goodreads_library_export.csv'
JSONFILE = 'Z:/Resources/Data/track_book_origins.json'


def oldmain():
    ''' main function '''
    print("[+] Starting...")
    print(f"[+] Reading {DATAFILE}...")
    count = 0
    with open(DATAFILE, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Exclusive Shelf'] == 'read':
                count += 1
                date_show = pd.to_datetime(row['Date Added'])
                date_year = date_show.year
                print(f"[-] {date_year}")
    print(f"[*] Total books read: {count}")
    print("[+] Done.")


def main():
    ''' main function '''
    print("[+] Starting.")
    print(f"[+] Reading {JSONFILE}...")
    booklist = []
    with open(JSONFILE, 'r', encoding='utf-8-sig') as jsonfile:
        for item in jsonfile:
            bookdict = json.loads(item)
            booklist.append(bookdict)
    for book in booklist:
        print(f"[-] {book['book_name']} was read on {book['created_at']}")
    print(f"[*] Total books read: {len(booklist)}")
    print("[+] Done.")


if __name__ == '__main__':
    main()
