''' box and whsiper plot using python '''
import pandas as pd
import matplotlib.pyplot as plt


def main():
    ''' main function '''
    data = pd.DataFrame({"values": [7, 2, 15, 9, 12, 4, 11, 8, 13, 6]})

    data.plot.box()

    plt.xlabel('Data')
    plt.ylabel('Value')
    plt.title('Box and Whisker Plot with Pandas and Matplotlib')
    plt.show()


if __name__ == '__main__':
    main()
