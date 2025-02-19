''' print direction of the flow'''
import socket
import dpkt


def print_pcap(pcap):
    ''' print direction of the flow'''
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print(f'Source: {src} Destination: {dst}')
        except:  # pylint: disable=bare-except
            pass


def main():
    ''' main function'''
    with open(r'Z:\violent-python3\chapter04\geotest.pcap',
              'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        print_pcap(pcap)


if __name__ == '__main__':
    main()
