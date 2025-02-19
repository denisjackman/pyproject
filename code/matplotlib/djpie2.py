'''Matplotlib pie chart example with a title and a legend.'''
import csv
import matplotlib.pyplot as plt


def main():
    '''Main program.'''
    Subjects = []
    Scores = []
    # Read the data from the CSV file.
    with open('Z:/Resources/Data/SubjectMarks.csv',
              'r',
              encoding='utf-8-sig') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            Subjects.append(row[0])
            Scores.append(int(row[1]))

    # Create the pie chart.
    plt.pie(Scores, labels=Subjects, autopct='%.2f%%')
    plt.title('Marks of a Student', fontsize=20)

    # Show the chart.
    plt.show()


if __name__ == '__main__':
    main()
