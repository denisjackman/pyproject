''' hbot ticket analysis '''
import pandas as pd

INPUT_FILE = "E:/Work/data/hbot-2024-11.csv"


def main():
    '''main function '''
    hbdf = pd.read_csv(INPUT_FILE)
    total_helptickets = len(hbdf)
    total_columns = hbdf.columns
    for item in hbdf:
        print(f"{item}")


if __name__ == "__main__":
    main()
