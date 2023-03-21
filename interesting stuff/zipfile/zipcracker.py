''' This is an example of using wordlist to crack a zip file password.'''
import zipfile
from tqdm import tqdm
from colorama import Fore


WORDLIST = 'data//test.txt'
ZIPFILE = 'data//test.zip'

def main():
    '''Main function'''
    print(Fore.GREEN + '[*] Zip File Password Cracker - Starting')
    secret_zipfile = zipfile.ZipFile(ZIPFILE)
    print(Fore.GREEN + f'[*] {ZIPFILE} has {len(secret_zipfile.namelist())} file(s) in it.')
    total_passwords = len(list(open(WORDLIST, 'r', encoding='utf8')))
    print(Fore.GREEN + f'[*] {total_passwords} passwords to test.')
    print(Fore.GREEN + f'[*] Cracking, {ZIPFILE} please wait...')
    with open(WORDLIST, "r", encoding='utf8') as wordfile:
        for password in wordfile:
            print(Fore.YELLOW + f'[!] Testing: {password.strip()}')
            try:
                secret_zipfile.extractall(pwd=password.strip().encode('utf-8'))
            except zipfile.error as err:
                print(Fore.RED + f'[-] Password incorrect: {password.strip()} [{err}]]')
                continue
            else:
                print(Fore.GREEN + f'[+] Password found: {password.strip()}')
                exit(0)
    print(Fore.RED + '[-] Password not found, try other wordlist.')
    print(Fore.GREEN + '[*] Zip File Password Cracker - Completed')

if __name__ == '__main__':
    main()
