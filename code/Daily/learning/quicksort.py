''' quick sort '''


def learning_quick_sort(input_list):
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
    qslesser = learning_quick_sort([x for x in arr if x < arr[0]])
    qsgreater = learning_quick_sort([x for x in arr if x > arr[0]])
    result = qslesser + qspivots + qsgreater
    return result


def main():
    ''' main function '''
    sortlist = [9, 1, 8, 7, 10, 6, 2, 3, 4, 5]
    resultsortlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print('[-] quick sort list before '
          f'{sortlist}')
    print('[-] quick sort list after  '
          f'{learning_quick_sort(sortlist)}')
    print(f'[-] {sortlist == resultsortlist}')


if __name__ == "__main__":
    main()
