''' quiz91
    What is the output of the following code?
    A) 0, 1, 2
    B) 0, 1, 2, 3
    C) 1, 2, 3

    The answer is A) 0, 1, 2

    the explanation is that the while loop will
    run 3 times and print the value of i

'''


def main():
    ''' main function '''
    i = 0
    while i < 3:
        print(f'[-] i is {i}')
        i += 1


if __name__ == '__main__':
    main()
