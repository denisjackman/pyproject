''' nmap scanner '''
import sys
import argparse
import nmap


def nmap_scan(tgt_host, tgt_ports):
    ''' Scan ports on target host '''
    nm_scan = nmap.PortScanner()
    for tgt_port in tgt_ports:
        nm_scan.scan(tgt_host, tgt_port)
        state = nm_scan[tgt_host]['tcp'][int(tgt_port)]['state']
        print(f'[*] {tgt_host} tcp/{tgt_port} {state}')


def main():
    ''' Main function '''
    print('[-] nmap scanner starting')
    parser = argparse.ArgumentParser(usage='nmap_scan.py -H TARGET_HOST -p TARGET_PORT')
    parser.add_argument('-H', metavar='TARGET_HOST', type=str, help='specify target host')
    parser.add_argument('-p', metavar='TARGET_PORT', type=str, help='specify target port[s] separated by comma')
    args = parser.parse_args()
    args.tgtHost = str(args.H)
    args.tgtPorts = str(args.p).split(',')
    if (args.tgtHost is None) | (args.tgtPorts[0] is None):
        print("[-] You must specify a target host and port[s].")
        print(parser.usage)
        sys.exit(0)
    nmap_scan(args.tgtHost, args.tgtPorts)
    print('[-] nmap scanner complete')


if __name__ == '__main__':
    main()
