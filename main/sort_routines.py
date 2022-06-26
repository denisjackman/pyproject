'''
    sort routines
'''


def radixSort(inputArray):
    '''
        radix sort routine
    '''
    # Find the maximum element in the inputArray
    maxEl = max(inputArray)

    countArrayLength = maxEl+1

    # Initialize the countArray with (max+1) zeros
    countArray = [0] * countArrayLength

    # Step 1 -> Traverse the inputArray and increase
    # the corresponding count for every element by 1
    for el in inputArray:
        countArray[el] += 1

    # Step 2 -> For each element in the countArray,
    # sum up its value with the value of the previous
    # element, and then store that value
    # as the value of the current element
    for i in range(1, countArrayLength):
        countArray[i] += countArray[i-1]

    # Step 3 -> Calculate element position
    # based on the countArray values
    outputArray = [0] * len(inputArray)
    i = len(inputArray) - 1
    while i >= 0:
        currentEl = inputArray[i]
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


def combSort(arr):
    '''
        comb sort routine
    '''
    result = arr
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
    for item in range(len(result)):  # pylint: disable C0200
        minimum = item
        for count in range(item + 1, len(result)):
            if result[count] < result[minimum]:
                minimum = count
        if minimum != item:
            result[item], result[minimum] = result[minimum], result[item]
    return result


def mergeSort(sort_list):
    '''
        this is a merge sort routine
    '''
    my_list = sort_list
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


def bubbleSort(sort_list):
    '''
        bubblesort routine
    '''
    length = len(sort_list)
    for i in range(length - 1):
        for j in range(length-1-i):
            if sort_list[j] > sort_list[j+1]:
                sort_list[j], sort_list[j+1] = sort_list[j+1], sort_list[j]
    return sort_list


def main():
    '''
        this is the main routine
    '''
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


if __name__ == '__main__':
    main()
