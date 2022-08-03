'''
    example
'''
import math
def future_value(present_value, annual_rate, periods_per_year, years):
    '''
        future value
    '''
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    # Put your code here.
    result = present_value * ( 1+ rate_per_period) ** periods
    return result

def is_area_of_polygon(number_of_sides, sides_length):
    '''
        area of a polygon
    '''
    pi = 3.14159265359
    area = ((number_of_sides * (sides_length **2))/math.tan(pi/number_of_sides))/4
    return area

print(int(round(math.log(1000,2))))
print(int(round(math.log(400,2))))
