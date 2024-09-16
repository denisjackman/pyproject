'''quiz94
what is the output of the following code?

a: [6, None, 1, 3]
b: [6, 1, 3]
c: [6, 0, 1, 3]
d: error

The answer is C
    The explanation is that the code is creating a list of the sum of the
    elements of the list x from the beginning to the current index.
    The first element of the list is 0 because the sum of the elements
    from the beginning to the first element is 0.
    The second element of the list is 1 because the sum of the elements
    from the beginning to the second element is 1.
    The third element of the list is 3 because the sum of the elements
    from the beginning to the third element is 3.
    The fourth element of the list is 6 because the sum of the elements
    from the beginning to the fourth element is 6.
    The final list is [6, 0, 1, 3].

'''


def main():
    ''' This is the main function'''
    x = [1, 2, 3, 4]
    y = [sum(x[0:i-1]) for i in range(0, 4)]
    print(f'[-] Answer is  : {y}')


if __name__ == '__main__':
    print('[+] This is the questions program starting')
    main()
    print('[+] This is the questions program ending')
