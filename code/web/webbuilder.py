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

def breakline():
    '''
    build a break line
    '''
    webpage = ''
    webpage += '<br>'
    return webpage

def bold(text):
    '''
        build a bold text
    '''
    webpage = ''
    webpage += f'<b>{text}</b>'
    return webpage

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

def pagetitle(titletext):
    '''
        build a title
    '''
    title = ''
    title += '<title>'
    title += titletext
    title += '</title>'
    return title

def pageheader():
    '''
    build the header of the web page
    '''
    title = 'Python Web Page Builder'
    webpage = ''
    webpage += '<!DOCTYPE html>'
    webpage += '<html>'
    webpage += '<head>'
    webpage += pagetitle(title)
    webpage += metadefinition()
    webpage += cssdefintion()
    webpage += '</head>'
    return webpage

def header1(subject):
    '''
    build the header of the web page
    '''
    webpage = ''
    webpage += '<h1>'
    webpage += subject
    webpage += '</h1>'
    return webpage

def buildpara(text):
    '''
        build a paragraph
    '''
    para = ''
    para += '<p>'
    para += text
    para += '</p>'
    return para

def buildlink(link, text):
    '''
        build a link
    '''
    webpage = ''
    webpage += f'<a href="{link}">{text}</a>'
    return webpage

def buildimage(imagepath, imagetext):
    '''
        build an image
    '''
    webpage = ''
    webpage += f'<img src="{imagepath}" alt="{imagetext}">'
    return webpage

def divstart(divid):
    '''
        build a div start
    '''
    div = ''
    div += f'<div id= "{divid}">'
    return div

def divend():
    '''
        build a div end
    '''
    div = ''
    div += '</div>'
    return div

def pagebody():
    '''
    build the body of the web page
    '''
    webpage = ''
    webpage += '<body>'
    webpage += header1('Python Web Builder')
    webpage += buildpara(f'This is a {bold("paragraph")}.')
    webpage += divstart('mainContent')
    webpage += header1('Main content')
    webpage += breakline()
    webpage += buildpara('This is a main content paragraph.')
    webpage += breakline()
    webpage += buildlink("https://www.w3schools.com",'This is a link')
    webpage += breakline()
    webpage += buildimage("https://www.w3schools.com/images/w3schools_green.jpg",'This is an image')
    webpage += breakline()
    webpage += divend()
    webpage += divstart('sidebar')
    webpage += header1('Sidebar Header')
    webpage += breakline()
    webpage += buildpara('This is a paragraph in the sidebar.')
    webpage += breakline()
    webpage += buildlink("https://www.w3schools.com", f'This is a {bold("link")} in the sidebar')
    webpage += breakline()
    webpage += buildimage("https://www.w3schools.com/images/w3schools_green.jpg", 'This is an image in the sidebar')
    webpage += breakline()
    webpage += divend()
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
