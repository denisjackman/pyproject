'''
    https://levelup.gitconnected.com/10-interesting-python-tkinter-programs-with-code-df52174993e1
'''

import tkinter as tk
root = tk.Tk()
root.resizable(0, 0)
root.title('CAPITALIZE')

OUT = ''


def capitalize():
    '''
    This function will capitalize the text in the entry box
    '''
    global OUT  # pylint: disable=W0603
    tkinput = text1.get("1.0", tk.END)
    text1.delete("1.0", tk.END)
    OUT = tkinput.upper()
    text1.insert("1.0", OUT)
    return OUT


text1 = tk.Text(root,
                font=('arial', 40, 'bold'),
                height=3,
                width=15)
text1.pack()

button1 = tk.Button(root,
                    text="CAPITALIZE",
                    font=('arial', 40, 'bold'),
                    command=capitalize)
button1.pack()
root.mainloop()
