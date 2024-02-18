''' This is an example of building  a zip file with a password.'''
import os
import zipfile36 as zipfile
from colorama import Fore

RESET = Fore.RESET
NOTE = Fore.BLACK + '[*] '
INFO = Fore.CYAN + '[!] '
ERROR = Fore.RED + '[-] '
NOTICE = Fore.GREEN + '[+] '

PACKLIST = ('y://Resources//development//lists//test.txt',
            'y://Resources//development//lists//wordlist.txt')
ZIPFILE = 'y://Resources//development//data//newtest.zip'


def ZipPacker(packfile, packlist):
    ''' This is a main function '''
    print(f'{NOTE}Zip File Packer - Starting{RESET}')
    # Create a ZipFile Object
    with zipfile.ZipFile(packfile, 'w') as zip_object:
        for item in packlist:
            print(f"{INFO}Adding {item} to zip file{RESET}")
            zip_object.write(item)

    # Check to see if the zip file is created
    if os.path.exists(packfile):
        print(f"{NOTICE}ZIP file created{RESET}")
    else:
        print(f"{ERROR}ZIP file not created{RESET}")
    print(f'{NOTE}Zip File Packer - Completed{RESET}')


if __name__ == '__main__':
    ZipPacker(ZIPFILE, PACKLIST)
