''' tkplay - play a sound file using tkinter '''

import tkinter as tk


def build_window(bw_name, bw_geometry):
    ''' build a window '''
    print('[*] build_window: start')
    print('[-] build_window: name: %s, geometry: %s' % (bw_name, bw_geometry))
    bw_window = tk.Tk()
    bw_window.title(bw_name)
    bw_window.geometry(bw_geometry)
    print('[*] build_window: end')
    return bw_window


def main():
    ''' main function '''
    print('[*] tk example start')
    main_window = build_window('tk example', '400x400')
    label = tk.Label(main_window,
                     text='tk example label in my window',
                     bg='red')
    label.pack()
    label1 = tk.Label(main_window,
                      text='tk example label1 in my window',
                      font=('Arial', 15, 'bold'),
                      bg='yellow')
    label1.pack()
    label2 = tk.Label(main_window,
                      text='tk example label2 in my window',
                      font=('Monospace', 16, 'italic'),
                      bg='green')
    label2.pack()
    main_window.mainloop()
    print('[*] tk example end')


if __name__ == '__main__':
    main()
