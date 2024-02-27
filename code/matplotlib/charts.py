'''
    example charts using matplotlib
'''
from matplotlib import pyplot as plt


def main():
    '''
        main function
    '''
    # create a simple line chart
    # plt.plot([1, 2, 3], [1, 2, 3])
    # plt.show()
    labels = ['Python', 'Java', 'HTML', 'C++', 'JavaScript']
    data = [95, 80, 65, 80, 95]
    explode = [0, 0, 0.1, 0, 0]
    plt.pie(data, labels=labels, explode=explode, shadow=True, startangle=90)
    plt.show()


if __name__ == "__main__":
    main()
