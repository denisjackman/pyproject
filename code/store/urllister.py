"""Extract list of URLs in a web page

This program is part of "Dive Into Python", a free Python book for
experienced programmers.  Visit http://diveintopython.org/ for the
latest version.
"""

__author__ = "Mark Pilgrim (mark@diveintopython.org)"
__version__ = "$Revision: 1.2 $"
__date__ = "$Date: 2004/05/05 21:57:19 $"
__copyright__ = "Copyright (c) 2001 Mark Pilgrim"
__license__ = "Python"
import urllib
from sgmllib import SGMLParser

class URLLister(SGMLParser):
    '''Extract list of URLs in a web page'''
    def __init__(self):
        self.urls = []

    def reset(self):
        '''reset the parser'''
        SGMLParser.reset(self)
        self.urls = []

    def start_a(self, attrs):
        '''find the start of an anchor tag'''
        href = [v for k, v in attrs if k=='href']
        if href:
            self.urls.extend(href)

if __name__ == "__main__":
    usock = urllib.urlopen("http://diveintopython.org/")
    parser = URLLister()
    parser.feed(usock.read())
    parser.close()
    usock.close()
    for url in parser.urls:
        print(url)
