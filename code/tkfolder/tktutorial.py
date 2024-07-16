"""
ZetCode Tkinter tutorial

This script shows a simple window
on the screen.

author: Jan Bodnar
last modified: January 2011
website: www.zetcode.com
"""

from tkinter import Tk, Frame, BOTH


class Example(Frame):
    '''
        class exmaple(Frame):
    '''
    def __init__(self, parent):
        Frame.__init__(self, parent, background="black")

        self.parent = parent

        self.initui()

    def initui(self):
        '''
            def initui(self):
        '''
        self.parent.title("Test")
        self.pack(fill=BOTH, expand=1)


def main():
    ''' main function '''
    root = Tk()
    root.geometry("250x150+300+300")

    root.mainloop()


if __name__ == '__main__':
    main()
