''' this is a scratch test script'''


def my_fun(num):
    ''' function to add numbers from 1 to num '''
    if num == 1:
        return 1
    return num + my_fun(num - 1)


def main():
    ''' main function'''
    print(my_fun(4))


if __name__ == '__main__':
    main()
