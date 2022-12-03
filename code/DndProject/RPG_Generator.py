'''
    Name : RPG_Generator.py

    Function :
    This is a RPG Games master tool.
    It is a swiss army knife of random generators, and other tools.

    It has in it currently:
        a Dice function
        a number generator
        a riddle generator
        a Shakepspearean Insult generator
        a Dwarven insult generator
        various naming generators
        a currency converter

    Working on:
        Oracle Generator

    References:
        https://www.dndspeak.com/
        https://www.reddit.com/r/d100/new/
        https://stephthedev.com/dnd-exchange-rate
        https://stephthedev.com/dnd-travel-calculator

    Notes:
        This is a work in progress.
'''

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.00 $"
__date__ = "$Date: 2022/11/01 00:00:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"


from dndinsult import shakespearean_insult_generator
from dndinsult import dwarven_insult_generator
from dndother import currency_converter
from dndother import riddle_generator
from dndother import fantasy_wine_name
from dndother import hexmap_tile_type
from dndother import book_title_generator
from dndother import aoran
from dndother import plural
from dndother import coatofarms_generator
from dndother import herb_name_generator
from dndother import adventure_name_generator
from dndother import lovecraft_creature_generator
from dndother import orc_tribe_generator
from dndother import organization_generator
from dndother import ship_name_generator
from dndnames import angelic_name
from dndnames import barbarian_name
from dndnames import dwarven_name
from dndnames import demon_name
from dndnames import elfname_generator
from dndnames import hyborian_name_generator
from dndnames import lizardman_name_generator
from dndnames import celtic_name_generator
from dndnames import epyptian_name_generator
from dndnames import greek_name_generator
from dndnames import orc_name_generator
from dndnames import oldenglish_name_generator
from dndnames import sumerian_name_generator
from dndplaces import town_name_generator
from dndplaces import woodname_generator
from dndplaces import streetname_generator
from dndplaces import dwarven_settlement_name_generator
from dndplaces import place_name_generator
from dndplaces import inn_name_generator
from dndplaces import site_name_generator

def main(test=True):
    '''
        Main function
    '''
    if test:
        print(f"Riddle Question         : {riddle_generator()}")
        print(f"Wine Name               : {fantasy_wine_name()}")
        print(f"Angelic Name            : {angelic_name()}")
        print(f"Barbarian Name          : {barbarian_name()}")
        print(f"Dwarven Name            : {dwarven_name()}")
        print(f"Dwarven Name            : {dwarven_name(gender='Male')}")
        print(f"Dwarven Name            : {dwarven_name(gender='female')}")
        print(f"Demon Name              : {demon_name()}")
        print(f"Town Name               : {town_name_generator()}")
        print(f"Wood Name               : {woodname_generator()}")
        print(f"Street Name             : {streetname_generator()}")
        print(f"Dwarven Settlement Name : {dwarven_settlement_name_generator()}")
        print(f"Place Name              : {place_name_generator()}")
        print(f"Book Title              : {book_title_generator()}")
        print(f"Book Title              : {book_title_generator(catalogue=True)}")
        print(f"Hexmap tile             : {hexmap_tile_type()}")
        print(f"A or An                 : {aoran('apple')}")
        print(f"Plural                  : {plural('apple')}")
        print(f"Shakey  insult          : {shakespearean_insult_generator()}")
        print(f"Dwarven insult          : {dwarven_insult_generator()}")
        print(f'Coat of Arms            : {coatofarms_generator()}')
        print(f'Elf Name                : {elfname_generator()}')
        print(f'Herb Name               : {herb_name_generator()}')
        print(f'Hyborian Name           : {hyborian_name_generator()}')
        print(f'Inn Name                : {inn_name_generator()}')
        print(f'Adventure Name          : {adventure_name_generator()}')
        print(f'Lizardman Name          : {lizardman_name_generator()}')
        print(f'Lovecraftian Creature   : {lovecraft_creature_generator()}')
        print(f'Celtic Name             : {celtic_name_generator()}')
        print(f"Celtic Name             : {celtic_name_generator(gender='male')}")
        print(f"Celtic Name             : {celtic_name_generator(gender='female')}")
        print(f"Egyptian Name           : {epyptian_name_generator()}")
        print(f"Greek Name              : {greek_name_generator()}")
        print(f"Old English Name        : {oldenglish_name_generator()}")
        print(f"Sumerian Name           : {sumerian_name_generator()}")
        print(f"Orc Name                : {orc_name_generator()}")
        print(f"Orc Tribe Name          : {orc_tribe_generator()}")
        print(f"Organization Name       : {organization_generator()}")
        print(f"Ship Name               : {ship_name_generator()}")
        print(f"Site Name               : {site_name_generator()}")
        print(f"Currency                : {currency_converter(100)}")
    else:
        print("No tests")

if __name__ == "__main__":
    main()
