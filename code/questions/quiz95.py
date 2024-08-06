''' quiz 95
what is the output of the following code?

a: 2
b: 5
c: 10
d: none of the above

the answer is: c
the explanation:
    The function myFun takes three arguments a, b, and c.
    The function returns the largest of the three numbers.
    In this case, the function is called with the arguments 10, 5, and 2.
    The function compares the first two arguments
    and returns 10 as the largest number.
    The output of the code is 10.
'''


def myFun(a, b, c):
    ''' This is a myfun'''
    if a > b:
        if a > c:
            return a
    elif b > c:
        return b
    else:
        return c
    return 0


def main():
    ''' main function '''
    print(f'[-] quiz 95 : {myFun(10, 5, 2)}')


if __name__ == '__main__':
    main()
