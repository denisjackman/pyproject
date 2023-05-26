'''Lambda test script '''
FRUIT = ['apple', 'banana', 'cherry', 'kiwi', 'mango']

SQUARE = lambda x: x ** 2
ADD = lambda x, y: x + y
FRUIT_TITLE = map(lambda x: x.title(), FRUIT)
FRUIT_FILTER = filter(lambda x: len(x)<6, FRUIT)

def main():
    ''' main function '''
    print(f'[-] Square of 5 is {SQUARE(5)}')
    print(f'[-] Add 5 and 10 is {ADD(5, 10)}')
    count = 0 
    for fruit in FRUIT_TITLE:
        print(f'[-] Fruit: {fruit} {FRUIT[count]}')
        count += 1
    for fruit in FRUIT_FILTER:
        print(f'[-] Filter Fruit: {fruit}')
if __name__ == '__main__':
    main()
