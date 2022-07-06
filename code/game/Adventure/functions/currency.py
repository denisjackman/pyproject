#!/usr/bin/python

"""
    currency.py
    This is a set of functions which will allow you to convert the currencies to the relevant vaslue
"""


__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2016/03/05 00:00:00 $"
__copyright__ = "Copyright (c) 2016 Denis J Jackman"
__license__ = "Python"


def gold_to_silver(amount):
    '''
        gold to silver
    '''
    result = amount * 10
    return result


def gold_to_copper(amount):
    '''
        gold to copper
    '''
    result = amount * 100
    return result


def silver_to_copper(amount):
    '''
        silver to copper
    '''
    result = amount * 10
    return result


def silver_to_gold(amount):
    '''
        silver to gold
    '''
    result = amount / 10
    return result


def copper_to_gold(amount):
    '''
        copper to gold
    '''
    result = amount / 100
    return result


def copper_to_silver(amount):
    '''
        copper to silver
    '''
    result = amount / 10
    return result


if __name__ == '__main__':
    print('running a test on currency ')
    print('Test 1 : 1 gold = ' + str(gold_to_silver(1)) + ' Silver =  ' + str(gold_to_copper(1)) + ' Copper')
    print('Test 2 : 10 silver = ' + str(silver_to_copper(10)) + ' Copper =  ' + str(silver_to_gold(10)) + ' Gold')
    print('Test 3 : 100 copper = ' + str(copper_to_silver(100)) + ' Silver =  ' + str(copper_to_gold(100)) + ' Gold')
    print('Test 4 : .5 gold ' + str(gold_to_silver(.5)) + ' Silver =  ' + str(gold_to_copper(.5)) + ' Copper')
