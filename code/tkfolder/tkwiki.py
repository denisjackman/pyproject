'''
https://levelup.gitconnected.com/10-interesting-python-tkinter-programs-with-code-df52174993e1
'''
import tkinter
import wikipedia

root = tkinter.Tk()
root.title("Wiki")
root.geometry("400x400")

frame = tkinter.Frame(root)
tkwikinput = tkinter.Entry(frame, width=50)
tkwikinput.pack()
RESULT = ''
text = tkinter.Text(root, font=('ariel', 20))


def search():
    '''
    This function will search the wikipedia for the text in the entry box
    '''
    global RESULT  # pylint: disable=W0603
    RESULT = tkwikinput.get()
    try:
        summary = wikipedia.summary(RESULT, sentences=3)
    except wikipedia.exceptions.PageError as err:
        RESULT = f"{err}"
        summary = RESULT
    text.insert('1.0', summary)
    return RESULT


button = tkinter.Button(frame, text='Search', command=search)
button.pack(side=tkinter.RIGHT)
frame.pack(side=tkinter.TOP)
text.pack()
root.mainloop()
