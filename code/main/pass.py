'''
    password
'''
import random
import string

def passwordgenerator(pwlen):
    '''
        password generator
    '''
    letters = string.ascii_letters
    numbers = '0123456789'
    special = '-+*%&$!_'
    passcode = letters + numbers + special
    password = ''.join(random.sample(passcode, pwlen))
    return password


def main():
    '''
        main function
    '''
    mainlen = input("Enter required password length")
    print(passwordgenerator(mainlen))

if __name__ == '__main__':
    main()
