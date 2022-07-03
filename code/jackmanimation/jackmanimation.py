#!/usr/bin/python
"""
jackmanimation.py

This is a module to contain useful functions that we may use

"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.2 $"
__date__ = "$Date: 2022/06/14 00:00:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"
import json

import math


def dist(p, q):
    '''
    Measure the distance between two spots
    '''
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


def collide(pos1, pos2, rad1, rad2):
    '''
        check for a collision between two objects
    '''
    result = False
    a = dist(pos1, pos2)
    b = rad1 + rad2
    result = a <= b
    return result


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


def heapify(arr, n, i):
    '''
        heapify routine
    '''
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(input_list):
    '''
        Heap sort routine
    '''
    arr = input_list
    n = len(arr)
    # Build max heap
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]
        # Heapify root element
        heapify(arr, i, 0)
    return arr


def quickSort(input_list):
    """ Quicksort a list

    :type input_list: list
    :param input_list: List to sort
    :returns: list -- Sorted list
    """
    result = []
    arr = input_list
    if not arr:
        return []

    pivots = [x for x in arr if x == arr[0]]
    lesser = quickSort([x for x in arr if x < arr[0]])
    greater = quickSort([x for x in arr if x > arr[0]])
    result = lesser + pivots + greater
    return result


def radixSort(input_list):
    '''
        radix sort routine
    '''
    # Find the maximum element in the input_list
    maxEl = max(input_list)

    countArrayLength = maxEl+1

    # Initialize the countArray with (max+1) zeros
    countArray = [0] * countArrayLength

    # Step 1 -> Traverse the input_list and increase
    # the corresponding count for every element by 1
    for el in input_list:
        countArray[el] += 1

    # Step 2 -> For each element in the countArray,
    # sum up its value with the value of the previous
    # element, and then store that value
    # as the value of the current element
    for i in range(1, countArrayLength):
        countArray[i] += countArray[i-1]

    # Step 3 -> Calculate element position
    # based on the countArray values
    outputArray = [0] * len(input_list)
    i = len(input_list) - 1
    while i >= 0:
        currentEl = input_list[i]
        countArray[currentEl] -= 1
        newPosition = countArray[currentEl]
        outputArray[newPosition] = currentEl
        i -= 1

    return outputArray


def getNextGap(gap):
    '''
        get the next gap
    '''
    # Shrink gap by Shrink factor
    gap = (gap * 10)/13
    if gap < 1:
        return 1
    return gap


def combSort(input_list):
    '''
        comb sort routine
    '''
    result = input_list
    note = len(result)

    # Initialize gap
    gap = note

    # Initialize swapped as true to make sure that
    # loop runs
    swapped = True

    # Keep running while gap is more than 1 and last
    # iteration caused a swap
    while gap != 1 or swapped == 1:

        # Find next gap
        gap = int(getNextGap(gap))

        # Initialize swapped as false so that we can
        # check if swap happened or not
        swapped = False

        # Compare all elements with current gap
        for item in range(0, note - gap):
            if result[item] > result[item + gap]:
                result[item], result[item + gap] = result[item + gap], result[item]
                swapped = True
    return result


def insertionSort(input_list):
    '''
        insertion sort routine
    '''
    array = input_list
    for step in range(1, len(array)):
        key = array[step]
        loop = step - 1
        while loop >= 0 and key < array[loop]:
            array[loop + 1] = array[loop]
            loop -= loop
        array[loop + 1] = key

    return array


def selectionSort(input_list):
    '''
        selection sort routine
    '''
    result = input_list
    for item in range(len(result)):
        minimum = item
        for count in range(item + 1, len(result)):
            if result[count] < result[minimum]:
                minimum = count
        if minimum != item:
            result[item], result[minimum] = result[minimum], result[item]
    return result


def mergeSort(input_list):
    '''
        this is a merge sort routine
    '''
    my_list = input_list
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left = my_list[:mid]
        right = my_list[mid:]

        # recursive call on each half
        left = mergeSort(left)
        right = mergeSort(right)

        item = 0
        count = 0
        loop = 0

        while item < len(left) and count < len(right):
            if left[item] <= right[count]:
                my_list[loop] = left[item]
                item += 1
            else:
                my_list[loop] = right[count]
                count += 1
            loop += 1
        while item < len(left):
            my_list[loop] = left[item]
            item += 1
            loop += 1

        while count < len(right):
            my_list[loop] = right[count]
            count += 1
            loop += 1
    return my_list


def bubbleSort(input_list):
    '''
        bubblesort routine
    '''
    length = len(input_list)
    for i in range(length - 1):
        for j in range(length-1-i):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
    return input_list


def reverse_string(input_string):
    '''
        simple function to reverse a string
    '''
    result = input_string[::-1]
    return result



def credscheck(file_details):
    """
        This function gathers the credentials needed to open anything
    """

    credentials = file_details
    try:
        with open(credentials, encoding="utf8") as creds_file:
            creds = json.load(creds_file)
    except Exception as err:
        message = f'Danger! Danger! Will Robinson!: {err}'
        print(message)
        return []
    else:
        print("Secrets loaded OK")
    creds_file.close()
    return creds


def fileread(filename):
    """
        this is a file read function
    """
    result = []
    with open(filename, 'r',  encoding="utf8") as inputfile:
        for item in inputfile:
            result.append(item)
    inputfile.close()
    return result


def main():
    """
        This is the main routine for the program
        for this module the routine runs basic checks on the function
        that are described within.
    """
    print("Starting the sequence:")

    testcreds = credscheck("credtest.json")
    if (testcreds["checkTest"] == "test") and (len(fileread("test.txt")) == 5):
        print('All systems nominal')

    print(" reverse a string            : :" + reverse_string('namkcaJ sineD')+':')
    list1 = [100, 10, 3, 56, 4, 2, 65, 76, 23]
    list2 = [2, 3, 4, 10, 23, 56, 65, 76, 100]
    list3 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    list4 = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print("bubble sort     : ", list1, bubbleSort(list1) == list2)
    print("bubble sort     : ", list3, bubbleSort(list3) == list4)
    print("merge Sort      : ", list1, mergeSort(list1) == list2)
    print("merge Sort      : ", list3, mergeSort(list3) == list4)
    print("selection Sort  : ", list1, selectionSort(list1) == list2)
    print("selection Sort  : ", list3, selectionSort(list3) == list4)
    print("insertion Sort  : ", list1, insertionSort(list1) == list2)
    print("insertion Sort  : ", list3, insertionSort(list3) == list4)
    print("radix Sort      : ", list1, radixSort(list1) == list2)
    print("radix Sort      : ", list3, radixSort(list3) == list4)
    print("comb Sort       : ", list1, combSort(list1) == list2)
    print("comb Sort       : ", list3, combSort(list3) == list4)
    print("heap Sort       : ", list1, heapSort(list1) == list2)
    print("heap Sort       : ", list3, heapSort(list3) == list4)
    print("quick Sort      : ", list1, quickSort(list1) == list2)
    print("quick Sort      : ", list3, quickSort(list3) == list4)
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
    x1 = dist([10, 0], [0, 0])
    x2 = dist([0, 0], [100, 100])
    print("dist([10,0],[0,0]),10", x1, 10, x1 == 10)
    print("dist([0,0],[100,100]),141.4213562373095", x2,
          141.4213562373095, x2 == 141.4213562373095)
    print("finishing up and closing down:")


if __name__ == '__main__':
    main()
