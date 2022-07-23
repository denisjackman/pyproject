'''
    agecalculator function
'''
import datetime

SMILEY1 = '\U0001F917'
SMILEY2 = '\U0001F62A'
SMILEY3 = '\U0001F637'
SMILEY4 = '\U0001F618'
SMILEY5 = '\U0001F600'

def ageCalculator(inputyear, inputmonth, inputday):
    '''
        function agecalculator
    '''
    today = datetime.datetime.now().date()
    dateofbirth = datetime.date(inputyear, inputmonth, inputday)
    age = int((today - dateofbirth).days / 365)
    return age


def main():
    '''
        main function
    '''
    print(ageCalculator(1965, 3, 2))
    print(SMILEY1)
    print(SMILEY2)
    print(SMILEY3)
    print(SMILEY4)
    print(SMILEY5)


if __name__ == '__main__':
    main()
