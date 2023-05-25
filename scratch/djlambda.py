'''Lambda test script '''
SQUARE = lambda x: x ** 2
ADD = lambda x, y: x + y

def main():
    ''' main function '''
    print(f'[-] Square of 5 is {SQUARE(5)}')
    print(f'[-] Add 5 and 10 is {ADD(5, 10)}')

if __name__ == '__main__':
    main()
