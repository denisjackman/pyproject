'''Display all the fonts available to Tkinter in a scrollable list.'''
import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title('Font Families')
fonts = list(font.families())
fonts.sort()


def populate(pop_frame):
    '''Put in the fonts'''
    listnumber = 1
    for item in fonts:
        label_text = f"{str(listnumber)} {item} "
        label = tk.Label(pop_frame,
                         text=label_text,
                         font=(item, 16))
        label.pack()
        listnumber += 1


def onFrameConfigure(ofc_canvas):
    '''Reset the scroll region to encompass the inner frame'''
    ofc_canvas.configure(scrollregion=ofc_canvas.bbox("all"))


canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
frame = tk.Frame(canvas, background="#ffffff")
vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4, 4), window=frame, anchor="nw")

frame.bind("<Configure>",
           lambda event,
           canvas=canvas: onFrameConfigure(canvas))

populate(frame)

root.mainloop()
