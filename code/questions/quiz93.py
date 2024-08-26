''' Question 93
What is the output of the following code?
a) 21
b) 15
c) 11
d) None

Answer: a) 21

Explanation:
The function foo takes two positional arguments a and b,
and two variable arguments *args and **kwargs.
'''


def quiz93(a, b, *args, **kwargs):
    ''' Function foo '''
    return a+b+sum(args)+sum(kwargs.values())


def main():
    ''' Main function '''
    print(quiz93(1, 2, 3, 4, x=5, y=6))


if __name__ == "__main__":
    main()
