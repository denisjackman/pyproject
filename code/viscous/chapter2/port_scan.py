''' Port scanner using the djportscan module '''
import sys
import argparse
import socket
import threading


def port_scan(tgt_host, tgt_ports):
    ''' Scan ports on target host '''
    try:
        tgt_ip = socket.gethostbyname(tgt_host)
    except:  # pylint: disable=bare-except
        print(f"[-] Cannot resolve '{tgt_host}': Unknown host")
        return
    try:
        tgtName = socket.gethostbyaddr(tgt_ip)
        print(f'[+] Scan results for: {tgtName[0]}')
    except:  # pylint: disable=bare-except # noqa: E722
        print(f'[+] Scan results for: {tgt_ip}')
    socket.setdefaulttimeout(1)
    for tgt_port in tgt_ports:
        print(f'[-] Scanning port {tgt_port}')
        t = threading.Thread(target=conn_scan,
                             args=(tgt_host,
                                   int(tgt_port)))
        t.start()


def conn_scan(tgt_host, tgt_port):
    ''' Connect to target host and port '''
    screen_lock = threading.Semaphore(value=1)
    try:
        conn_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn_skt.connect((tgt_host, tgt_port))
        conn_skt.send(b'ViolentPython\r\n')
        results = conn_skt.recv(100)
        screen_lock.acquire()  # pylint: disable=R1732
        print(f'[+] {tgt_port}/tcp open')
        print(f'[+] {results}')
        conn_skt.close()
    except OSError:
        screen_lock.acquire()  # pylint: disable=R1732
        print(f'[-] {tgt_port}/tcp closed')
    finally:
        screen_lock.release()
        conn_skt.close()


def main():
    ''' Main function '''
    print('[+] Starting port scan')
    parser = argparse.ArgumentParser(
        usage='port_scan.py -H TARGET_HOST -p TARGET_PORTS'
              '\nexample: python3 port_scan.py -H scanme.nmap.org -p 21,80')

    parser.add_argument('-H', type=str, metavar='TARGET_HOST',
                        help='specify target host (IP address or domain name)')
    parser.add_argument('-p',
                        required=True,
                        type=str,
                        metavar='TARGET_PORTS',
                        help='specify target port[s] separated by comma '
                             '(no spaces)')
    args = parser.parse_args()
    args.tgt_host = str(args.H)
    args.tgt_ports = str(args.p).split(',')
    if (args.tgt_host is None) | (args.tgt_ports[0] is None):
        print("[-] You must specify a target host and port[s].")
        print(parser.usage)
        sys.exit(0)

    port_scan(args.tgt_host, args.tgt_ports)


if __name__ == '__main__':
    print('[+] Port scan starting')
    main()
    print('[+] Port scan complete')
