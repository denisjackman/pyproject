''' sort the requirements file into a unique item list '''


def unique_list(sortlist):
    ''' sort a list into a unique item list '''
    result = []
    for item in sortlist:
        if item not in result:
            result.append(item)
        else:
            print(f'[+] Duplicate item {item.strip()}')
    return result


def main():
    ''' main routine '''
    print('[+] Starting ')
    print('[+] Reading requirements file ')
    with open(r'Z:/pyproject/requirements.txt',
              'r',
              encoding='utf-8-sig') as file:
        reqs = file.readlines()
    print(f'[-] Total requirements is {len(reqs):,}')
    print('[+] Sorting requirements file ')
    reqs.sort()
    print('[+] Removing duplicates ')
    newreqs = unique_list(reqs)
    print(f'[-] Total unique requirements is {len(newreqs):,}')
    print('[+] Writing new requirements file ')
    with open(r'Z:/pyproject/newrequirements.txt',
              'w',
              encoding='utf-8-sig') as file:
        for item in newreqs:
            file.write(item)
    print('[+] Finished')


if __name__ == '__main__':
    main()
