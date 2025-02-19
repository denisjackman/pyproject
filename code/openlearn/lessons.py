''' openlearn.lessons.py'''


def main():
    ''' main function'''
    expenses = 54
    people = 6
    if people > 6:
        percentage = 0.10
    else:
        percentage = 0
    tip = expenses * percentage
    bill = expenses + tip
    print(f"Total bill: {bill}")


if __name__ == '__main__':
    main()
