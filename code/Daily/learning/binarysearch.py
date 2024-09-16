''' Binary Search
This routine searchs using a binary search for a ojbject in the list
if the object is in the list it return the postion of the object in the list
if the objectr is not in the list it returns False
'''


def learning_binary_search(targetlist, low, high, target):
    ''' Binary Search Algorithm in Python '''
    result = False
    if high >= low:
        mid = (high + low) // 2
        if targetlist[mid] == target:
            return mid
        if targetlist[mid] > target:
            return learning_binary_search(targetlist, low, mid - 1, target)
        return learning_binary_search(targetlist, mid + 1, high, target)
    return result


def main():
    ''' main function '''
    searchlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('[-] Binary looking for 5 in searchlist '
          f'{learning_binary_search(searchlist, 0, len(searchlist)-1, 5)}')
    print('[-] Binary looking for 20 in searchlist '
          f'{learning_binary_search(searchlist, 0, len(searchlist)-1, 20)}')


if __name__ == "__main__":
    main()
