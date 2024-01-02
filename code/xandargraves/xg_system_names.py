''' This is a list of systems for the imperial side of the Xander Graves UNiverse'''

DATA_DIR = 'G:/Writing/Fiction/Stories/Xander graves/Data'
SUFFIXS = 'suffixs.dat'
TOPPERS = 'toppers.dat'
PREFIXS = 'prefixs.dat'

def read_file(file_name):
    ''' This is the read file function'''
    print('[o] This is the read file function starting')
    result = []
    with open(file_name, 'r', encoding='utf-8-sig') as file_handle:
        for line in file_handle:
            result.append(line.strip())
    print('[o] This is the read file function ending')
    return result

def main():
    ''' This is the main function'''
    print('[-] This is the main function starting')
    print(f'[-] {DATA_DIR}')
    suffix_list = read_file(f'{DATA_DIR}/{SUFFIXS}')
    topper_list = read_file(f'{DATA_DIR}/{TOPPERS}')
    prefix_list = read_file(f'{DATA_DIR}/{PREFIXS}')   
    print(f'[-] {suffix_list}')
    print(f'[-] {topper_list}')
    print(f'[-] {prefix_list}')
    print(f'[-] {len(suffix_list)}')
    print(f'[-] {len(topper_list)}')
    print(f'[-] {len(prefix_list)}')
    print('[-] This is the main function ending')

if __name__ == '__main__':
    print('[+] This is the xg_system_names program starting')
    main()
    print('[+] This is the xg_system_names program ending')
