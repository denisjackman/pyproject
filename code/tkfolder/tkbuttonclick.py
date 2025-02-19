'''
    tkplay - play with tkinter
    geometry managers are
        pack,
        grid,
        place

    The widgets are:
        Label,
        Button,
        Entry,
        Text,
        Frame,
        Checkbutton,
        Radiobutton,
        Listbox,
        Scrollbar,
        Scale,
        Canvas,
        Menu,
        Menubutton,
        OptionMenu,
        LabelFrame,
        PanedWindow,
        Message,
        Spinbox,
        Bitmap,
        Image,
        PhotoImage,
        Toplevel,

'''

import tkinter as tk

LOGO = 'Z:/Resources/jackmanimation.png'


def on_entry_submit():
    ''' entry submit event '''
    print('[*] on_entry_submit: start')
    print('[-] on_entry_submit: entry submitted')
    button.config(text=f"Follow {entry.get()}")  # pylint: disable=E0606
    print('[*] on_entry_submit: end')


def load_image(li_image):
    ''' load an image '''
    print('[*] load_image: start')
    print(f'[-] load_image: image: {li_image}')
    li_photo = tk.PhotoImage(file=li_image)
    print('[*] load_image: end')
    return li_photo


if __name__ == '__main__':
    main_window = tk.Tk()
    main_window.title('tk example')
    main_window.minsize(400, 400)
    main_window.maxsize(800, 800)
    label = tk.Label(main_window,
                     text='tk example label in my window',
                     font=('Arial', 15, 'bold'),
                     bg='red',
                     padx=20,
                     pady=20)
    label.pack()
    entry = tk.Entry(main_window, width=30, show='*')
    entry.pack()

    button = tk.Button(main_window,
                       text='Submit',
                       command=on_entry_submit)
    frame = tk.Frame(main_window)
    frame.pack()

    button1 = tk.Button(frame,
                        text='Block1',
                        fg='red')
    button1.pack(side=tk.LEFT)
    button2 = tk.Button(frame,
                        text='Block2',
                        fg='blue')
    button2.pack(side=tk.LEFT)

    button.pack()
    main_window.mainloop()
