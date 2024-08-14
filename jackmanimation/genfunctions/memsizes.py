'''
    approximate size
'''
import math

SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}


def future_value(present_value, annual_rate, periods_per_year, years):
    '''
        future value
    '''
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    result = present_value * (1 + rate_per_period) ** periods
    return result


def is_area_of_polygon(number_of_sides, sides_length):
    '''
        area of a polygon
    '''
    pi = 3.14159265359
    area = ((number_of_sides * (sides_length ** 2)) / math.tan(pi / number_of_sides)) / 4
    return area


def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    '''Convert a file size to human-readable form.
    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
    Returns: string
    '''
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000

    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return f'{size:.1f} {suffix}'

    raise ValueError('number too large')
