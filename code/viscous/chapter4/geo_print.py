''' Geo print'''
import socket
import argparse
import dpkt
import geoip2.database


def ret_geo_str(ip):
    ''' return geo string'''
    try:
        with geoip2.database.Reader(r'Z:\violent-python3\chapter04\geolite2_city.mmdb') as gi:
            rec = gi.city(ip)
            city = rec.city.name
            country = rec.country.name
            if city != '':
                geo_loc = f'{city}, {country}'
            else:
                geo_loc = country
            return geo_loc
    except Exception as e:
        print(f'{"":>3}[-] Exception: {e.__class__.__name__}')
        return 'Unregistered'


def print_pcap(pcap_file):
    ''' print direction of the flow'''
    for ts, buf in pcap_file:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print(f'[+] Source: {ret_geo_str(src)} --> Destination: {ret_geo_str(dst)}')
        except Exception as e:
            print(f'{"":>3}[-] Exception: {e.__class__.__name__}')


def main():
    ''' main function'''
    parser = argparse.ArgumentParser(usage='python geo_print.py PCAP_FILE')
    parser.add_argument('pcap_file', type=str, metavar='PCAP_FILE', help='specify pcap filename')
    args = parser.parse_args()
    pcap_file = args.pcap_file
    with open(pcap_file, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        print_pcap(pcap)


if __name__ == '__main__':
    main()
