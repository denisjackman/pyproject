'''This is a set of list comprehension examples  '''


def main():
    ''' main function '''
    print('[+] Starting list comprehension examples')
    fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
    newlist = []
    for x in fruits:
        if 'a' in x:
            newlist.append(x)
    listnew = [x for x in fruits if x != 'apple']
    newlistnew = [x for x in fruits]  # pylint: disable=R1721
    nlist = [x for x in range(10)]  # pylint: disable=R1721
    slist = [x for x in range(10) if x < 5]
    ulist = [x.upper() for x in fruits]
    hlist = ['hello' for x in fruits]
    blist = [x if x != 'banana' else 'orange' for x in fruits]
    print(f'[-] fruits list : {fruits}')
    print(f'[-] newlist list : {newlist}')
    print(f'[-] listnew list : {listnew}')
    print(f'[-] newlistnew list : {newlistnew}')
    print(f'[-] nlist list : {nlist}')
    print(f'[-] slist list : {slist}')
    print(f'[-] ulist list : {ulist}')
    print(f'[-] hlist list : {hlist}')
    print(f'[-] blist list : {blist}')
    print('[+] Finish list comprehension examples')


if __name__ == '__main__':
    main()
