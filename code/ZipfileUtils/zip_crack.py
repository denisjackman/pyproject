'''
    zipcrack.py - a simple zip file password cracker
'''
import sys
import zipfile36 as zipfile
from tqdm import tqdm

WORDLIST = 'y://Resources//development//lists//wordlist.txt'
ZIPFILE = 'y://Resources//development//data//secret.zip'


def main():
    '''Main function    '''
    # count the number of words in this WORDLIST
    with open(WORDLIST, "rb") as wordfile:
        temp = wordfile.read()
        n_words = len(temp)
    # print the total number of passwords
    print(f"Total passwords to test: {n_words}")
    with open(WORDLIST, "rb") as wordfile:
        for word in tqdm(wordfile, total=n_words, unit="word"):
            try:
                with zipfile.ZipFile(ZIPFILE) as archive:
                    archive.extractall(pwd=word.strip(),
                                       path="Z://Resources//development//data//")
            except:  # pylint: disable=bare-except
                continue
            else:
                print(f"[+] Password found: {word.decode().strip()}")
                sys.exit(0)
        print("[!] Password not found, try other WORDLIST.")


if __name__ == '__main__':
    main()
