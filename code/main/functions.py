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


def findmissingnumbers(number_list):
    '''
        given a list (number_list)
        find the missing numbers in the list
    '''
    numbers = set(number_list)
    length = len(number_list)
    output = []
    for item in range(1, length + 1):
        if item not in numbers:
            output.append(item)
    return output

def main():
    '''
        main routine
    '''
    print("Starting now : ")
    arr = ['t','u','t','o','r','i','a','l']
    x = 'a'
    print("element found at index "+str(linearsearch(arr,x)))
    print("Ending now")
    listofnumbers = [1, 2, 3, 5, 6, 7, 8, 9]
    print(findmissingnumbers(listofnumbers))


if __name__ == '__main__':
    main()
