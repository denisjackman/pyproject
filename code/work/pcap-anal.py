''' pcap jira analysis'''
import pandas as pd

CSV_FILE = "E:/PPB/UKI JIRA 2024-09-23T13_45_17+0100.csv"


def main():
    ''' main function'''
    df = pd.read_csv(CSV_FILE)
    print(f"{df.head()}")
    print(f"[-] Info     : {df.info()}")
    print(f"[-] Describe : {df.describe()}")


if __name__ == '__main__':
    main()
