''' win reg exploration '''
import os
import platform
import ctypes
import requests
import config  # pylint: disable=E0401

RUN_NAME = os.path.basename(__file__)
OS_NAME = platform.system()
RUN_CHECK = False
IS_ADMIN = ctypes.windll.shell32.IsUserAnAdmin() != 0
WIGLE_CHECK = False

if OS_NAME == 'Windows':
    import winreg  # pylint: disable=E0401
    RUN_CHECK = True


def val2addr(val):
    ''' convert MAC address to string '''
    addr = ''
    if val is None:
        return addr
    for ch in val:
        if isinstance(ch, int):
            addr += f'{ch:02x}'
        else:
            addr += f'{ord(ch):02x}'
    addr = addr.strip(' ').replace(' ', ':')[0:17]
    return addr


def wigle_print(api_key, netid):
    """ This gathers information from net """
    print(f'{"":>3}[-] Searching with Wigle.net for {netid}')
    headers = {'Accept': 'application/json',
               'Authorization': f'Basic {api_key}'}
    url = 'https://api.wigle.net/api/v2/network/search'
    payload = {'onlymine': False,
               'freenet': False,
               'paynet': False}

    payload['ssid'] = netid

    try:
        net_info = requests.get(url,
                                params=payload,
                                headers=headers,
                                timeout=5)
        net_info.raise_for_status()
        response = net_info.json()
    except requests.exceptions.HTTPError as err:
        print(f'{"":>3}[-] {err}')
        return
    try:
        map_lat = response['results'][0]['trilat']
        map_lon = response['results'][0]['trilong']
        print(f'[-] Lat: {map_lat}, Lon: {map_lon}')
    except KeyError:
        print(f'{"":>3}[-] {response["message"]}')
    finally:
        print(f'{"":>3}[-] {netid}')


def print_nets():
    ''' print network info'''
    net = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\\NetworkList\Signatures\Unmanaged"
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, net)  # pylint: disable=E0606
    print('[*] Networks You have Joined.')
    for i in range(100):
        try:
            guid = winreg.EnumKey(key, i)
            net_key = winreg.OpenKey(key, str(guid), 0, winreg.KEY_READ)
            (n, addr, t) = winreg.EnumValue(net_key, 5)
            (n, name, t) = winreg.EnumValue(net_key, 4)
            mac_addr = val2addr(addr)
            net_name = str(name)
            print(f'{"":>3}[+] {net_name.ljust(20)} {mac_addr.rjust(20)}')
            if WIGLE_CHECK:
                wigle_print(config.WIGLE_ENCODED, mac_addr)
            winreg.CloseKey(net_key)
        except (WindowsError, OSError):  # pylint: disable=E0602
            break
        except IndexError:
            break


def main():
    ''' main'''

    if RUN_CHECK:
        if IS_ADMIN:
            print_nets()
        else:
            print(f'[-] {RUN_NAME} must be run as admin')
    else:
        print(f'[-] {OS_NAME} not supported')


if __name__ == '__main__':
    print(f'[*] {RUN_NAME} starting')
    main()
    print(f'[*] {RUN_NAME} ending')
