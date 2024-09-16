'''quiz86

what is the output of this code snippet?
a: 21
b: 18
c: 20
d: 24

the answer is: a

the explanation is:
the code snippet is a while loop that increments x by 3
until x is greater than 20
the loop will run 7 times, and the final value of x will be 21

'''


def main():
    ''' main function '''
    x = 0
    while x < 20:
        x = x + 3
    print(x)


if __name__ == "__main__":
    main()
