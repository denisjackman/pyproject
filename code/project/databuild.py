'''Data builder '''

from faker import Faker

def main():
    '''Main function'''
    print('[+] Main Function Starting...')
    fake = Faker()
    for _ in range(10):
        print(f'[*] {fake.name()}')
        print(f'[*] {fake.address()}')
        print(f'[*] {fake.email()}')
        print(f'[*] {fake.text()}')
        print(f'[*] {fake.url()}')
        print(f'[*] {fake.date()}')
        print(f'[*] {fake.country()}')
    print('[-] Main Function Finished.')

if __name__ == '__main__':
    main()
