''' Quiz 87
What is the output of the following code?

a: [0, 9, 7]
b: [0, 9, 8, 7, 4]
c: [9, 8, 7]
d: [0, 1, 2, 3, 4]

the answer is : a: [0, 9, 8, 7, 4]

The explanation is as follows:
The code snippet is using list slicing to replace the elements in the list x.
The statement x[1:4] = [9, 8, 7]
replaces the elements at index 1, 2, and 3 ([1,2,3,])
with the elements 9, 8, and 7 respectively.

'''


def main():
    ''' main function '''
    x = [0, 1, 2, 3, 4]
    x[1:4] = [9, 8, 7]
    print(x)


if __name__ == "__main__":
    main()
