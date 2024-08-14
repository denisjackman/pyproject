'''
This is a list of systems for the
imperial side of the Xander Graves Universe
'''
import random

DATA_DIR = 'G:/Writing/Fiction/Stories/Xander graves/Data'
SUFFIXS = 'suffixs.dat'
TOPPERS = 'toppers.dat'
PREFIXS = 'prefixs.dat'
RESULT = 'result.dat'


def read_file(file_name, verbose=False):
    ''' This is the read file function'''
    if verbose:
        print('[o] This is the read file function starting')
    result = []
    with open(file_name, 'r', encoding='utf-8-sig') as file_handle:
        for line in file_handle:
            result.append(line.strip())
    if verbose:
        print('[o] This is the read file function ending')
    return result


def generate_names(gn_suffix, gn_topper, gn_prefix, verbose=False):
    ''' This is the generate names function'''
    if verbose:
        print('[o] This is the generate names function starting')
    suffix_rn = random.randint(0, len(gn_suffix)-1)
    topper_rn = random.randint(0, len(gn_topper)-1)
    prefix_rn = random.randint(0, len(gn_prefix)-1)
    result = f'{gn_prefix[prefix_rn]}{gn_suffix[suffix_rn]}'
    if random.randint(0, 1) == 1:
        result = f'{gn_topper[topper_rn]} {result}'
    if verbose:
        print('[o] This is the generate names function ending')
    return result


def write_file(file_name, write_list, verbose=False):
    ''' This is the write file function'''
    if verbose:
        print('[o] This is the write file function starting')
    with open(file_name, 'w', encoding='utf-8-sig') as file_handle:
        for item in write_list:
            file_handle.write(f'{item}\n')
    if verbose:
        print('[o] This is the write file function ending')


def main():
    ''' This is the main function'''
    print('[-] This is the main function starting')
    print(f'[-] {DATA_DIR}')
    suffix_list = read_file(f'{DATA_DIR}/{SUFFIXS}')
    topper_list = read_file(f'{DATA_DIR}/{TOPPERS}')
    prefix_list = read_file(f'{DATA_DIR}/{PREFIXS}')
    print(f'[-] {len(suffix_list)}')
    print(f'[-] {len(topper_list)}')
    print(f'[-] {len(prefix_list)}')
    namelist = []
    for _ in range(1000):
        namelist.append(f'{generate_names(suffix_list, topper_list, prefix_list)}')
    namelist.sort()
    print(f'[-] before {len(namelist)}')
    namelist = list(dict.fromkeys(namelist))
    print(f'[-] after {len(namelist)}')
    write_file(f'{DATA_DIR}/{RESULT}', namelist)
    print('[-] This is the main function ending')


if __name__ == '__main__':
    print('[+] This is the xg_system_names program starting')
    main()
    print('[+] This is the xg_system_names program ending')
