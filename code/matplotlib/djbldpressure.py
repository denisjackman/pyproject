'''This is another matplotlib example'''
import csv
import matplotlib.pyplot as plt


def main():
    ''' main function'''
    Names = []
    Values = []
    with open('Z:/Resources/Data/bldprs_measure.csv',
              'r',
              encoding='utf-8-sig') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            Names.append(row[0])
            Values.append(int(row[1]))

    plt.scatter(Names, Values, color='g', s=100)
    plt.xticks(rotation=25)

    plt.xlabel('Names')
    plt.ylabel('Values')
    plt.title('Patients Blood Pressure Report', fontsize=20)
    plt.show()


if __name__ == '__main__':
    main()
