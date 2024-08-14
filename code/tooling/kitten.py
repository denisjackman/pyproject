''' This is a search tool for the Kitten project.'''
import os
import sys
# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.utilities.fileutility import getargs


def main():
    ''' This is the main function for the kitten project.'''
    print('[*] kitten starting up')
    print('[-] kitten getting arguments')
    kitten_command_args = getargs()
    if kitten_command_args["verbosemode"]:
        print('[-] kitten walking through files')
        print(f'[-] {kitten_command_args}')
    if kitten_command_args["deletemode"]:
        print('[-] kitten delete mode')
    if kitten_command_args["verbosemode"]:
        print('[-] kitten verbose mode')
    print('[*] kitten finished')


if __name__ == "__main__":
    main()
