''' get all the links on a page '''
import requests as rq
from bs4 import BeautifulSoup
URL = "https://www.maidenheadthicketbowls.org/"
OUTPUT_FILE = "Z:/Resources/development/myLinks.txt"


def getlinks(url, verbose=False):
    ''' get all the links on a page '''
    if verbose:
        print("[+] --- Start getlinks")
    if ("https" or "http") in url:
        data = rq.get(url, timeout=5)
    else:
        data = rq.get("https://" + url, timeout=5)
    soup = BeautifulSoup(data.text, "html.parser")
    links = []
    for link in soup.find_all("a"):
        links.append(link.get("href"))

    # Writing the output to a file (myLinks.txt) instead of to stdout
    # You can change 'a' to 'w' to overwrite the file each time
    with open(OUTPUT_FILE, 'a', encoding='utf-8-sig') as saved:
        print(links[:10], file=saved)
    if verbose:
        print("[+] --- Finish getlinks")


def main():
    ''' main function '''
    getlinks(URL)


if __name__ == '__main__':
    main()
