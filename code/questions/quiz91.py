'''quiz91.py
what is the output of the following code?

a) 1 3 5 7 9
b) 0 2 4 6 8 10
c) 2 4 6 8 10
d) 1 2 3 4 5 6 7 8 9 10

Answer: a) 1 3 5 7 9

Explanation:
This is a simple while loop that prints the odd numbers from 1 to 10.
The loop starts with num = 0 and increments it by 1 in each iteration.
If the number is even (num % 2 == 0),
it skips to the next iteration using the continue statement.
Otherwise, it prints the number and increments it by 1.
The loop continues until num reaches 10.
So, the output is 1 3 5 7 9.

'''


def main():
    '''main function'''
    num = 0
    while num < 10:
        if num % 2 == 0:
            num += 1
            continue
        print(num)
        num += 1


if __name__ == "__main__":
    main()
