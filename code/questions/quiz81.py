''' quiz 81

what will the output from this code be

a [1,2,3,4]
b [100,2,3,4]
c [100,2]
d [100,2,3,4,5]

The answer is D

the explanation is
'''


def main():
    ''' main function '''
    x = [1, 2, 3, 4, 5]
    y = x
    y[0] = 100
    print(x)


if __name__ == '__main__':
    main()
