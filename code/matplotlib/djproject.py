'''
    matplotlib project and play

    The plan is to to create a simple script which will open file and chart it

    steps
    1. open the target file
    2. read the file into a list
    3. sort the list and consolidate it
    4. plot the list
'''
import csv
import matplotlib.pyplot as plt

DATA_FILE = 'biostats.csv'


def openfile():
    ''' open the file and read it into a list'''
    print("[+] Opening the file")
    result = []
    with open(DATA_FILE,
              'r',
              encoding='utf-8-sig') as csvfile:
        result = list(csv.DictReader(csvfile, delimiter=','))
    print("[+] Closing the file")
    return result


def listsorted(listtosort):
    ''' sort the list and consolidate it'''
    print("[+] Sorting the list")
    result = listtosort
    print("[+] Consolidating the list")
    return result


def chart(listtochart):
    ''' plot the list'''
    print("[+] Starting to plot the list")
    x = []
    y = []
    for row in listtochart:
        x.append(row["\ufeffName"])
        y.append(int(row["Age"]))

    plt.bar(x, y, color='g', width=0.72, label='Age')
    plt.xlabel('Names')
    plt.ylabel('Ages')
    plt.title('Age of Different People')
    plt.legend()
    plt.show()
    print("[+] Finished plotting the list")


def main():
    ''' main function'''
    print("[+] Starting the program]")
    datalist = openfile()
    sortedlist = listsorted(datalist)
    chart(sortedlist)
    print("[+] Ending the program")


if __name__ == '__main__':
    main()
