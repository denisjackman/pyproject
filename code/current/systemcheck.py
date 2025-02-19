''' sys check.py '''
import os
import platform

RUN_NAME = os.path.basename(__file__)
OS_NAME = platform.system()
RUN_CHECK = False

if OS_NAME == 'Windows':
    RUN_CHECK = True


def sys_check():
    ''' sys check '''
    print(f'[-] OS: {OS_NAME}')


def main():
    ''' main '''
    if RUN_CHECK:
        sys_check()
    else:
        print(f'[-] {OS_NAME} not supported')


if __name__ == '__main__':
    print(f'[*] {RUN_NAME} starting')
    main()
    print(f'[*] {RUN_NAME} ending')
