''' crypto file checking '''
import crypt


def main():
    ''' main function '''
    password = crypt.crypt('egg', 'HX')
    print('[+] Checking password')
    print(f'[-] password : {password}')
    print('[+] Finished Checking password')


if __name__ == '__main__':
    main()
