'''
    https://levelup.gitconnected.com/10-interesting-python-tkinter-programs-with-code-df52174993e1
'''
import tkinter
from datetime import date
RESULT = ""


def calculator():
    '''
        calculator
    '''
    global RESULT  # pylint: disable=global-statement
    RESULT = str(entry.get())
    today = date.today()
    dob_data = RESULT.split("/")
    date1 = int(dob_data[0])
    month = int(dob_data[1])
    year = int(dob_data[2])
    dob = date(year, month, date1)
    numberOfDays = (today - dob).days
    age = numberOfDays // 365
    label = tkinter.Label(root, text="Your age is " + str(age))
    label.pack()


root = tkinter.Tk()
root.geometry("300x300")
entry = tkinter.Entry(root)
entry.pack()

button = tkinter.Button(root, text="Age", command=calculator)
button.pack()
root.mainloop()
