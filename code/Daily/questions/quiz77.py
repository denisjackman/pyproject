''' quiz77

what is the output of this
a) 34
b) 23
c) 87

The answer is a) 34

The explanation the slice is minus two
so it count back back from the end of the list
87 then 34 and then we print the answer which is 34
'''


def main():
    ''' main function'''
    a = [12, 23, 34, 87]
    b = a[-2]
    print(b)


if __name__ == '__main__':
    main()
