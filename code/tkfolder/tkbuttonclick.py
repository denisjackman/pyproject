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


def on_button_click():
    ''' button click event '''
    print('[*] on_button_click: start')
    print('[-] on_button_click: button clicked')
    if button.cget('text') == 'Button Clicked':
        button.config(text='Click Me')
    else:
        button.config(text='Button Clicked')
    print('[*] on_button_click: end')


def on_entry_submit():
    ''' entry submit event '''
    print('[*] on_entry_submit: start')
    print('[-] on_entry_submit: entry submitted')
    print(f'[-] on_entry_submit: entry: {entry.get()}')
    button.config(text=f"Follow {entry.get()}")
    print('[*] on_entry_submit: end')


def load_image(li_image):
    ''' load an image '''
    print('[*] load_image: start')
    print(f'[-] load_image: image: {li_image}')
    li_photo = tk.PhotoImage(file=li_image)
    print('[*] load_image: end')
    return li_photo


def main():
    ''' main function '''
    print('[*] tk example start')
    main_window = tk.build_window('tk example', '800x800')
    label = tk.Label(main_window,
                     text='tk example label in my window',
                     bg='red', padx=20, pady=20)
    label.pack()
    label1 = tk.Label(main_window,
                      text='tk example label1 in my window',
                      font=('Arial', 15, 'bold'),
                      bg='yellow', padx=20, pady=20)
    label1.pack()
    label2 = tk.Label(main_window,
                      text='tk example label2 in my window',
                      font=('Monospace', 16, 'italic'),
                      bg='green', padx=20, pady=20)
    label2.pack()

    logo = load_image(LOGO)
    label3 = tk.Label(main_window, image=logo)
    label3.pack()

    main_window.mainloop()
    print('[*] tk example end')


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
