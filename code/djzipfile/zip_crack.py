'''
    zipcrack.py - a simple zip file password cracker
'''
import zipfile
from tqdm import tqdm


# the password list path you want to use
WORDLIST = 'lists//WORDLIST.txt'
ZIPFILE = 'data//secret.zip'
#WORDLIST = sys.argv[2]
# the zip file you want to crack its password
#ZIPFILE = sys.argv[1]
# initialize the Zip File object
ZIPFILE = zipfile.ZipFile(ZIPFILE)
# count the number of words in this WORDLIST
n_words = len(list(open(WORDLIST, "rb")))
# print the total number of passwords
print(f"Total passwords to test: {n_words}")
with open(WORDLIST, "rb") as WORDLIST:
    for word in tqdm(WORDLIST, total=n_words, unit="word"):
        try:
            ZIPFILE.extractall(pwd=word.strip())
        except:
            continue
        else:
            print(f"[+] Password found: {word.decode().strip()}")
            exit(0)
print("[!] Password not found, try other WORDLIST.")
