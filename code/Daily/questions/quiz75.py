''' quiz75

what is the output of this
a) 1
b) 2
c) 3
d) 4

The answer is c) 3

The explanation is the numeric value of True is 1 and False is 0
the statement (a == 2) which is False and by defintion 0
b is then equal to zero
having three added to b means it is three when printed
'''


def main():
    ''' main function'''
    a = 5
    b = a == 2
    print(b + 3)


if __name__ == '__main__':
    main()
