''' quiz 89
what is the output of the following code?
A) 8
B) 2
C) 8.0
D) 26

the answer is C) 8.0
the explanation is that the code will convert the two strings
the first to a integer
the second to a float
Then it will add the two numbers together
As the result is a float, the print statement will print the result as a float
'''


def main():
    ''' main function'''
    a = "2"
    b = "6"
    print(f"{int(a) + float(b)}")


if __name__ == '__main__':
    main()
