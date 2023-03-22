''' This is a menu program that will allow you to choose from a list of options'''
import os 

def main():
    ''' This is the main function'''
    run_menu = True
    while run_menu:
        os.system('cls')
        print('Welcome to the menu program')
        print('Please choose from the following options')
        print('1. Option 1')
        print('2. Option 2')
        choice = input('Please enter your choice: ')
        if choice == '3':
            run_menu = False
        if choice == '1':
            print('You have chosen option 1')
        elif choice == '2':
            print('You have chosen option 2')
    os.system('cls')
    
if __name__ == '__main__':
    main()
