''' This is an example of using wordlist to crack a zip file password.'''
import sys
import zipfile36 as zipfile
from tqdm import tqdm
from colorama import Fore

RESET = Fore.RESET
NOTE = Fore.BLACK + '[*] '
INFO = Fore.CYAN + '[!] '
ERROR = Fore.RED + '[-] '
NOTICE = Fore.GREEN + '[+] '
WORDLIST = 'y://Resources//development//lists//wordlist.txt'
ZIPFILE = 'y://Resources//development//data//secret.zip'


def ZipCracker(Crackfile, Cracklist):
    '''Main function'''
    print(f'{NOTE}Zip File Password Cracker - Starting{RESET}')
    with zipfile.ZipFile(Crackfile) as secret_zipfile:
        print(f'{NOTE}{Crackfile} has '
              f'{len(secret_zipfile.namelist())} '
              f'file(s) in it.{RESET}')
    total_passwords = 0
    with open(Cracklist, 'rb') as lenfile:
        for _ in lenfile:
            total_passwords += 1
    print(f'{NOTE}{total_passwords} passwords to test.{RESET}')
    print(f'{NOTE}Cracking, {Crackfile} please wait...{RESET}')
    with open(Cracklist, "rb") as wordfile:
        for password in tqdm(wordfile,
                             total=total_passwords,
                             unit='passwords'):
            try:
                with zipfile.ZipFile(Crackfile) as secret_zipfile:
                    secret_zipfile.extractall(pwd=password.strip())
            except:  # pylint: disable=bare-except
                continue
            else:
                print(f'{NOTICE}Password found: '
                      f'{password.decode().strip()}{RESET}')
                print(f'{NOTE}Zip File Password Cracker - Completed{RESET}')
                sys.exit(0)
    print(f'{ERROR}Password not found, try other wordlist.{RESET}')
    print(f'{NOTE}Zip File Password Cracker - Completed{RESET}')


if __name__ == '__main__':
    ZipCracker(ZIPFILE, WORDLIST)
