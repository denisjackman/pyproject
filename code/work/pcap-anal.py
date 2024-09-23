''' pcap jira analysis'''
import csv

CSV_FILE = "E:/PPB/UKI JIRA 2024-09-23T13_45_17+0100.csv"


def main():
    ''' main function'''
    with open(CSV_FILE,
              'r',
              encoding='utf-8-sig') as csvfile:
        templist = csv.reader(csvfile, delimiter=',')
        extensionlist = list(templist)
    print(f"{len(extensionlist)}")


if __name__ == '__main__':
    main()
