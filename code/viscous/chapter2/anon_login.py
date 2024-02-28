''' anon login script'''
import ftplib


def anon_login(hostname):
    ''' anon login '''
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'me@your.com')
        print('\n[*] ' + str(hostname) + ' FTP Anonymous Logon Succeeded.')
        ftp.quit()
        return True
    except Exception as e:
        print('\n[-] ' + str(hostname) + ' FTP Anonymous Logon Failed.')
        print(e)
        return False


def main():
    ''' main '''
    host = '192.168.95.179'
    anon_login(host)


if __name__ == '__main__':
    main()
