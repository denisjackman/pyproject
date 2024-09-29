''' medisafe analysis'''
import pandas as pd

MEDISAFE_CSV_FILE = "Y:/Data/health/DJ-Medisafe.csv"


def main():
    ''' main function'''
    medi_df = pd.read_csv(MEDISAFE_CSV_FILE)
    print(f"{medi_df.head()}")
    print(f"[-] Info     : {medi_df.info()}")
    print(f"[-] Describe : {medi_df.describe()}")


if __name__ == '__main__':
    main()
