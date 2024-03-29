''' zip play example '''
from itertools import zip_longest


def main():
    ''' main function '''
    print('[*] zip play example start')
    names = ['Cecilia',
             'Lise',
             'Marie',
             'Rohit',
             'Sachin',
             'Dhoni',
             'Steve']
    scores = [60, 70, 80, 90, 100, 110, 120]
    ls1 = [1, 2, 3, 4, 5, 6, 7]
    ls2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    newlist = list(zip(names, scores))
    newls = list(zip_longest(ls1, ls2, fillvalue='-x-'))
    print(f'[-] {newlist}')
    print(f'[-] {newls}')
    for name, score in zip(names, scores):
        print(f'[-] {name} -> {score}')
    print('[*] zip play example end')


if __name__ == '__main__':
    main()
