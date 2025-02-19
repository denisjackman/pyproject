''' This script parses the skype data and displays it.'''
import sqlite3
import argparse
import os
import sys


def print_profile(skype_db):
    '''
    This function prints the profile
    information for a skype database.
    '''
    conn = sqlite3.connect(skype_db)
    c = conn.cursor()
    c.execute("SELECT fullname, skypename, city, country, \
        datetime(profile_timestamp,'unixepoch') FROM Accounts;")
    for row in c:
        print('[*] -- Found Account --')
        print(f'[+] User: {str(row[0])}')
        print(f'[+] Skype Username: {str(row[1])}')
        print(f'[+] Location: {str(row[2])},{str(row[3])}')
        print(f'[+] Profile Date: {str(row[4])}')


def print_contacts(skype_db):
    ''' This function prints the contacts for a skype database.'''
    conn = sqlite3.connect(skype_db)
    c = conn.cursor()
    c.execute("SELECT displayname, skypename, city, country, \
        phone_mobile, birthday FROM Contacts;")
    for row in c:
        print('[*] -- Found Contact --')
        print(f'[+] User: {str(row[0])}')
        print(f'[+] Skype Username: {str(row[1])}')
        if str(row[2]) != '' and str(row[2]) != 'None':
            print(f'[+] Location: {str(row[2])},{str(row[3])}')
        if str(row[4]) != 'None':
            print(f'[+] Mobile Number: {str(row[4])}')
        if str(row[5]) != 'None':
            print(f'[+] Birthday: {str(row[5])}')


def print_calls(skype_db):
    ''' This function prints the calls for a skype database.'''
    conn = sqlite3.connect(skype_db)
    c = conn.cursor()
    c.execute("SELECT datetime(begin_timestamp,'unixepoch'), \
        identity FROM calls, conversations WHERE \
        calls.conv_dbid = conversations.id;")
    print('[*] -- Found Calls --')
    for row in c:
        print(f'[+] Time: {str(row[0])} | Partner: {str(row[1])}')


def print_messages(skype_db):
    ''' This function prints the messages for a skype database.'''
    conn = sqlite3.connect(skype_db)
    c = conn.cursor()
    c.execute("SELECT datetime(timestamp,'unixepoch'), \
        dialog_partner, author, body_xml FROM Messages;")
    print('[*] -- Found Messages --')
    for row in c:
        try:
            if 'partlist' not in str(row[3]):
                if str(row[1]) != str(row[2]):
                    msg_direction = 'To ' + str(row[1]) + ': '
                else:
                    msg_direction = 'From ' + str(row[2]) + ': '
                print(f'[*] Time: {str(row[0])} {msg_direction} {str(row[3])}')
        except:  # pylint: disable=bare-except
            pass


def main():
    ''' Main function.'''
    print('[*] Skype Parser Starting')
    parser = argparse.ArgumentParser(description='Skype Parser')
    parser.add_argument('-p',
                        dest='pathName',
                        type=str,
                        help='specify path name of Skype profile')
    options = parser.parse_args()
    path_name = options.pathName
    if path_name is None:
        parser.print_help()
        sys.exit(0)
    elif os.path.isdir(path_name) is False:
        print(f'[!] Path does not exist: {path_name}')
        sys.exit(0)
    else:
        skype_db = os.path.join(path_name, 'main.db')
        if os.path.isfile(skype_db):
            print_profile(skype_db)
            print_contacts(skype_db)
            print_calls(skype_db)
            print_messages(skype_db)
        else:
            print(f'[!] Skype Database does not exist: {skype_db}')
    print('[*] Skype Parser Ending')


if __name__ == '__main__':
    main()
