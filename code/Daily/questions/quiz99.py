'''
    quiz 99
    based on the following code, what will be the output?
    a) hillo
    b) hello
    c) Error
    d) None

    correct answer is:
    c) Error

    explanation:
    the code will throw an error because strings are immutable in python
    and you cannot change the value of a string once it is created
    so the code will throw an error at line 16

    check pyproject/images/quiz99.png for the original question

'''


def main():
    ''' main function '''
    text = 'hello'
    text[1] = 'i'  # pylint: disable=unsupported-assignment-operation
    print(text)


if __name__ == "__main__":
    main()
