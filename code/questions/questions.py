''' This is a questions scratch pad'''


def question2():
    ''' This is a question 2'''
    mylist = ["python", "hub"]
    for i in mylist:
        mylist.append(i.upper())  # pylint: disable=W4701
    print(f'[-] question 2 : {mylist}')


def question3(a, b, c):
    ''' This is a question 3'''
    if a > b:
        if a > c:
            return a
    elif b > c:
        return b
    else:
        return c
    return 0


def question4():
    ''' This is a question 4'''
    x = [1, 2, 3, 4]
    y = [sum(x[0:i-1]) for i in range(0, 4)]
    print(f'[-] question 4 : {y}')


def question5():
    ''' This is a question 5'''
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500}
    d, r = roman  # pylint: disable=W0644
    print(f'[-] question 5 : {d} {r}')


def question6():
    ''' This is a question 6'''
    print(f'[-] question 6 : {round(1 / 3, 2)} ')


def main():
    ''' This is the main function'''
    print('[*] This is the main function starting')
    print('[-] question 2 : is an infinite loop ')
    print(f'[-] question 3 : {question3(10, 5, 2)}')
    question4()
    try:
        question5()
    except Exception as err:
        print(f'[-] question 5 : {err}')
    question6()
    print('[*] This is the main function ending')


if __name__ == '__main__':
    print('[+] This is the questions program starting')
    main()
    print('[+] This is the questions program ending')
