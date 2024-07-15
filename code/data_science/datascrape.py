'''
datascrape.py

This is a os utility tool

'''

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.00 $"
__date__ = "$Date: 2022/09/05 09:00:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"

from urllib.request import urlopen
from bs4 import BeautifulSoup


def datascrapemain():
    '''
        this is the main function
    '''
    print("Starting a data scrape")

    # set up the variables
    listfiles = []
    checkfilepath = "Z:/Resources/Data/Reddit-data/comment_votes.csv"

    with open(checkfilepath, encoding='utf-8-sig') as input_file:
        for item in input_file.readlines():
            listitems = item.split(',')
            listfiles.append(listitems[1])

    # step through the list of files
    for item in listfiles:
        if item != 'permalink':
            with urlopen(item) as page:
                with urlopen(item) as page:
                    soup = BeautifulSoup(page, features="lxml")
                    stuff = soup.find("meta", property="og:title")
                    if stuff is not None:
                        print(f"file: {item} title: {stuff['content']}")
    print("Finished a data scrape")


if __name__ == '__main__':
    datascrapemain()
