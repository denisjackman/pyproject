"""
webscraper.py
"""
import urllib3
from bs4 import BeautifulSoup


__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2019/04/23 00:00:00 $"
__copyright__ = "Copyright (c) 2019 Denis J Jackman"
__license__ = "Python"


def main():
    """
    main
    """
    wiki = "http://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
    page = urllib3.urlopen(wiki)
    soup = BeautifulSoup(page)
    print(soup.prettify())


if __name__ == "__main__":
    main()
