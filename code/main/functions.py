'''
    a list of useful functions built in python
'''


def linearsearch(input_list,search_item):
    '''
        linear search
    '''
    result = -1
    for item in range(len(input_list)):
        if input_list[item] == search_item:
            result = item
    return result


def main():
    '''
        main routine
    '''
    print("Starting now : ")
    arr = ['t','u','t','o','r','i','a','l']
    x = 'a'
    print("element found at index "+str(linearsearch(arr,x)))
    print("Ending now")


if __name__ == '__main__':
    main()
