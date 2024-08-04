'''
    quiz98
    based on the code below, what will be the output?
    a) 4
    b) 10
    c) 14
    d) 20

    correct answer is:
    b) 10

    explanation:
    the code is a recursive function that adds the numbers from 1 to n
    so the output will be 1 + 2 + 3 + 4 = 10

'''


def my_fun(n):
    ''' my_fun '''
    if n == 1:
        return 1
    return n + my_fun(n-1)


def main():
    ''' main '''
    print(my_fun(4))


if __name__ == "__main__":
    main()
