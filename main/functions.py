'''
    a list of useful functions buily in python
'''


def get_mean(input_list):
    '''
        given a list get the mean from the list and return it
    '''
    result = 0
    result = sum(input_list)/len(input_list)
    return result


def get_median(input_list):
    '''
        given a list get the median from the list and return it
    '''
    result = 0
    work_list = input_list
    work_list.sort()
    if len(work_list) % 2 == 0:
        mid_one = work_list[len(work_list)//2]
        mid_two = work_list[len(work_list)//2 - 1]
        result = (mid_one + mid_two) / 2
    else:
        result = work_list[len(work_list)//2]
    return result


def get_mode(input_list):
    '''
        given a list get the mode and return it
    '''
    result = 0
    frequency = {}
    for item in input_list:
        frequency.setdefault(item,0)
        frequency[item] += 1
    frequent = max(frequency.values())
    for item, content in frequency.items():
        if content == frequent:
            result = item
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
    print("fib test 1  :",get_fib(1,0)==0)
    print("fib test 2  :",get_fib(1,1)==1)
    print("fib test 3  :",get_fib(5,1)==5)
    test_list  = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
    print("Mean function")
    print("Mean test 1 :", get_mean(test_list) == 20.2)
    print("median function")
    print("Median test 1 :", get_median(test_list) == 20.0 )
    print("mode function")
    print("Mode test 1   :", get_mode(test_list) == 20)
    print("Ending now")

if __name__ == '__main__':
    main()
