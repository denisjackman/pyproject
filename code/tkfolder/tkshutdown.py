'''
    https://levelup.gitconnected.com/10-interesting-python-tkinter-programs-with-code-df52174993e1
'''
import tkinter
import os

root = tkinter.Tk()
root.geometry("300x300")


def shut():
    '''
    This function is used to shutdown the system
    '''
    os.system("shutdown /s /t 1")


TTK = tkinter.Button(root, text="SHUT DOWN", command=shut).pack()  # pylint: disable=E1111
root.mainloop()
