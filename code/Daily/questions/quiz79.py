''' quiz79

how many time will the code print "Hello"
A) 2
B) 3
C) 4
D) 5

The answer is B.

The explanantion is that during the run
the first time into the loop n = 5 prints hello and then becomes 3
the second time into the loop n = 3 prints hello and then becomes 1
the third time into the loop n = 1 prints hello and then becomes -1
The last time n is now -1 and the loop is complete

'''


def main():
    ''' main function'''
    n = 5
    while n > 0:
        print("Hello")
        n -= 2


if __name__ == '__main__':
    main()
