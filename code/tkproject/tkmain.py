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
from jackmanimation.utilities.fileutility import walk_through  # noqa: E402


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
        pop_label.pack()
        listnumber += 1


def main():
    ''' main function '''
    print('[*] main: start')
    MAIN_WINDOW.title('TK Project')
    MAIN_WINDOW.config(bg='black')
    MAIN_WINDOW.geometry('800x600')
    MAIN_WINDOW.minsize(1000, 1000)
    MAIN_WINDOW.maxsize(1100, 1100)
    mw_image = tk.PhotoImage(file=LOGO)
    mw_aimage = load_image(ALOGO)
    button_image = mw_aimage
    tm_mainargs = {"verbosemode": False,
                   "deletemode": False,
                   "startdirectory": TM_TARGET_DIR,
                   "targetdirectory": TM_TARGET_DIR}
    tm_filelist = walk_through(tm_mainargs)
    mw_radiovar = tk.IntVar()
    mw_radio = tk.Radiobutton(MAIN_WINDOW,
                              text='Radio Button 1',
                              variable=mw_radiovar,
                              value=1)
    mw_radio.pack()
    mw_radio1 = tk.Radiobutton(MAIN_WINDOW,
                               text='Radio Button 2',
                               variable=mw_radiovar,
                               value=2)
    mw_radio1.pack()
    mw_radio2 = tk.Radiobutton(MAIN_WINDOW,
                               text='Radio Button 3',
                               variable=mw_radiovar,
                               value=3)
    mw_radio2.pack()

    mw_label = tk.Label(MAIN_WINDOW,
                        text=f'Total files found {len(tm_filelist)}',
                        font=('Arial', 15, 'bold'))
    mw_label.pack()
    mw_button = tk.Button(MAIN_WINDOW,
                          image=button_image)
    mw_button.pack()
    MAIN_WINDOW.iconphoto(False, mw_image)

    selected_option = tk.StringVar(value='Please Choose Wisely')
    dropdown = tk.OptionMenu(MAIN_WINDOW,  # pylint: disable=E1120
                             selected_option,
                             *tm_filelist)
    dropdown.pack(pady=10, padx=10)

    mw_list = tk.Listbox(MAIN_WINDOW, bg='yellow', width=120)
    mw_list.insert(tk.END, *tm_filelist)
    mw_list.pack()

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
    mw_menu.add_cascade(label='File', menu=mw_filemenu)

    mw_helpmenu = tk.Menu(mw_menu, tearoff=0)
    mw_helpmenu.add_command(label='Help Index')
    mw_helpmenu.add_command(label='About')
    mw_menu.add_cascade(label='Help', menu=mw_helpmenu)

    MAIN_WINDOW.config(menu=mw_menu)

    mw_message = tk.Message(MAIN_WINDOW,
                            text='This is a message',
                            font=('Arial', 20),
                            relief=tk.RAISED,
                            bg='blue',)
    mw_message.pack()
    print('[*] main: end')


def image_button():
    ''' image button '''
    ib_file = open_filename()
    ib_image = Image.open(ib_file)
    ib_image = ib_image.resize((250, 250), Image.Resampling.LANCZOS)
    ib_image = ImageTk.PhotoImage(ib_image)
    ib_panel = tk.Label(MAIN_WINDOW, image=ib_image)
    ib_panel.image = ib_image
    ib_panel.pack()


if __name__ == '__main__':
    main()
    main_button = tk.Button(MAIN_WINDOW,
                            text='Image Button',
                            command=image_button)
    main_button.pack()
    MAIN_WINDOW.mainloop()
