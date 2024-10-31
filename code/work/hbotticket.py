''' hbot ticket analysis '''
import pandas as pd
import matplotlib.pyplot as plt

INPUT_FILE = "E:/Work/data/hbotdata.csv"


def main():
    '''main function '''
    hbdf = pd.read_csv(INPUT_FILE)
    status_counts = hbdf.groupby('Status').size().reset_index(name='Total by Status')
    team_counts = hbdf.groupby('Team').size().reset_index(name='Total Tickets')
    label_counts = hbdf.groupby('Labels').size().reset_index(name='Total Tickets')
    print(f"{status_counts}")
    print(f"{team_counts}")
    print(f'{label_counts}')
    # nu_status_counts = hbdf['Status'].value_counts()
    # plt.figure(figsize=(8, 8))
    # plt.pie(nu_status_counts, labels=nu_status_counts.index, autopct='%1.1f%%', startangle=140)
    # plt.title('Distribution of Tickets by Status')
    # plt.show()

    # nu_team_counts = hbdf['Team'].value_counts()
    # plt.figure(figsize=(8, 8))
    # plt.pie(nu_team_counts, labels=nu_team_counts.index, autopct='%1.1f%%', startangle=140)
    # plt.title('Distribution of Tickets by Team')
    # plt.show()


if __name__ == "__main__":
    main()
