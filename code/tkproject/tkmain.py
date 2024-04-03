'''
    this is a play project to use TKINTER
    to develop a GUI application
'''
import tkinter as tk
from PIL import Image, ImageTk

MAIN_WINDOW = tk.Tk()
LOGO = 'Z:/Resources/jackmanimation.png'
ALOGO = 'Z:/jackmanimation/jackmanimation/images/logo.jpg'


def load_image(li_image):
    ''' load an image '''
    print('[*] load_image: start')
    print(f'[-] load_image: image: {li_image}')
    li_temp = Image.open(li_image)
    li_photo = ImageTk.PhotoImage(li_temp)
    print('[*] load_image: end')
    return li_photo


def main():
    ''' main function '''
    print('[*] main: start')
    name = 'TK Project'
    minx = 800
    miny = 600
    maxx = 1000
    maxy = 900
    geometry = f'{minx}x{miny}'
    MAIN_WINDOW.title(name)
    MAIN_WINDOW.geometry(geometry)
    MAIN_WINDOW.minsize(minx, miny)
    MAIN_WINDOW.maxsize(maxx, maxy)
    image = load_image(LOGO)
    aimage = load_image(ALOGO)  # noqa: F841
    MAIN_WINDOW.iconphoto(False, image)
    print('[*] main: end')


if __name__ == '__main__':
    main()
    MAIN_WINDOW.mainloop()
