''' This is a test element for the game.'''
import os
from code.DndProject.dnddice import dice
from code.DndProject.dnddice import number_generator
from code.DndProject.dndinsult import shakespearean_insult_generator
from code.DndProject.dndinsult import dwarven_insult_generator
#from code.DndProject.dndnames import dwarven_name
#from code.DndProject.dndnames import elfname_generator
#from code.DndProject.dndnames import angelic_name
#from code.DndProject.dndnames import barbarian_name
#from code.DndProject.dndnames import demon_name
#from code.DndProject.dndnames import hyborian_name_generator
#from code.DndProject.dndnames import lizardman_name_generator

def main():
    ''' main function'''
    
    print('[+] Starting')
    print(f'[-] Progam name             : {os.path.basename(__file__)}')
    print(f'[-] Dice                    : {dice()}')
    print(f'[-] Number Generator        : {number_generator()}')
    print(f'[-] Shakespearean Insult    : {shakespearean_insult_generator()}')
    print(f'[-] Dwarven Insult          : {dwarven_insult_generator()}')
    #print(f'[-] Dwarf Name              : {dwarven_name()}')
    #print(f'[-] Elf Name                : {elfname_generator()}')
    #print(f'[-] Angelic Name            : {angelic_name()}')
    #print(f'[-] Barbarian Name          : {barbarian_name()}')
    #print(f'[-] Demon Name              : {demon_name()}')
    #print(f'[-] Hyborian Name           : {hyborian_name_generator()}')
    #print(f'[-] Lizardman Name          : {lizardman_name_generator()}')
    print('[+] Finished')

if __name__ == '__main__':
    main()