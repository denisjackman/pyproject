'''
    menu system
'''
import time

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2018/08/08 12:57:00 $"
__copyright__ = "Copyright (c) "
__license__ = "Python"

'''
    Author : Denis Jackman
    Date : 8th-August-2018
    Version : 1.0
    Function :
    A sample menu system for python.

'''
users = {}


def main_menu():
    '''
        main menu
    '''
    result = True
    status = input("do you have a login account ? Y/N? Or press Q to Quit. ")
    status = status.lower()
    if status == 'y':
        old_user()
    elif status == 'n':
        new_user()
    elif status == 'q':
        result = False
    return result


def old_user():
    '''
        old user
    '''
    login = input("Enter Login name : ")
    password = input("Enter Password : ")
    if login in users and users[login] == password:
        print("\nLogin successful \n")
        print(f"User: {login} accessed the system at {time.asctime()}")
    else:
        print("\n User does not exist or has wrong password\n")


def new_user():
    '''
        new user
    '''
    create_login = input("Create a login name: ")
    if create_login in users:
        print("\n Login Name already exists.\n")
    else:
        create_password = input("Create password: ")
        users[create_login] = create_password
        print("\nUser Created \n")
        with open("Z:/Resources/development/main/logins.txt",
                  "a",
                  encoding='utf-8-sig') as logins:
            logins.write("\n" + create_login + " " + create_password)


def main():
    '''
        main function
    '''
    main_running = True
    while main_running:
        main_running = main_menu()


if __name__ == "__main__":
    # run the main
    main()
