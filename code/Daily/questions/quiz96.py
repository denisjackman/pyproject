''' quiz96.py
Quiz: 96

What will be the output of the following code?
    a: ['python', 'hub']
    b: ['PYTHON', 'HUB']
    c: infinite loop
    d: None of the above

the answer is: c
the explanation:
    The code will run into an infinite loop.
    The for loop will keep on appending the elements to the list.
    The list will keep on growing and the loop will never end.
'''


def main():
    ''' main function '''
    myList = ["python", "hub"]
    for i in myList:
        myList.append(i.upper())  # pylint: disable=w4701
    print(myList)


if __name__ == "__main__":
    main()
