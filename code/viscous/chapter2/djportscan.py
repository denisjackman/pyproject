''' Port scanner using the djportscan module '''
import sys
import optparse
from socket import socket, gethostbyname, gethostbyaddr, AF_INET, SOCK_STREAM, setdefaulttimeout
from threading import Thread, Semaphore

screenLock = Semaphore(value=1)

def connScan(tgtHost, tgtPort):
    ''' Connect to target host and port '''
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print(f'[+] {tgtPort}/tcp open')
        print(f'[+] {str(results)}')
        connSkt.close()
    except: # pylint: disable=bare-except
        screenLock.acquire()
        print(f'[-] {tgtPort}/tcp closed')

def portScan(tgtHost, tgtPorts):
    ''' Scan ports on target host '''
    try:
        tgtIP = gethostbyname(tgtHost)
    except: # pylint: disable=bare-except
        print(f"[-] Cannot resolve '{tgtHost}': Unknown host")
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print(f'[+] Scan results for: {tgtName[0]}')
    except: # pylint: disable=bare-except
        print(f'[+] Scan results for: {tgtIP}')
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print(f'[-] Scanning port {tgtPort}')
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()

def main():
    ''' Main function '''
    print('[+] Starting port scan')
    parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target port[s] separated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost is None) | (tgtPorts[0] is None):
        print("[-] You must specify a target host and port[s].")
        print(parser.usage)
        sys.exit(0)
    portScan(tgtHost, tgtPorts)
    print('[+] Port scan complete')

if __name__ == '__main__':
    main()
