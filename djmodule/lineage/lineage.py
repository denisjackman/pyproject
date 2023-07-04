#!/usr/bin/env python
"""
lineage.py

This is a module for all the game items for the lineage game
"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2022/06/14 00:00:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"
import random


def gold_to_silver(amount):
    '''
        convert gold to silver
    '''
    result = amount * 10
    return result


def gold_to_copper(amount):
    '''
        convert gold to copper
    '''
    result = amount * 100
    return result


def silver_to_copper(amount):
    '''
        convert silver to copper
    '''
    result = amount * 10
    return result


def silver_to_gold(amount):
    '''
        convert silver to gold
    '''
    result = amount / 10
    return result


def copper_to_gold(amount):
    '''
        convert copper to gold
    '''
    result = amount / 100
    return result


def copper_to_silver(amount):
    '''
        convert copper to silver
    '''
    result = amount / 10
    return result


def dice(sides=6, rolls=1):
    '''
        Rolls a dice which has 'sides' sides (default is six (6))
        for 'rolls' number of times (default is one (1))
    '''
    result = 0
    loop = 0
    while loop < rolls:
        result = result + random.randrange(1, sides+1)
        loop = loop + 1
    return result


def number_generator(number=100):
    '''
        Generates a random number between 1 and number
    '''
    return random.randint(1, number)


def population_birth(population,
                     happieness=0,
                     global_factors=0,
                     local_factors=0):
    '''
        this calculates the population growth
        for a nation, city or other entity
    '''
    growth = 0
    pop = population/200
    factors = 25 + happieness
    factors = factors + number_generator(5)
    factors = factors + global_factors + local_factors
    growth = pop * factors
    return int(growth)


def population_decline(population,
                       happieness=0,
                       global_factors=0,
                       local_factors=0):
    '''
        This calculates the decline rate
        for a nation, city or other entity
    '''
    decline = 0
    pop = population/400
    factors = 25 + happieness
    factors = factors + number_generator(5)
    factors = factors + global_factors + local_factors
    decline = pop * factors
    return int(decline)


def fed(population, food_units):
    '''
        This works out the fed factor of a population
        divide the population by 1000 rounding out
        if this is more than the available food units
        Then the population is fed.

        send back the fed factor and the new food units available
    '''
    population_check = population / 1000
    factor = food_units / population_check
    fed_description = ""
    fed_factor = 0
    if factor == 0:
        fed_description = "wrong answer"
        fed_factor = 0
    elif 0 < factor < .33:
        fed_description = "Starving"
        fed_factor = -10
    elif .33 <= factor < .50:
        fed_description = "Malnourished"
        fed_factor = -5
    elif .50 <= factor < 1:
        fed_description = "Underfed"
        fed_factor = -4
    elif 1 <= factor < 2:
        fed_description = "Fed"
        fed_factor = 3
    elif 2 <= factor < 3:
        fed_description = "Average"
        fed_factor = 5
    elif 3 <= factor < 4:
        fed_description = "Medium"
        fed_factor = 7
    elif 4 <= factor < 5:
        fed_description = "Well"
        fed_factor = 9
    elif factor >= 5:
        fed_description = "Overfed"
        fed_factor = 10
    food_units = int(max(food_units - population_check, 0))
    return(fed_factor, fed_description, food_units)

if __name__ == '__main__':
