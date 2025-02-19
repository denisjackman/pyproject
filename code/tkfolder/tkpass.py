'''
    https://levelup.gitconnected.com/10-interesting-python-tkinter-programs-with-code-df52174993e1
'''
import tkinter
import random
import string


def gen():
    '''
    Generate a random string of length n
    '''
    password = []
    for i in range(4):
        lower = random.choice(string.ascii_lowercase)
        upper = random.choice(string.ascii_uppercase)
        password.append(lower)
        password.append(upper)
        passs = " ".join(str(x)for x in password)
        label.config(text=passs)
    return passs


root = tkinter.Tk()
label = tkinter.Label(root, font=('arial', 40, 'bold'))
label.pack()
BUTTON1 = tkinter.Button(root,  # pylint: disable=E1111
                         text="Generate",
                         font=('arial', 40, 'bold'),
                         command=gen). place(x=100, y=200)
root.geometry("500x500")
root.title("password ")
root.mainloop()
