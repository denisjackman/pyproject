''' this is a list play file '''


def main():
    ''' main function '''
    print('[-] Main function is running')
    d = {1: 2, 3: 4, 6: 727, 83: 422}
    lst = [1, 82, -6, 4, 3, 8]
    states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
              'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia',
              'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas',
              'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts',
              'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana',
              'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
              'New Mexico', 'New York', 'North Carolina', 'North Dakota',
              'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island',
              'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah',
              'Vermont', 'Virginia', 'Washington', 'West Virginia',
              'Wisconsin', 'Wyoming']

    print('[*] Making a copy of the list')
    new_states = states.copy()
    print('[*] Printing the length of the new list')
    print(f'[*] before ({len(states)}) after ({len(new_states)})')
    for state in new_states:
        if state[0] == 'N':
            print(f'{state}')
    print('[*] Removing Nevada')
    new_states.remove('Nevada')
    for state in new_states:
        if state[0] == 'N':
            print(f'{state}')
    print('[*] Printing the new length of the new list')
    print(f'[*] before ({len(states)}) after ({len(new_states)})')
    print('[*] clearing the list')
    new_states.clear()
    print(f'[*] before ({len(states)}) after ({len(new_states)})')
    new_states = states.copy()
    new_states.sort()
    print('[*] Printing the sorted list')
    for state in new_states:
        print(f'\t{state}')
    print(f'[*] {lst[2]}')
    print(f'[*] {lst[-1]}')
    print(f'[*] This {4 in lst}')
    print(f'[*] {lst.index(8)}')
    print(f'[*] {lst.index(4)}')
    print(f'[*] {lst}')
    lst.append(632)
    print(f'[*] {lst}')
    print(f'[*] {lst.pop()}')
    print(f'[*] {lst}')
    print(f'[*] {lst.pop(4)}')
    print(f'[*] {lst}')
    if 4 in lst:
        lst.remove(4)
    print(f'[*] {lst}')
    print(f'[*] {d}')
    d[1] = 37
    print(f'[*] {d}')
    print('[-] Main function is done')


if __name__ == "__main__":
    print('[+] Running listplay.py')
    main()
    print('[+] Finished listplay.py')
