''' default pages for the chapter 2'''
import ftplib

def returnDefault(rdftp):
    ''' return the default pages for the chapter 2'''
    try:
        dirList = rdftp.nlst()
    except: # pylint: disable=bare-except
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
    host = '192.168.1.236'
    userName = 'guest'
    passWord = 'guest'
    ftp = ftplib.FTP(host)
    ftp.login(userName, passWord)
    returnDefault(ftp)

if __name__ == '__main__':
    main()
