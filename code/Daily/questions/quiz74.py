''' quiz74

what is the output of this code
a) 8
b) 20
c) 40
d) 30

The answer is c: 40

The explanation is that
a is given the value of 5
b remain as 2
c is given the value of 4

b and c are multiplied (8)
This result is multiplied by a (5)
giving and answer of forty (40)

'''


def func(a=1, b=2, c=2):
    ''' func '''
    return a * b * c


def main():
    ''' main function'''
    result = func(5, c=4)
    print(result)


if __name__ == '__main__':
    main()
