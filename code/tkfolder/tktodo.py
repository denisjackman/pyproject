'''
    https://levelup.gitconnected.com/10-interesting-python-tkinter-programs-with-code-df52174993e1
'''

import tkinter as tk
window = tk.Tk()

label = tk.Label(window, text="TO-DO-LIST")
label.pack()

tklist = tk.Listbox(window, bg='yellow')
tklist.insert(1, 'Clean your stuff')
tklist.insert(2, 'Create a Tkinter program')
tklist.insert(3, 'Finish application')
tklist.insert(4, 'Get a Refill')
tklist.pack()

window.config(bg='black')
window.geometry("300x300")
window.title('LIST')
window.mainloop()
