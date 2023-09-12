''' win reg exploration '''
from winreg import *

def val2addr(val):
    ''' convert MAC address to string '''
    addr = ''
    for ch in val:
        addr += f'%02x {ord(ch)}'
    addr = addr.strip(' ').replace(' ', ':')[0:17]
    return addr

def printNets():
    ''' print network info '''
    net = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"+\
            r"\NetworkList\Signatures\Unmanaged"
    key = OpenKey(HKEY_LOCAL_MACHINE, net)
    print('[*] Networks You have Joined.')
    for i in range(100):
        try:
            guid = EnumKey(key, i)
            netKey = OpenKey(key, str(guid))
            (n, addr, t) = EnumValue(netKey, 5)
            (n, name, t) = EnumValue(netKey, 4)
            macAddr = val2addr(addr)
            netName = str(name)
            print('[+] ' + netName + ' ' + macAddr)
            CloseKey(netKey)
        except: # pylint: disable=bare-except
            break

def main():
    ''' main'''
    printNets()

if __name__ == '__main__':
    main()
