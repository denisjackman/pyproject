''' This is a test element for the game.'''
import os
from djcode.DndProject.dnddice import dice
from djcode.DndProject.dnddice import number_generator
from djcode.DndProject.dndinsult import shakespearean_insult_generator
from djcode.DndProject.dndinsult import dwarven_insult_generator
from djcode.DndProject.dndnames import dwarven_name
from djcode.DndProject.dndnames import elfname_generator
from djcode.DndProject.dndnames import angelic_name
from djcode.DndProject.dndnames import barbarian_name
from djcode.DndProject.dndnames import demon_name
from djcode.DndProject.dndnames import hyborian_name_generator
from djcode.DndProject.dndnames import lizardman_name_generator
from djcode.DndProject.dndother import currency_converter
from djcode.DndProject.dndother import riddle_generator
from djcode.DndProject.dndother import fantasy_wine_name
from djcode.DndProject.dndother import hexmap_tile_type
from djcode.DndProject.dndother import book_title_generator
from djcode.DndProject.dndother import aoran
from djcode.DndProject.dndother import plural
from djcode.DndProject.dndother import coatofarms_generator
from djcode.DndProject.dndother import herb_name_generator
from djcode.DndProject.dndother import adventure_name_generator
from djcode.DndProject.dndother import lovecraft_creature_generator
from djcode.DndProject.dndother import orc_tribe_generator
from djcode.DndProject.dndother import organization_generator
from djcode.DndProject.dndother import ship_name_generator
from djcode.DndProject.dndnames import celtic_name_generator
from djcode.DndProject.dndnames import epyptian_name_generator
from djcode.DndProject.dndnames import greek_name_generator
from djcode.DndProject.dndnames import orc_name_generator
from djcode.DndProject.dndnames import oldenglish_name_generator
from djcode.DndProject.dndnames import sumerian_name_generator
from djcode.DndProject.dndplaces import town_name_generator
from djcode.DndProject.dndplaces import woodname_generator
from djcode.DndProject.dndplaces import streetname_generator
from djcode.DndProject.dndplaces import dwarven_settlement_name_generator
from djcode.DndProject.dndplaces import place_name_generator
from djcode.DndProject.dndplaces import inn_name_generator
from djcode.DndProject.dndplaces import site_name_generator
def main():
    ''' main function'''

    print('[+] Starting')
    print(f'[-] Progam name             : {os.path.basename(__file__)}')
    print(f'[-] Dice                    : {dice()}')
    print(f'[-] Number Generator        : {number_generator()}')
    print(f'[-] Shakespearean Insult    : {shakespearean_insult_generator()}')
    print(f'[-] Dwarven Insult          : {dwarven_insult_generator()}')
    print(f'[-] Dwarf Name              : {dwarven_name()}')
    print(f'[-] Elf Name                : {elfname_generator()}')
    print(f'[-] Angelic Name            : {angelic_name()}')
    print(f'[-] Barbarian Name          : {barbarian_name()}')
    print(f'[-] Demon Name              : {demon_name()}')
    print(f'[-] Hyborian Name           : {hyborian_name_generator()}')
    print(f'[-] Lizardman Name          : {lizardman_name_generator()}')
    print(f"[-] Riddle Question         : {riddle_generator()}")
    print(f"[-] Wine Name               : {fantasy_wine_name()}")
    print(f"[-] Angelic Name            : {angelic_name()}")
    print(f"[-] Barbarian Name          : {barbarian_name()}")
    print(f"[-] Dwarven Name            : {dwarven_name()}")
    print(f"[-] Dwarven Name (m)        : {dwarven_name(gender='Male')}")
    print(f"[-] Dwarven Name (f)        : {dwarven_name(gender='female')}")
    print(f"[-] Demon Name              : {demon_name()}")
    print(f"[-] Town Name               : {town_name_generator()}")
    print(f"[-] Wood Name               : {woodname_generator()}")
    print(f"[-] Street Name             : {streetname_generator()}")
    print(f"[-] Dwarven Settlement Name : {dwarven_settlement_name_generator()}")
    print(f"[-] Place Name              : {place_name_generator()}")
    print(f"[-] Book Title              : {book_title_generator()}")
    print(f"[-] Book Title              : {book_title_generator(catalogue=True)}")
    print(f"[-] Hexmap tile             : {hexmap_tile_type()}")
    print(f"[-] A or An                 : {aoran('apple')}")
    print(f"[-] Plural                  : {plural('apple')}")
    print(f"[-] Shakey  insult          : {shakespearean_insult_generator()}")
    print(f"[-] Dwarven insult          : {dwarven_insult_generator()}")
    print(f'[-] Coat of Arms            : {coatofarms_generator()}')
    print(f'[-] Elf Name                : {elfname_generator()}')
    print(f'[-] Herb Name               : {herb_name_generator()}')
    print(f'[-] Hyborian Name           : {hyborian_name_generator()}')
    print(f'[-] Inn Name                : {inn_name_generator()}')
    print(f'[-] Adventure Name          : {adventure_name_generator()}')
    print(f'[-] Lizardman Name          : {lizardman_name_generator()}')
    print(f'[-] Lovecraftian Creature   : {lovecraft_creature_generator()}')
    print(f'[-] Celtic Name             : {celtic_name_generator()}')
    print(f"[-] Celtic Name (m)         : {celtic_name_generator(gender='male')}")
    print(f"[-] Celtic Name (f)         : {celtic_name_generator(gender='female')}")
    print(f"[-] Egyptian Name           : {epyptian_name_generator()}")
    print(f"[-] Greek Name              : {greek_name_generator()}")
    print(f"[-] Old English Name        : {oldenglish_name_generator()}")
    print(f"[-] Sumerian Name           : {sumerian_name_generator()}")
    print(f"[-] Orc Name                : {orc_name_generator()}")
    print(f"[-] Orc Tribe Name          : {orc_tribe_generator()}")
    print(f"[-] Organization Name       : {organization_generator()}")
    print(f"[-] Ship Name               : {ship_name_generator()}")
    print(f"[-] Site Name               : {site_name_generator()}")
    print(f"[-] Currency                : {currency_converter(100)}")
    print('[+] Finished')

if __name__ == '__main__':
    main()
