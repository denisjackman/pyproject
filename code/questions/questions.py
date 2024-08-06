''' This is a questions scratch pad'''


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
