''' This is an example of using wordlist to crack a zip file password.'''
import zipfile
from tqdm import tqdm
from colorama import Fore

RESET = Fore.RESET
NOTE = Fore.BLACK + '[*] '
INFO = Fore.CYAN + '[!] '
ERROR = Fore.RED + '[-] '
NOTICE = Fore.GREEN + '[+] '
WORDLIST = 'lists//wordlist.txt'
ZIPFILE = 'data//secret.zip'

def ZipCracker(Crackfile, Cracklist):
    '''Main function'''
    print(f'{NOTE}Zip File Password Cracker - Starting{RESET}')
    secret_zipfile = zipfile.ZipFile(Crackfile)
    print(f'{NOTE}{Crackfile} has {len(secret_zipfile.namelist())} file(s) in it.{RESET}')
    total_passwords = len(list(open(Cracklist, 'rb')))
    print(f'{NOTE}{total_passwords} passwords to test.{RESET}')
    print(f'{NOTE}Cracking, {Crackfile} please wait...{RESET}')
    with open(Cracklist, "rb") as wordfile:
        for password in tqdm(wordfile, total=total_passwords, unit='passwords'):
            try:
                secret_zipfile.extractall(pwd=password.strip())
            except:
                continue
            else:
                print(f'{NOTICE}Password found: {password.decode().strip()}{RESET}')
                print(f'{NOTE}Zip File Password Cracker - Completed{RESET}')
                exit(0)
    print(f'{ERROR}Password not found, try other wordlist.{RESET}')
    print(f'{NOTE}Zip File Password Cracker - Completed{RESET}')

if __name__ == '__main__':
    ZipCracker(ZIPFILE, WORDLIST)
