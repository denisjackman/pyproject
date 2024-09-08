''' quiz 78

what is the output from the following code

a) hello5
b) 5hello
c) hello+5
d) TypeError

The answer is d) TypeError

The explanation is the variables are of two different types
and cannot be mashed together
'''


def main():
    ''' main function'''
    x = 5
    y = "hello"
    print(x + y)


if __name__ == '__main__':
    try:
        main()
    except TypeError as e:
        print(e)
