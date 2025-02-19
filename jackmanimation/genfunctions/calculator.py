''' a simple calculator module '''


def add(a, b):
    ''' add two numbers '''
    return a + b


def subtract(a, b):
    ''' subtract two numbers '''
    return a - b


def multiply(a, b):
    ''' multiply two numbers '''
    return a * b


def divide(a, b):
    ''' divide two numbers '''
    return a / b


def main():
    ''' main function '''
    print(add(1, 2) == 3)
    print(subtract(2, 1) == 1)
    print(multiply(1, 2) == 2)
    print(divide(1, 2) == 0.5)


if __name__ == '__main__':
    main()
