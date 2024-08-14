'''
    https://levelup.gitconnected.com/10-interesting-python-tkinter-programs-with-code-df52174993e1
'''

from tkinter import messagebox
import tkinter as tk

root = tk.Tk()
root.geometry("200x200")


def msg():
    '''
    This function will show a message box
    '''
    messagebox.showwarning("Alert Box", "Stop Virus found")


but = tk.Button(root, text="ok", command=msg)
but.place(x=100, y=100)
root.mainloop()
