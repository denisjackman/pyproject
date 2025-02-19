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


def build_window(bw_name, bw_geometry):
    ''' build a window '''
    print('[*] build_window: start')
    print(f'[-] build_window: name: {bw_name}, geometry: {bw_geometry}')
    bw_window = tk.Tk()
    bw_window.title(bw_name)
    bw_window.geometry(bw_geometry)
    print('[*] build_window: end')
    return bw_window


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
    tkp_main_window = build_window('tk example', '800x800')
    label = tk.Label(tkp_main_window,
                     text='tk example label in my window',
                     bg='red', padx=20, pady=20)
    label.pack()
    tkp_label1 = tk.Label(tkp_main_window,
                          text='tk example tkp_label1 in my window',
                          font=('Arial', 15, 'bold'),
                          bg='yellow', padx=20, pady=20)
    tkp_label1.pack()
    tkp_label2 = tk.Label(tkp_main_window,
                          text='tk example tkp_label2 in my window',
                          font=('Monospace', 16, 'italic'),
                          bg='green', padx=20, pady=20)
    tkp_label2.pack()

    logo = load_image(LOGO)
    label3 = tk.Label(tkp_main_window, image=logo)
    label3.pack()

    tkp_main_window.mainloop()
    print('[*] tk example end')


if __name__ == '__main__':
    main()
