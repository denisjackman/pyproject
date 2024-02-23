'''
    insult generator module for dnd
'''
__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.00 $"
__date__ = "$Date: 2022/11/25 00:00:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"
import platform
import json
from random import choice

if platform.system() == "Windows":
    FILEPATH = "Z:/Resources/development/"
else:
    FILEPATH = "/mnt/y/Resources/development/"


def shakespearean_insult_generator():
    '''
    Author : Denis Jackman
    Date : 31-July-2013
    Version : 1.0
    Function :
    This is a random insult generator based on Shakespearean lines.
    There are three (3) columns of Insult terms.
    Which are built then into an insult.
    This is pre-fixed with 'Thou'

    There are no inputs. The output is the insult as a string (result)
    '''
    filename = f"{FILEPATH}referencedata/ShakespeareInsult.json"
    with open(filename, "r", encoding='utf-8-sig') as file:
        data = json.load(file)
    column_one = choice(data["insult_column_one"])
    column_two = choice(data["insult_column_two"])
    column_three = choice(data["insult_column_three"])
    result = f"Thou {column_one} {column_two} {column_three}."
    # return it
    return result


def dwarven_insult_generator():
    '''
        dwarven insult generator
    '''
    with open(f"{FILEPATH}/referencedata/DwarvenInsult.json",
              "r",
              encoding='utf-8-sig') as file:
        data = json.load(file)
    dwarven_insult_one = choice(data["insult_column_one"]).capitalize()
    dwarven_insult_two = choice(data["insult_column_two"])
    dwarven_insult_three = choice(data["insult_column_three"])
    result = f"{dwarven_insult_one} "\
             f"{dwarven_insult_two} "\
             f"{dwarven_insult_three}."
    return result


def main():
    ''' main function '''
    print(f"Shakey  insult          : {shakespearean_insult_generator()}")
    print(f"Dwarven insult          : {dwarven_insult_generator()}")


if __name__ == '__main__':
    main()
