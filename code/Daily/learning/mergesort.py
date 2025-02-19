''' merge sort '''


def learning_merge_sort(input_list):
    '''
        this is a merge sort routine
    '''
    my_list = input_list
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left = my_list[:mid]
        right = my_list[mid:]

        # recursive call on each half
        left = learning_merge_sort(left)
        right = learning_merge_sort(right)

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


def main():
    ''' main function '''
    sortlist = [9, 1, 8, 7, 10, 6, 2, 3, 4, 5]
    resultsortlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print('[-] merge sort list before '
          f'{sortlist}')
    print('[-] merge sort list after  '
          f'{learning_merge_sort(sortlist)}')
    print(f'[-] {sortlist == resultsortlist}')


if __name__ == "__main__":
    main()
