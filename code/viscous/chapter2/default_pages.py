''' default pages for the chapter 2'''
import ftplib


def returnDefault(rdftp):
    ''' return the default pages for the chapter 2'''
    try:
        rd_dirList = rdftp.nlst()
    except:  # pylint: disable=bare-except
        rd_dirList = []
        print('[-] Oh Dear ! Could not list directory contents.')
        print('[-] Whoops ! Skipping To Next Target.')
        return None

    rd_retList = []
    for rd_fileName in rd_dirList:
        rd_fn = rd_fileName.lower()
        if '.php' in rd_fn or '.htm' in rd_fn or '.asp' in rd_fn or '.html' in rd_fn:
            print('[+] Found default page: ' + rd_fileName)
            rd_retList.append(rd_fileName)
    return rd_retList


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
