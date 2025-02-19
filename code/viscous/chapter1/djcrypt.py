''' crypto file checking '''
from passlib.hash import pbkdf2_sha256 as passlib


def main():
    ''' main function '''
    custom_pass = passlib.using(rounds=5000, salt_size=16)
    password_string = 'egg'
    nu_password = custom_pass.hash(password_string)
    print('[+] Checking password')
    print(f'[-] password : {nu_password}')
    print('[+] Finished Checking password')


if __name__ == '__main__':
    main()
