''' linear search algorithm in python '''
# Search Algorithms
#      Liner Search Algorithm          - DONE
#      Binary Search Algorithm         - DONE
#      Depth First Search Algorithm
#      Breadth First Search Algorithm

# Sort Algorithms
#      insertion sort                  - DONE
#      selection sort                  - DONE
#      quick sort                      - DONE
#      Merge sort                      - DONE
#      heap sort
#      counting sort


def quick_sort(input_list):
    """ Quicksort a list
    :type input_list: list
    :param input_list: List to sort
    :returns: list -- Sorted list
    """
    result = []
    arr = input_list
    if not arr:
        return []

    qspivots = [x for x in arr if x == arr[0]]
    qslesser = quick_sort([x for x in arr if x < arr[0]])
    qsgreater = quick_sort([x for x in arr if x > arr[0]])
    result = qslesser + qspivots + qsgreater
    return result


def radix_sort(input_list):
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


def insertion_sort(input_list):
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


def selection_sort(input_list):
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


def merge_sort(input_list):
    '''
        this is a merge sort routine
    '''
    my_list = input_list
    if len(my_list) > 1:
        ms_mid = len(my_list) // 2
        ms_left = my_list[:ms_mid]
        ms_right = my_list[ms_mid:]

        # recursive call on each half
        ms_left = merge_sort(ms_left)
        ms_right = merge_sort(ms_right)

        ms_item = 0
        ms_count = 0
        ms_loop = 0

        while ms_item < len(ms_left) and ms_count < len(ms_right):
            if ms_left[ms_item] <= ms_right[ms_count]:
                my_list[ms_loop] = ms_left[ms_item]
                ms_item += 1
            else:
                my_list[ms_loop] = ms_right[ms_count]
                ms_count += 1
            ms_loop += 1
        while ms_item < len(ms_left):
            my_list[ms_loop] = ms_left[ms_item]
            ms_item += 1
            ms_loop += 1

        while ms_count < len(ms_right):
            my_list[ms_loop] = ms_right[ms_count]
            ms_count += 1
            ms_loop += 1
    return my_list


def bubble_sort(input_list):
    '''
        bubblesort routine
    '''
    length = len(input_list)
    for i in range(length - 1):
        for j in range(length-1-i):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
    return input_list


def linear_search(targetlist, target):
    ''' returns the target if found, else returns None '''
    result = False
    if target in targetlist:
        for item in range(len(targetlist)):
            if targetlist[item] == target:
                return targetlist[item]
    return result


def binary_search(targetlist, low, high, target):
    ''' Binary Search Algorithm in Python '''
    result = False
    if high >= low:
        mid = (high + low) // 2
        if targetlist[mid] == target:
            return mid
        if targetlist[mid] > target:
            return binary_search(targetlist, low, mid - 1, target)
        return binary_search(targetlist, mid + 1, high, target)
    return result


def main():
    ''' main function '''
    print("[+] Linear Search Algorithm start[+]")
    searchlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('[-] Linear looking for 5 in searchlist '
          f'{linear_search(searchlist, 5)}')
    print('[-] Linear looking for 20 in searchlist'
          f'{linear_search(searchlist, 20)}')
    print('[-] Binary looking for 5 in searchlist'
          f'{binary_search(searchlist, 0, len(searchlist)-1, 5)}')
    print('[-] Binary looking for 20 in searchlist'
          f'{binary_search(searchlist, 0, len(searchlist)-1, 20)}')
    print('[+] Linear Search Algorithm finish[+]')


if __name__ == "__main__":
    main()
