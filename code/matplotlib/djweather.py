''' this is another matplotlib example'''
import csv
import matplotlib.pyplot as plt


def main():
    ''' main function'''
    x = []
    y = []
    with open('Z:/Resources/Data/Weatherdata.csv',
              'r',
              encoding='utf-8-sig') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            x.append(row[0])
            y.append(int(row[1]))
    plt.plot(x,
             y,
             color='g',
             linestyle='dashed',
             marker='o',
             label='Weather Data')
    plt.xlabel('Dates')
    plt.ylabel('Temperatures(oC)')
    plt.title('Weather Report', fontsize=20)
    plt.grid()
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
