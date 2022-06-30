'''
    sort routines
'''


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
    print("heap Sort       : ", list1, heapSort(list1) == list2)
    print("heap Sort       : ", list3, heapSort(list3) == list4)
    print("quick Sort      : ", list1, quickSort(list1) == list2)
    print("quick Sort      : ", list3, quickSort(list3) == list4)


if __name__ == '__main__':
    main()
