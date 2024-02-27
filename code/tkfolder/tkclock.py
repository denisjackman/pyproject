'''
    https://levelup.gitconnected.com/10-interesting-python-tkinter-programs-with-code-df52174993e1
'''

import tkinter
import time

root = tkinter.Tk()
root.geometry("400x100")
root.config(bg='black')


def update():
    '''
    This function will update the time on the label every second
    '''
    clock.config(text=time.strftime("%I:%M:%S"))
    clock.after(1000, update)


clock = tkinter.Label(root,
                      background='black',
                      foreground='white',
                      font=('arial', 40, 'bold'))
clock.pack()
update()
root.title('clock')
root.mainloop()
