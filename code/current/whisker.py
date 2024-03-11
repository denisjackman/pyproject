''' box and whsiper plot using python '''
import matplotlib.pyplot as plt


def main():
    ''' main function '''
    data = [7, 2, 15, 9, 12, 4, 11, 8, 13, 6]
    plt.boxplot(data)
    plt.xlabel('Data')
    plt.ylabel('Value')
    plt.title('Box and Whisker Plot')
    plt.show()


if __name__ == '__main__':
    main()
