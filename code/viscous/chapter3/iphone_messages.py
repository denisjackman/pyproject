''' check iphone for messages '''
import os
import sqlite3
import argparse
import sys


def is_message_table(iphonedb):
    ''' check if the table exists '''
    try:
        with sqlite3.connect(iphonedb) as conn:
            c = conn.cursor()
            c.execute('SELECT tbl_name FROM sqlite_master WHERE type == "table";')
            for row in c:
                if 'message' in str(row):
                    return True
    except Exception as e:
        print(e)
        return False
    return False


def print_message(msgdb):
    ''' print the message '''
    try:
        with sqlite3.connect(msgdb) as conn:
            c = conn.cursor()
            c.execute('SELECT datetime(date, "unixepoch"), address, text FROM message WHERE address > 0;')
            for row in c:
                date = str(row[0])
                addr = str(row[1])
                text = row[2]
                print(f'\n[+] Date: {date}, Addr: {addr}, Message: {text}')
    except Exception as e:
        print(e)


def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='check iphone for messages')
    parser.add_argument('-p', dest='path', type=str, help='specify iphone backup directory')
    args = parser.parse_args()
    path = args.path
    if not path:
        print(parser.usage)
        sys.exit(0)
    elif not os.path.isdir(path):
        print(f'[-] {path} does not exist')
        sys.exit(0)
    else:
        msgdb = os.path.join(path, '3d0d7e5fb2ce288813306e4d4636395e047a3d28')
        if is_message_table(msgdb):
            print_message(msgdb)
        else:
            print(f'[-] no message table found in {msgdb}')


if __name__ == '__main__':
    main()
