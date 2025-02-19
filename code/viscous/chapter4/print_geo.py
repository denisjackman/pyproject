''' print geo data '''
import argparse
import geoip2.database


def print_record(target_ip):
    ''' print geo data '''
    with geoip2.database.Reader(r'Z:\violent-python3\chapter04\geolite2_city.mmdb') as reader:
        response = reader.city(target_ip)
        print(f'Country: {response.country.name}')
        print(f'City: {response.city.name}')
        print(f'Latitude: {response.location.latitude}')
        print(f'Longitude: {response.location.longitude}')


def main():
    ''' main '''
    parser = argparse.ArgumentParser()
    parser.add_argument('target_ip', help='target ip address')
    args = parser.parse_args()
    print_record(args.target_ip)


if __name__ == '__main__':
    main()
