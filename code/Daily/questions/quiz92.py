''' quiz 92

What is the value of x after the following code is executed?

a) 19
b) 21
c) 18
d) 20

The correct answer is: b) 21

The explanation is that the while loop will run until x is greater than
or equal to 20. The loop will run 7 times, and x will be incremented by
3 each time. The loop will stop when x is 21, so the final value of
x will be 21.
'''


def main():
    ''' main '''
    x = 0
    while x < 20:
        x += 3
    print(x)


if __name__ == "__main__":
    main()
