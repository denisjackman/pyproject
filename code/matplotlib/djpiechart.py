''' pie chart example '''
import matplotlib.pyplot as plt


def main():
    ''' main function '''
    cars = ["BMW", "VW", "Audi", "Mercedes", "Opel"]
    data = [23, 17, 35, 29, 12]
    # fig = plt.figure(figsize=(10, 7))
    plt.pie(data, labels=cars)
    plt.show()


if __name__ == "__main__":
    main()
