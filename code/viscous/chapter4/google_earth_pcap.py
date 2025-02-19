''' Geo print'''
import socket
import argparse
import dpkt
import geoip2.database


def get_KML(ip):
    ''' return KML string'''
    kml = ''
    with geoip2.database.Reader(r'Y:\violent-python3\chapter04\geolite2_city.mmdb') as gi:
        rec = gi.city(ip)
    try:
        latitude = rec.location.latitude
        longitude = rec.location.longitude
        kml = (f'<Placemark>\n'
               f'<name>{ip}</name>\n'
               f'<Point>\n'
               f'<coordinates>{longitude},{latitude}</coordinates>\n'
               f'</Point>\n'
               f'</Placemark>\n')
    except Exception as e:
        print(f'{"":>3}[-] Exception: {e.__class__.__name__}')
    return kml


def plot_IPs(pcap_file):
    ''' plot IPs'''
    kml_pts = ''
    for ts, buf in pcap_file:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            src_kml = get_KML(src)
            dst = socket.inet_ntoa(ip.dst)
            dst_kml = get_KML(dst)
            kml_pts = kml_pts + src_kml + dst_kml
        except Exception as e:
            print(f'{"":>3}[-] Exception: {e.__class__.__name__}')
    return kml_pts


def main():
    ''' main function'''
    parser = argparse.ArgumentParser(usage='python google_earth_pcap.py PCAP_FILE')
    parser.add_argument('pcap_file', type=str, metavar='PCAP_FILE', help='specify pcap filename')
    args = parser.parse_args()
    pcap_file = args.pcap_file
    with open(pcap_file, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        kml_header = '<?xml version="1.0" encoding="UTF-8"?>\n' \
                     '<kml xmlns="http://www.opengis.net/kml/2.2"\n' \
                     'xmlns:gx="http://www.google.com/kml/ext/2.2"\n ' \
                     'xmlns:kml="http://www.opengis.net/kml/2.2"\n ' \
                     'xmlns:atom="http://www.w3.org/2005/Atom">' \
                     '<Document>\n' \
                     '<name>Untitled</name>\n'
        kml_footer = '</Document>\n' \
                     '</kml>\n'
        kmldoc = f'{kml_header}{plot_IPs(pcap)}{kml_footer}'
        print(kmldoc)


if __name__ == '__main__':
    main()
