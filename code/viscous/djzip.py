''' zip file cracker '''
import zipfile
import optparse
import sys
from threading import Thread

def extractFile(zFile, password):
    ''' extract file from zip file '''''
    passcheck = False
    try:
        zFile.extractall(pwd=password)
        passcheck = True
    except:  # pylint: disable=bare-except
        pass
    if passcheck:
        print(f'[+] Found password {password}\n')


def main():
    ''' main function '''
    parser = optparse.OptionParser('usage%prog -f <zipfile> -d <dictionary>')
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
    (options, args) = parser.parse_args()
    if (options.zname is None) | (options.dname is None):
        print(f"{parser.usage}")
        sys.exit(0)
    else:
        zname = options.zname
        dname = options.dname
    with zipfile.ZipFile(zname) as zFile:
        with open(dname, 'r', encoding='utf-8-sig') as passFile:
            for line in passFile.readlines():
                password = line.strip('\n')
                t = Thread(target=extractFile, args=(zFile, password))
                t.start()

if __name__ == '__main__':
    main()
