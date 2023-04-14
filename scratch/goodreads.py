''' this is a script to sift a goodreads csv file for books '''
import csv
import pandas as pd

DATAFILE = 'Y:/Resources/excel/goodreads_library_export.csv'

def main():
    ''' main function '''
    print("[+] Starting...")
    print(f"[+] Reading {DATAFILE}...")
    count = 0
    with open(DATAFILE, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Exclusive Shelf'] == 'read':
                count += 1
                date_show = pd.to_datetime(row['Date Added'])
                date_year = date_show.year
                print(f"[-] {date_year}")
                #print(f"[=] {type(date_show)}")
                #print(f"[-] {row['Title']} by {row['Author']} was read in {date_show} and rated {row['My Rating']}/5 stars")
    print(f"[*] Total books read: {count}")
    print("[+] Done.")

if __name__ == '__main__':
    main()
