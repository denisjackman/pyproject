''' box and whsiper plot using python '''
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    ''' main function '''
    data = [7, 2, 15, 9, 12, 4, 11, 8, 13, 6]
    sns.boxplot(data=data)
    # Customize with hue (category) plot
    data = {"category": ["A", "B", "A", "A", "B", "A", "A", "B", "B", "A"],
            "values": data}
    sns.boxplot(x="category", y="values", data=data)

    plt.show()


if __name__ == '__main__':
    main()
