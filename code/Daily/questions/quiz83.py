''' This is a questions scratch pad'''


def question5():
    ''' This is a question 5'''
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500}
    d, r = roman  # pylint: disable=W0644
    print(f'[-] question 5 : {d} {r}')


def main():
    ''' This is the main function'''
    try:
        question5()
    except Exception as err:
        print(f'[-] question 5 : {err}')


if __name__ == '__main__':
    main()
