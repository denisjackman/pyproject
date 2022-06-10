"""
http_builder.py

This program is designed to build webpages

"""

__author__ = "Denis J Jackman (denis_jackm+an@hotmail.com)"
__version__ = "$Revision: 1.00 $"
__date__ = "$Date: 2022/06/09 00:31:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"


def html_init():
    """ this is the initiator for a webpage """
    print('''
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
     "http://www.w3.org/TR/html4/strict.dtd">
    ''')
    print('<HTML>')


def html_head():
    """ this publishes the html header """
    print('<HEAD>')
    print('</HEAD>')
    title = "this is my test web page"
    html_title(title)


def html_body():
    """ this is the html body """
    print('<BODY>')
    print('<P>Hello world!')
    print('</BODY>')


def html_finish():
    """ this is the finish of the web page """
    print('</HTML>')


def html_title(http_title):
    """ this publishes the title """
    print('<TITLE>' + http_title + '</TITLE>')


def main():
    """ This is the main routine for the program """


if __name__ == '__main__':
    main()
