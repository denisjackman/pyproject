'''
trying the new match syntax
https://learnpython.com/blog/python-match-case-statement/

'''
import sys


print(f'Your python version is {sys.version_info[0]}.{sys.version_info[1]}. ')
if sys.version_info[0] == 3 and sys.version_info[1] >= 10:
    COMMAND = 'Hello, World!'
    match COMMAND:
        case 'Hello, World!':
            print('Hello to you too!')
        case 'Goodbye, World!':
            print('See you later')
        case other:
            print('No match found')
else:
    print('boring old python checking')
