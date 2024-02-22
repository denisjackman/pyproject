''' geocoder example '''
import geocoder as geo


def main():
    ''' main function '''
    ip_address = geo.ip('me')
    print(f'ip_address: {ip_address}')
    print(f'ip_address.latlng: {ip_address.latlng}')
    print(f'ip_address.city: {ip_address.city}')
    print(f'ip_address.state: {ip_address.state}')
    print(f'ip_address.country: {ip_address.country}')
    print(f'ip_address.postal: {ip_address.postal}')
    print(f'ip_address.address: {ip_address.address}')


if __name__ == '__main__':
    main()
