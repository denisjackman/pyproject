''' This is an example of building  a zip file with a password.'''
from zipfile import ZipFile
import os
from colorama import Fore

RESET = Fore.RESET
NOTE = Fore.BLUE + '[*] '
INFO = Fore.RED + '[!] '
ERROR = Fore.RED + '[-] '
NOTICE = Fore.YELLOW + '[+] '
WORDLIST = 'lists//test.txt'
ZIPFILE = 'data//newtest.zip'

def ZipPacker(packfile, packlist):
    ''' This is a main function '''
    print(f'{NOTE}Zip File Packer - Starting{RESET}')
    # Create a ZipFile Object
    with ZipFile(packfile, 'w') as zip_object:
    # Adding files that need to be zipped
        zip_object.write(packlist)

    # Check to see if the zip file is created
    if os.path.exists(packfile):
        print(f"{NOTICE}ZIP file created{RESET}")
    else:
        print(f"{ERROR}ZIP file not created{RESET}")
    print(f'{NOTE}Zip File Packer - Completed{RESET}')
    

if __name__ == '__main__':
    ZipPacker(ZIPFILE, WORDLIST)



