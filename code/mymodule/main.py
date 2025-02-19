''' This is a primer for using custom modules in Python.
    https://www.youtube.com/watch?v=GxCXiSkm6no
    https://www.youtube.com/watch?v=0oTh1CXRaQ0
'''
from functionality import add, sub, mul, div
from othermodule import second
from othermodule.submodule import third, fourth


def main():
    ''' This is the main function'''
    print('[+] This is the main function starting')
    print(f'[+] 10 + 20 = {add(10, 20)}')
    print(f'[+] 10 - 20 = {sub(10, 20)}')
    print(f'[+] 10 * 20 = {mul(10, 20)}')
    print(f'[+] 20 / 10 = {div(20, 10)}')
    print('[+] This is the main function ending')
    second.myfunction()
    third.another_function()
    fourth.last_fct()


if __name__ == '__main__':
    main()
