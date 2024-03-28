''' this is a sample tuple play file '''


def main():
    ''' main function '''
    new_tuple = ("apple",
                 "banana",
                 "cherry",
                 "orange",
                 "kiwi",
                 "melon",
                 "mango")
    print('[-] Main function is running')
    print('[*] Updating a tuple')
    print(f'[*] {new_tuple}')
    new_tuple = update_tuple(new_tuple, 2, 'blueberry')
    print(f'[*] {new_tuple}')
    new_tuple = append_tuple(new_tuple, 'strawberry')
    print(f'[*] {new_tuple}')
    new_tuple = append_tuple(new_tuple, 'cherry')
    print(f'[*] {new_tuple}')
    new_tuple = remove_tuple(new_tuple, 'blueberry')
    print(f'[*] {new_tuple}')
    new_tuple = append_tuple(new_tuple, 'blueberry')
    print(f'[*] {new_tuple}')
    print('[-] Main function is complete')


def update_tuple(ut_tuple, ut_index, ut_value):
    ''' update tuple '''
    print('[-] Updating the tuple')
    ut_list = list(ut_tuple)
    ut_list[ut_index] = ut_value
    print('[-] Finished updating the tuple')
    return tuple(ut_list)


def append_tuple(at_tuple, at_value):
    ''' append tuple '''
    print('[-] Appending the tuple')
    at_list = list(at_tuple)
    at_list.append(at_value)
    print('[-] Finished appending the tuple')
    return tuple(at_list)


def remove_tuple(rt_tuple, rt_value):
    ''' remove tuple '''
    print('[-] Removing the tuple')
    rt_list = list(rt_tuple)
    rt_list.remove(rt_value)
    print('[-] Finished removing the tuple')
    return tuple(rt_list)


def tuple_to_list(tt_tuple):
    ''' tuple to list '''
    print('[-] Converting the tuple to a list')
    print('[-] Finished converting the tuple to a list')
    return list(tt_tuple)


if __name__ == '__main__':
    print('[+] Starting the program')
    main()
    print('[+] Ending the program')
