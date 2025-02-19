'''
    https://levelup.gitconnected.com/10-interesting-python-tkinter-programs-with-code-df52174993e1
'''
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
upload = Image.open("Z:/Resources/images/lenna.jpeg")
image = ImageTk.PhotoImage(upload)
label = tk.Label(root, image=image, height=128, width=128)
label.place(x=0, y=0)

root.title('image')
root.geometry('600x400')
root.mainloop()
