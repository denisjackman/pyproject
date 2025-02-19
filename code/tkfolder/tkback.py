'''
    https://levelup.gitconnected.com/10-interesting-python-tkinter-programs-with-code-df52174993e1
'''

import tkinter as tk
from random import randint

color_changer = tk.Tk()


def update():
    '''
    This function will update the color of the window every second
    '''
    color = f"{randint(0, 0xFFFFFF)}"
    color_changer.config(background='#fcba03' + color)
    color_changer.after(1000, update)


update()
color_changer.title('color')
color_changer.geometry("400x400")
color_changer.mainloop()
