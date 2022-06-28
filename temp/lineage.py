#!/usr/bin/env python
"""
lineage.py

This is a module for all the game items for the lineage game
"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.0 $"
__date__ = "$Date: 2022/06/14 00:00:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"

import os
import sys
#pylint: disable=wrong-import-position
MODULE_PATH = "../jackmanimation/"
sys.path.append(os.path.abspath(MODULE_PATH))
from jackmanimation import number_generator
#pylint: enable=wrong-import-position


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


def main():
    """ This is the main routine for the program """
    print("Starting the sequence:")
    loop = 0
    nation = 1000
    print("Year : Pop  : Births : Deaths ")
    while loop < 6:
        new_growth = population_birth(nation)
        new_decline = population_decline(nation)
        print(f"   {loop} : {nation} : {new_growth}    : {new_decline} ")
        nation = nation + new_growth - new_decline
        loop = loop + 1
    print("Fed Function : ")
    check = fed(10, 1)
    print(check)
    print("finishing up and closing down:")


if __name__ == '__main__':
    main()
