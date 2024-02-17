''' This is an example of using wordlist to crack a zip file password.'''
import zipfile36 as zipfile
from colorama import Fore

ZIPFILE = 'y://Resources//development//data//newtest.zip'
RESET = Fore.RESET
NOTE = Fore.BLACK + '[*] '
INFO = Fore.CYAN + '[!] '
ERROR = Fore.RED + '[-] '
NOTICE = Fore.GREEN + '[+] '


def ZipChecker(checkfile):
    '''Main function'''
    print(f'{NOTE}Zip File Password Checker - Starting {RESET}')

    zf = zipfile.ZipFile(checkfile)
    for zinfo in zf.infolist():
        is_encrypted = zinfo.flag_bits & 0x1
        if is_encrypted:
            print(f'{INFO}{zinfo.filename} is encrypted! {RESET}')
        else:
            print(f'{INFO}{zinfo.filename} is not encrypted. {RESET}')
    print(f'{NOTE}Zip File Password Checker - Finishing {RESET}')


if __name__ == '__main__':
    ZipChecker(ZIPFILE)
