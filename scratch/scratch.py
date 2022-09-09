#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
scratch.py

This program is a template for python programs
All this stuff at the top of the script is just optional metadata;

"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.00 $"
__date__ = "$Date: 2022/09/08 17:16:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"

def pageheader():
    '''
    build the header of the web page
    '''
    title = 'default title'
    webpage = ''
    webpage += '<!DOCTYPE html>'
    webpage += '<html>'
    webpage += '<head>'
    webpage += f'<title>{title}</title>'
    webpage += '</head>'
    webpage += '<body>'
    return webpage

def pagebody():
    '''
    build the body of the web page
    '''
    webpage = 'Hello World'
    return webpage

def pagefooter():
    '''
    build the footer of the web page
    '''
    webpage = ''
    webpage += '</body>'
    webpage += '</html>'
    return webpage
def build_page():
    '''
    build the web page
    '''
    webpage = ''
    webpage += pageheader()
    webpage += pagebody()
    webpage += pagefooter()
    return webpage

def main():
    """ This is the main routine for the program """
    print("Starting the sequence:")
    path = r'Y:\pyproject\scratch\index.html'
    with open(path, "w", encoding='utf8') as file:
        file.write(build_page())
    print("finishing up and closing down:")

if __name__ == '__main__':
    main()
