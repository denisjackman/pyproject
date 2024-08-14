'''
    various function
'''
import datetime
import random
import string
import math

daysOfMonths = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isArmstrong(number):
    ''' this is a function to check if a number
        is an armstrong number or not'''
    result = False
    total = 0
    temp = number

    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp //= 10
    if number == total:
        result = True
    return result


def passwordgenerator(pwlen):
    '''
        password generator
    '''
    letters = string.ascii_letters
    uletters = string.ascii_uppercase
    numbers = '0123456789'
    special = '-+*%&$!_'
    passcode = letters + uletters + numbers + special
    password = ''.join(random.sample(passcode, pwlen))
    return password


def ageCalculator(inputyear, inputmonth, inputday):
    '''
        function agecalculator
    '''
    today = datetime.datetime.now().date()
    dateofbirth = datetime.date(inputyear, inputmonth, inputday)
    age = int((today - dateofbirth).days / 365)
    return age


def isLeapYear(year):
    '''
        return true if it is a leap year
    '''
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def daysInMonth(year, month):
    '''
        the number of days in a month
    '''
    result = 0
    print(f'[0]year is {year} and month is {month} {result}')
    if month in (1, 3, 5, 7, 8, 10, 12):
        result = 31
        print(f'[1]year is {year} and month is {month} {result}')
    else:
        if month == 2:
            if isLeapYear(year):
                result = 29
            else:
                result = 28
            print(f'[2]year is {year} and month is {month} {result}')
        else:
            result = 30
            print(f'[3]year is {year} and month is {month} {result}')
    return result


def isValidDateRange(date1, date2):
    '''
        is a given date range valid
    '''
    year1 = date1[0]
    month1 = date1[1]
    day1 = date1[2]
    year2 = date2[0]
    month2 = date2[1]
    day2 = date2[2]

    if year2 > year1:
        return True
    if year2 == year1:
        if month2 > month1:
            return True
        if month2 == month1:
            if day2 >= day1:
                return True
    return False


def isAfterGregorian(year, month, day):
    '''
        is our date after the gregorian calender
    '''
    if year > 1582:
        return True
    if year == 1582:
        if month > 10:
            return True
        if month == 10:
            if day >= 15:
                return True
    return False


def nextDay(year, month, day):
    """
        Simple version:
            assume every month has 30 days
    """
    if day < daysInMonth(year, month):
        return year, month, day + 1
    if month == 12:
        return year + 1, 1, 1
    return year, month + 1, 1


def dateIsAfter(diadate1, diadate2):
    """
        Returns True if year1-month1-day1 is after year2-month2-day2.
        Otherwise, returns False.
    """
    year1 = diadate1[0]
    month1 = diadate1[1]
    day1 = diadate1[2]
    year2 = diadate2[0]
    month2 = diadate2[1]
    day2 = diadate2[2]
    if year1 > year2:
        return True
    if year1 == year2:
        if month1 > month2:
            return True
        if month1 == month2:
            return day1 > day2
    return False


def daysBetweenDates(dbddate1, dbddate2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    year1 = dbddate1[0]
    month1 = dbddate1[1]
    day1 = dbddate1[2]
    year2 = dbddate2[0]
    month2 = dbddate2[1]
    day2 = dbddate2[2]

    assert isValidDateRange([year1, month1, day1], [year2, month2, day2])
    assert isAfterGregorian(year1, month1, day1)
    assert isAfterGregorian(year2, month2, day2)

    days = 0
    while dateIsAfter(dbddate2, dbddate1):
        days += 1
        (year1, month1, day1) = nextDay(year1, month1, day1)
    return days


def newRating(player_rating, opponent_rating, gametype):
    '''
        ELO rating system
        win lose score rating system
        gametype can be w or l (or a combination of any
        words that start with w or l)
    '''
    gameresult = gametype[0].lower()
    chance_of_winning = int((1 / (1 + (math.pow(10, ((opponent_rating - player_rating) / 400))))) * 100)
    chance_of_losing = 100 - chance_of_winning
    k_factor = 32
    win_points = int(round(k_factor * (chance_of_losing/100.0)))
    lose_points = int(round(k_factor * (chance_of_winning/100.0)))
    if gameresult == "w":
        result = player_rating + win_points
    else:
        result = player_rating - lose_points
    return result
