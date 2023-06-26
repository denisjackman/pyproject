''' This is a test element for the game.'''
import os
from code.DndProject.dnddice import dice
from code.DndProject.dnddice import number_generator

def main():
    ''' main function'''
    
    print('[+] Starting')
    print(f'[-] Progam name             : {os.path.basename(__file__)}')
    print(f'[-] Dice                    : {dice()}')
    print(f'[-] Number Generator        : {number_generator()}')
    print('[+] Finished')

if __name__ == '__main__':
    main()