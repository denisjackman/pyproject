#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
scratch.py

This program is a template for python programs
All this stuff at the top of the script is just optional metadata;

TODO: finish adding the list of tages 
TODO: divide the tags into html5 supported items 
TODO: add a list of tags that are done 
TDOD: code each tag into a subroutine 
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

def tag_list():
    '''
        build a list of tags
        From https://www.w3schools.com/tags/default.asp
         Tag Description
            '<!--...-->'     Defines a comment
            <!DOCTYPE>       Defines the document type
            <a>              Defines a hyperlink
            <abbr>           Defines an abbreviation or an acronym
            <acronym>        Not supported in HTML5. Use <abbr> instead. Defines an acronym
            <address>        Defines contact information for the author/owner of a document
            <applet>         Not supported in HTML5. Use <embed> or <object> instead. Defines an embedded applet
            <area>           Defines an area inside an image-map
            <article>        Defines an article
            <aside>          Defines content aside from the page content
            <audio>          Defines sound content
            <b>              Defines bold text
            <base>           Specifies the base URL/target for all relative URLs in a document
            <basefont>       Not supported in HTML5. Use CSS instead. Specifies a default color, size, and font for all text in a document
            <bdi>            Isolates a part of text that might be formatted in a different direction from other text outside it
            <bdo>            Overrides the current text direction
            <big>            Not supported in HTML5. Use CSS instead. Defines big text
            <blockquote>     Defines a section that is quoted from another source
            <body>           Defines the document's body
            <br>             Defines a single line break
            <button>         Defines a clickable button
            <canvas>         Used to draw graphics, on the fly, via scripting (usually JavaScript)
            <caption>        Defines a table caption
            <center>         Not supported in HTML5. Use CSS instead. Defines centered text
            <cite>           Defines the title of a work
            <code>           Defines a piece of computer code
            <col>            Specifies column properties for each column within a <colgroup> element
            <colgroup>       Specifies a group of one or more columns in a table for formatting
    '''
        
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
