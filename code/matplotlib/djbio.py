''' This is a matplotlib script to plot the data from the biostats.csv file'''
import csv
import matplotlib.pyplot as plt


def main():
    ''' main function'''
    x = []
    y = []
    count = False
    with open('Z:/Resources/Data/biostats.csv',
              'r',
              encoding='utf-8-sig') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            if count:
                x.append(row[0])
                y.append(int(row[2]))
            else:
                count = True
    plt.bar(x, y, color='g', width=0.72, label='Age')
    plt.xlabel('Names')
    plt.ylabel('Ages')
    plt.title('Age of Different People')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
