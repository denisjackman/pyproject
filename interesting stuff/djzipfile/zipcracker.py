''' This is an example of using wordlist to crack a zip file password.'''
import zipfile
#from tqdm import tqdm
from colorama import Fore

RESET = Fore.RESET
NOTE = Fore.BLUE + '[*] '
INFO = Fore.RED + '[!] '
ERROR = Fore.RED + '[-] '
NOTICE = Fore.YELLOW + '[+] '
WORDLIST = 'lists//test.txt'
ZIPFILE = 'data//secret.zip'

def ZipCracker(Crackfile, Cracklist):
    '''Main function'''
    print(f'{NOTE}Zip File Password Cracker - Starting{RESET}')
    secret_zipfile = zipfile.ZipFile(Crackfile)
    print(f'{NOTE}{Crackfile} has {len(secret_zipfile.namelist())} file(s) in it.{RESET}')
    total_passwords = len(list(open(Cracklist, 'r', encoding='utf8')))
    print(f'{NOTE}{total_passwords} passwords to test.{RESET}')
    print(f'{NOTE}Cracking, {Crackfile} please wait...{RESET}')
    with open(Cracklist, "r", encoding='utf8') as wordfile:
        for password in wordfile:
            password = password.strip()
            print(f'{INFO}Testing: {password}{RESET}')
            try:
                secret_zipfile.extractall(pwd=password)
            except zipfile.error as err:
                print( f'{ERROR} incorrect: {password} [{err}]{RESET}')
                continue
            else:
                print(f'{NOTICE}Password found: {password}{RESET}')
                exit(0)
    print(f'{ERROR}Password not found, try other wordlist.{RESET}')
    print(f'{NOTE}Zip File Password Cracker - Completed{RESET}')

if __name__ == '__main__':
    ZipCracker(ZIPFILE, WORDLIST)
