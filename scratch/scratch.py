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
def metadefinition():
    '''
        build a meta data section
    '''
    meta = ''
    meta += '<meta charset="UTF-8">'
    meta += '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
    meta += '<meta http-equiv="X-UA-Compatible" content="ie=edge">'
    meta += '<meta name="description" content="Python Scripting example">'
    meta += '<meta name="keywords" content="HTML, CSS, JavaScript">'
    meta += '<meta name="author" content="Denis Jackman">'
    return meta


def cssdefintion():
    '''
        build a css style sheet
    '''
    css = ''
    css += '<style>'
    css += 'body {'
    css += 'background-color: black;'
    css += 'font-family: verdana;'
    css += 'font-size: 12px;'
    css += 'color: white;'
    css += '}'
    css += 'h1 {'
    css += 'font-size: 24px;'
    css += 'color: lightgreen;'
    css += 'text-align: center;'
    css += '}'
    css += 'p {'
    css += 'font-size: 20px;'
    css += 'font-family: verdana;'
    css += 'color: 	#E600FF;'
    css += '}'
    css += 'a {'
    css += 'background-color: gray;'
    css += 'color: lightblue;'
    css += 'font-size: 20px;'
    css += 'border: 2px solid white;'
    css += 'border-style: solid;'
    css += 'border-color: white;'
    css += '}'
    css += '</style>'
    return css

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
    webpage += metadefinition()
    webpage += cssdefintion()
    webpage += '</head>'
    return webpage


def pagebody():
    '''
    build the body of the web page
    '''
    webpage = ''
    webpage += '<body>'
    webpage += '<h1>Hello World</h1>'
    webpage += '<p>This is a paragraph.</p>'
    webpage += '<a href="https://www.w3schools.com">This is a link</a>'
    webpage += '</body>'
    return webpage

def pagefooter():
    '''
    build the footer of the web page
    '''
    webpage = ''
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
