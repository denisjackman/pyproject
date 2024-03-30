''' tkplay - play a sound file using tkinter '''

import tkinter as tk


def build_window(bw_name, bw_geometry):
    ''' build a window '''
    bw_window = tk.Tk()
    bw_window.title(bw_name)
    bw_window.geometry(bw_geometry)
    return bw_window

def main():
    ''' main function '''
    print('[*] tk example start')
    main_window = build_window('tk example', '400x400')
    label = tk.Label(main_window, text='tk example label in my window')
    label.pack()
    main_window.mainloop()
    print('[*] tk example end')


if __name__ == '__main__':
    main()
