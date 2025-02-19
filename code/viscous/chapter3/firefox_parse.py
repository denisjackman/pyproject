''' Firefox parse'''
import re
import sqlite3
import argparse
import os
import sys


def print_downloads(download_db):
    ''' print downloads '''
    with sqlite3.connect(download_db) as conn:
        c = conn.cursor()
        c.execute('SELECT name, source, datetime(endTime/1000000,\
        \'unixepoch\') FROM moz_downloads;')
        print('[*] --- Files Downloaded --- ')
        for row in c:
            print(f'[+] File: {str(row[0])} from source: {str(row[1])} at: {str(row[2])}')


def print_cookies(cookies_db):
    ''' print cookies '''
    try:
        with sqlite3.connect(cookies_db) as conn:
            c = conn.cursor()
            c.execute('SELECT host, name, value FROM moz_cookies')
            print('[*] -- Found Cookies --')
            for row in c:
                host = str(row[0])
                name = str(row[1])
                value = str(row[2])
                print(f'[+] Host: {host}, Cookie: {name}, Value: {value}')
    except Exception as e:
        if 'encrypted' in str(e):
            print('[*] Error reading your cookies database.')
            print('[*] Upgrade your Python-Sqlite3 Library')
            sys.exit(0)


def print_history(places_db):
    ''' print history '''
    try:
        with sqlite3.connect(places_db) as conn:
            c = conn.cursor()
            c.execute('SELECT url, datetime(visit_date/1000000,\
            \'unixepoch\') FROM moz_places, moz_historyvisits WHERE \
            visit_count > 0 AND moz_places.id==moz_historyvisits.place_id;')
            print('[*] -- Found History --')
            for row in c:
                url = str(row[0])
                date = str(row[1])
                print(f'[+] {date} - Visited: {url}')
    except Exception as e:
        if 'encrypted' in str(e):
            print('[*] Error reading your places database.')
            print('[*] Upgrade your Python-Sqlite3 Library')
            sys.exit(0)


def print_google(places_db):
    ''' print google '''
    with sqlite3.connect(places_db) as conn:
        c = conn.cursor()
        c.execute('SELECT url, datetime(visit_date/1000000,\
        \'unixepoch\') FROM moz_places, moz_historyvisits WHERE \
        visit_count > 0 AND moz_places.id==moz_historyvisits.place_id;')
        print('[*] -- Found Google --')
        for row in c:
            url = str(row[0])
            date = str(row[1])
            if 'google' in url.lower():
                r = re.findall(r'q=.*\&', url)
                if r:
                    search = r[0].split('&')[0]
                    search = search.replace('q=', '').replace('+', ' ')
                    print(f'[+] {date} - Searched For: {search}')


def main():
    ''' main function '''
    print('[-] Firefox parse started')
    parser = argparse.ArgumentParser(description='Firefox History Parser',
                                     usage='firefox_parse.py --fireprofile <path to firefox profile>')
    parser.add_argument('--fireprofile',
                        type=str,
                        metavar='FIREFOX_PROFILE',
                        help='specify firefox profile path')
    args = parser.parse_args()
    print(f'[*] Firefox profile path: {args.fireprofile} {args}')
    path_name = args.fireprofile
    download_db = os.path.join(path_name, 'downloads.sqlite')
    if os.path.isfile(download_db):
        print_downloads(download_db)
    else:
        print(f'[-] Downloads Db does not exist: {download_db}')
    cookies_db = os.path.join(path_name, 'cookies.sqlite')
    if os.path.isfile(cookies_db):
        print_cookies(cookies_db)
    else:
        print(f'[-] Cookies Db does not exist: {cookies_db}')
    places_db = os.path.join(path_name, 'places.sqlite')
    if os.path.isfile(places_db):
        print_history(places_db)
        print_google(places_db)
    else:
        print(f'[-] PlacesDb does not exist: {places_db}')
    print('[-] Firefox parse finished')


if __name__ == '__main__':
    main()
