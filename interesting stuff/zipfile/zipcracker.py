''' This is an example of using wordlist to crack a zip file password.'''
import zipfile
from tqdm import tqdm

WORDLIST = 'data//rockyou.txt'
ZIPFILE = 'data//secret.zip'

def main():
    '''Main function'''
    print('[*] Zip File Password Cracker - Starting')
    secret_zipfile = zipfile.ZipFile(ZIPFILE)
    print(f'[*] {ZIPFILE} has {len(secret_zipfile.namelist())} file(s) in it.')
    total_passwords = len(list(open(WORDLIST, 'r', encoding='utf8')))
    print(f'[*] {total_passwords} passwords to test.')
    print(f'[*] Cracking, {ZIPFILE} please wait...')
    with open(WORDLIST, "r", encoding='utf8') as wordfile:
        for password in tqdm(wordfile, total=total_passwords, unit="password"):
            try:
                secret_zipfile.extractall(pwd=password.strip())
            except:
                continue
            else:
                print(f'[+] Password found: {password.decode().strip()}')
                exit(0)
    print('[-] Password not found, try other wordlist.')
    print('[*] Zip File Password Cracker - Completed')

if __name__ == '__main__':
    main()
