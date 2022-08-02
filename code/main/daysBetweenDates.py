# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Compensate for leap days.
# Assume that the birthday and current date are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is 2 Jan 2012
# you are 1 day old.
#
# Hint
# A whole year is 365 days, 366 if a leap year.
def isLeapYear(year):
    '''
        return true if it is a leap year
    '''
    if year % 400 == 0:
        return True
    if year % 100 ==0:
        return False
    if year % 4 == 0:
        return True
    return False

daysOfMonths = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def daysInMonth(year,month):
    '''
        the number of days in a month
    '''
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month == 2:
        if isLeapYear(year):
            return 29
        return 28
    return 30

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

    if year2> year1:
        return True
    if year2 == year1:
        if month2 > month1:
            return True
        if month2 == month1:
            if day2 >= day1:
                return True
    return False

def isAfterGregorian(year,month,day):
    '''
        is our date after the gregorian calender
    '''
    if year > 1582:
        return True
    if year ==1582:
        if month > 10:
            return True
        if month==10:
            if day >= 15:
                return True
    return False

def nextDay(year, month, day):
    """
        Simple version:
            assume every month has 30 days
    """
    if day < daysInMonth(year,month):
        return year, month, day + 1
    if month == 12:
        return year + 1, 1, 1
    return year, month + 1, 1

def dateIsAfter(date1, date2):
    """
        Returns True if year1-month1-day1 is after year2-month2-day2.
        Otherwise, returns False.
    """
    year1 = date1[0]
    month1 = date1[1]
    day1 = date1[2]
    year2 = date2[0]
    month2 = date2[1]
    day2 = date2[2]
    if year1 > year2:
        return True
    if year1 == year2:
        if month1 > month2:
            return True
        if month1 == month2:
            return day1 > day2
    return False

def daysBetweenDates(date1, date2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    year1 = date1[0]
    month1 = date1[1]
    day1 = date1[2]
    year2 = date2[0]
    month2 = date2[1]
    day2 = date2[2]

    assert isValidDateRange([year1,month1,day1], [year2, month2, day2])
    assert isAfterGregorian(year1,month1,day1)
    assert isAfterGregorian(year2,month2,day2)

    days = 0
    while dateIsAfter(date2, date1):
        days += 1
        (year1, month1, day1) = nextDay(year1, month1, day1)
    return days

def test():
    '''
        test cases
    '''
    test_cases = [(((2012,1,1),(2012,2,28)), 58),
                  (((2012,1,1),(2012,3,1)), 60),
                  (((2011,6,30),(2012,6,30)), 366),
                  (((2011,1,1),(2012,8,8)), 585 ),
                  (((1900,1,1),(1999,12,31)), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")

test()
