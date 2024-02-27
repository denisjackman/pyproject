'''this is to plot seizuire data'''
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = 'G:/Aidan Jackman/seizure.xlsx'


def main():
    '''main function'''
    data = pd.read_excel(DATA_FILE, sheet_name='Episode')
    plt.bar(data['Year'], data['Seizures'])
    plt.show()
    book = pd.read_excel(DATA_FILE, sheet_name='Books')
    plt.bar(book['Year'], book['Books'])
    plt.suptitle('Books by Year', fontsize=20)
    plt.xlabel('Year', fontsize=18)
    plt.ylabel('Books', fontsize=18)
    plt.show()


if __name__ == '__main__':
    main()
