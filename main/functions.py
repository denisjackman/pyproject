'''
    a list of useful functions buily in python
'''


def get mean(input_list):
    '''
        given a list get the mean from the list and return it
    '''
    result = 0
    return result


def get_median(input_list):
    '''
        given a list get the median from the list and return it
    '''
    result = 0
    return result


def get_mode(input_list):
    '''
        givena list get the mode and return it
    '''
    result = 0
    return result


def get_fib(number, start):
    '''
        (int, int) -> int
        Returns the nth Fibonacci number where start defines whether the squence
        starts at 0 or 1 and n is a whole number greater than or equal to 1
        >>>get_fib(1,0)
        0
        >>>get_fib(1,1)
        1
        >>>get_fib(5,1)
        5
        '''

    # define first two numbers as 0,1 or 1,1
    oldest = start
    older = 1
    # begin iterating through sequence
    for item in range(number):
        # first number as defined
        if item == 0:
            current = oldest
        # second number as defined
        elif item == 1:
            current = older
        # all other numbers are the sum of the previous two numbers
        else:
            current = older + oldest
            # re-label oldest and older for next step only if we are outside
            # of the first pre-defined two
            oldest = older
            older = current
    # return last number in sequence
    return current


def main():
    '''
        main routine
    '''
    print("Starting now : ")
    print("fib function")
    print("fib test 1 :",get_fib(1,0)==0)
    print("fib test 2 :",get_fib(1,1)==1)
    print("fib test 3 :",get_fib(5,1)==5)
    print("Ending now")


if __name__ == '__main__':
    main()
