''' utility to find zip files '''
import csv

DIRECTORYLISTFILE = "Y:\\Resources\\development\\directorylist.txt"
DIRECTORYSUMMARY = "Y:\\Resources\\development\\directorysummary.txt"

def main():
    ''' main function '''
    print("[+] Starting")

    with open(DIRECTORYSUMMARY, 'r', encoding='utf-8-sig') as csvfile:
        templist = csv.reader(csvfile, delimiter=',')
        extensionlist = list(templist)

    with open(DIRECTORYLISTFILE, 'r', encoding='utf-8-sig') as filelistfile:
        filelist = filelistfile.read().replace('\n', '')

    print(f"[-] files found {len(filelist):,}")
    print(f"[-] extensions found {len(extensionlist):,}")
    print(f"[-] extension's example {extensionlist[1]} {int(extensionlist[1][1]):,}")
    print(f"[-] file's example {filelist[1]}")
    print("[+] Finished")

if __name__ == '__main__':
    main()
