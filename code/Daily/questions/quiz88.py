''' quiz 88
What is the output of the following code?
A) 10
B) 11
C) 18
D) 20

The answer is :
D) 20

The explanation is as follows:
i = 9 and the while loop will run until i % 5 == 0
i = 9 + 1 = 10
10 % 5 == 0
The while loop will exit and the else block will execute
i = 10 * 2 = 20
The output will be 20


'''


def main():
    '''main function'''
    i = 9
    while i % 5 != 0:
        i = i + 1
    i = i * 2
    print(i)


if __name__ == '__main__':
    main()
