''' utility to find zip files '''
import csv

DIRECTORYLISTFILE = "Z:/Resources/development/directorylist.txt"
DIRECTORYSUMMARY = "Z:/Resources/development/directorysummary.txt"


def main():
    ''' main function '''
    print("[+] Starting")

    with open(DIRECTORYSUMMARY,
              'r',
              encoding='utf-8-sig') as csvfile:
        templist = csv.reader(csvfile, delimiter=',')
        extensionlist = list(templist)

    with open(DIRECTORYLISTFILE,
              'r',
              encoding='utf-8-sig') as filelistfile:
        filelist = filelistfile.readlines()
    testvalue = 0
    testkey = ""
    for item in extensionlist:
        itemkey = item[0]
        itemvalue = int(item[1])
        if testvalue < itemvalue:
            testkey = itemkey
            testvalue = itemvalue
    print(f"[-] Largest item is '{testkey}' and it is {testvalue:,}")
    print(f"[-] files found {len(filelist):,}")
    print(f"[-] extensions found {len(extensionlist):,}")
    print("[-] extension's example "
          f"{extensionlist[1]} {int(extensionlist[1][1]):,}")
    temp = filelist[1].replace('\n', '')
    print(f"[-] file's example {temp}")
    print("[+] Finished")


if __name__ == '__main__':
    main()
