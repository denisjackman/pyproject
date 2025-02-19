'''
    this is a play project to use TKINTER
    to develop a GUI application
'''
import os
import sys
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.utilities.fileutility import walk_through


MAIN_WINDOW = tk.Tk()
LOGO = 'Z:/Resources/jackmanimation.png'
ALOGO = 'Z:/jackmanimation/jackmanimation/images/logo.jpg'
TM_TARGET_DIR = 'Z:/Resources/'


def open_filename():
    ''' open a file '''
    filename = filedialog.askopenfilename(title='open')
    return filename


def load_image(li_image):
    ''' load an image '''
    print('[*] load_image: start')
    print(f'[-] load_image: image: {li_image}')
    li_temp = Image.open(li_image)
    li_photo = ImageTk.PhotoImage(li_temp)
    print('[*] load_image: end')
    return li_photo


def populate(pop_frame, pop_list):
    '''Put in the fonts'''
    listnumber = 1
    for item in pop_list:
        label_text = f"{str(listnumber)} {item} "
        pop_label = tk.Label(pop_frame,
                             text=label_text,
                             font=('Arial', 16))
        # pop_label.pack()
        pop_label.grid(row=0, column=4, columnspan=2, sticky=tk.S)
        listnumber += 1


def image_button():
    ''' image button '''
    ib_file = open_filename()
    ib_image = Image.open(ib_file)
    ib_image = ib_image.resize((50, 50), Image.Resampling.LANCZOS)
    ib_image = ImageTk.PhotoImage(ib_image)
    ib_panel = tk.Label(MAIN_WINDOW, image=ib_image)
    ib_panel.image = ib_image
    # ib_panel.pack()
    # ib_panel.grid(row=8, column=0, columnspan=2, sticky=tk.E)
    ib_panel.place(x=400, y=60, width=50, height=50)


def main_menu():
    ''' main menu '''
    mw_menu = tk.Menu(MAIN_WINDOW)

    mw_filemenu = tk.Menu(mw_menu, tearoff=0)
    mw_filemenu.add_command(label='New')
    mw_filemenu.add_separator()
    mw_filemenu.add_command(label='Open')
    mw_filemenu.add_command(label='Save')
    mw_filemenu.add_command(label='Save As')
    mw_filemenu.add_command(label='Close')
    mw_filemenu.add_command(label='Print')
    mw_filemenu.add_separator()
    mw_filemenu.add_command(label='Exit', command=MAIN_WINDOW.quit)

    mw_helpmenu = tk.Menu(mw_menu, tearoff=0)
    mw_helpmenu.add_command(label='Help Index')
    mw_helpmenu.add_command(label='About')

    mw_menu.add_cascade(label='File', menu=mw_filemenu)
    mw_menu.add_cascade(label='Help', menu=mw_helpmenu)

    MAIN_WINDOW.config(menu=mw_menu)


def main():
    ''' main function '''
    print('[*] main: start')
    mw_image = tk.PhotoImage(file=LOGO)
    mw_aimage = load_image(ALOGO)
    button_image = mw_aimage
    tm_mainargs = {"verbosemode": False,
                   "deletemode": False,
                   "startdirectory": TM_TARGET_DIR,
                   "targetdirectory": TM_TARGET_DIR}
    tm_filelist = walk_through(tm_mainargs)

    MAIN_WINDOW.title('TK Project')
    # MAIN_WINDOW.config(bg='black')
    MAIN_WINDOW.geometry('400x400')
    MAIN_WINDOW.minsize(400, 400)
    MAIN_WINDOW.maxsize(800, 600)
    MAIN_WINDOW.iconphoto(False, mw_image)

    main_menu()

    mw_radiovar = tk.IntVar()
    mw_radio = tk.Radiobutton(MAIN_WINDOW,
                              text='Radio Button 1',
                              variable=mw_radiovar,
                              value=1)

    mw_radio1 = tk.Radiobutton(MAIN_WINDOW,
                               text='Radio Button 2',
                               variable=mw_radiovar,
                               value=2)

    mw_radio2 = tk.Radiobutton(MAIN_WINDOW,
                               text='Radio Button 3',
                               variable=mw_radiovar,
                               value=3)

    mw_label = tk.Label(MAIN_WINDOW,
                        text=f'Total files found {len(tm_filelist)}',
                        font=('Arial', 15, 'bold'))

    mw_button = tk.Button(MAIN_WINDOW,
                          image=button_image)

    mw_selected_option = tk.StringVar(value='Please Choose Wisely')
    mw_dropdown = tk.OptionMenu(MAIN_WINDOW,  # pylint: disable=E1120
                                mw_selected_option,
                                *tm_filelist)

    mw_list = tk.Listbox(MAIN_WINDOW, bg='yellow', width=120)
    mw_list.insert(tk.END, *tm_filelist)

    mw_message = tk.Message(MAIN_WINDOW,
                            text='This is a message',
                            font=('Arial', 20),
                            relief=tk.RAISED,
                            bg='blue',)

    # mw_radio.pack()
    # mw_radio1.pack()
    # mw_radio2.pack()
    # mw_label.pack()
    # mw_button.pack()
    # mw_dropdown.pack(pady=10, padx=10)
    # mw_message.pack()
    # mw_list.pack()

    # mw_radio.grid(row=2, column=1, columnspan=1, sticky=tk.E)
    # mw_radio1.grid(row=3, column=1, columnspan=1, sticky=tk.E)
    # mw_radio2.grid(row=4, column=1, columnspan=1, sticky=tk.E)
    # mw_label.grid(row=0, column=0, columnspan=1, sticky=tk.W)
    # mw_button.grid(row=0, column=3, columnspan=1, sticky=tk.W)
    # mw_dropdown.grid(row=5, column=0, columnspan=5, sticky=tk.E)
    # mw_list.grid(row=6, column=0, columnspan=8, sticky=tk.W)
    # mw_message.grid(row=7, column=0, columnspan=2, sticky=tk.E)

    mw_radio.place(x=20, y=120, width=100, height=20)
    mw_radio1.place(x=20, y=140, width=100, height=20)
    mw_radio2.place(x=20, y=160, width=100, height=20)
    mw_label.place(x=100, y=0, width=100, height=20)
    mw_button.place(x=0, y=50, width=50, height=50)
    mw_dropdown.place(x=300, y=0, width=100, height=20)
    mw_list.place(x=200, y=200, width=150, height=100)
    mw_message.place(x=0, y=400, width=150, height=50)

    print('[*] main: end')


if __name__ == '__main__':
    main()
    main_button = tk.Button(MAIN_WINDOW,
                            text='Image Button',
                            command=image_button)
    # main_button.pack()
    # main_button.grid(row=9, column=0, columnspan=2, sticky=tk.W)
    main_button.place(x=0, y=0, width=100, height=50)

    MAIN_WINDOW.mainloop()
