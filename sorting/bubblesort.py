'''
    bubblesort routine
'''


def bubble_sort(input_list):
    '''
        bubblesort routine
    '''
    output_list = input_list
    length = len(output_list)
    for item in range(length - 1):
        for compare_item in range((length - 1) - item):
            if output_list[compare_item] > output_list[compare_item + 1]:
                output_list[compare_item], output_list[compare_item + 1] = output_list[compare_item + 1], output_list[compare_item]  # pylint: disable E501
    return output_list


def main():
    '''
        this is the main routine
    '''
    list1 = [100, 10, 3, 56, 4, 2, 65, 76, 23]
    list2 = [2, 3, 4, 10, 23, 56, 65, 76, 100]
    print(list1, bubble_sort(list1) == list2)


if __name__ == '__main__':
    main()
