'''
a util to find files with a pattern in the name and delete them
'''
import os
import sys
# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.genfunctions.various import newRating
from jackmanimation.genfunctions.various import ageCalculator
from jackmanimation.genfunctions.various import passwordgenerator
from jackmanimation.genfunctions.various import isLeapYear

from jackmanimation.gameitems.constants import SMILEY1
from jackmanimation.gameitems.colours import BLACK
from jackmanimation.gameitems.colours import COLOURS_RGB_LIST

from jackmanimation.lineage.lineage import fed
from jackmanimation.lineage.lineage import population_birth
from jackmanimation.lineage.lineage import population_decline

from jackmanimation.genfunctions.searchutils import linear_search
from jackmanimation.genfunctions.searchutils import binary_search


def constantdemo():
    ''' This is the main routine for the program '''
    print("[+] Starting the CONSTANT sequence:")
    print(f'[-] SMILEY1          : {SMILEY1}')
    print(f'[-] BLACK            : {BLACK}')
    print(f'[-] COLOURS_RGB_LIST : {COLOURS_RGB_LIST["BLACK"]}')
    print('[+] Finished')


def variousdemo():
    ''' This is the main routine for the program '''
    print("[+] Starting the VARIOUS sequence:")
    print('[-] score rating - old 1200 playing 1200 and winning : '
          f'{newRating(1200, 1200, "w")}')
    print('[-] score rating - old 1200 playing 1200 and losing  : '
          f'{newRating(1200, 1200, "Loss")}')
    print('[-] score rating - old 1216 playing 1184 and winning : '
          f'{newRating(1216, 1184, "Win")}')
    print('[-] age based on 2/3/2023                            : '
          f'{ageCalculator(1965, 3, 2)}')
    print('[-] password genertator (18 characters long)         : '
          f'{passwordgenerator(18)}')
    print('[-] is 2020 a leap year                              : '
          f'{isLeapYear(2020)}')
    print('[-] is 2021 a leap year                              : '
          f'{isLeapYear(2021)}')
    print('[+] Finished')


def lineagedemo():
    ''' This is the main routine for the program '''
    pop = 1000
    fu = 10
    happyfactors = 0
    globalfactors = 0
    localfactors = 0
    print("[+] Starting the LINEAGE sequence:")
    print(f"[-] base numbers       : pop {pop} food {fu} happyfactors "
          f"{happyfactors} globalfactors {globalfactors} localfactors "
          f"{localfactors}")
    print(f'[-] fed                : {fed(pop, fu)}')
    print(f'[-] population_birth   : {population_birth(pop, happyfactors, globalfactors, localfactors)}')
    print(f'[-] population_decline : {population_decline(pop, happyfactors, globalfactors, localfactors)}')
    print('[+] Finished')


def searchdemo():
    ''' This is the main routine for the program'''
    print("[+] Search Algorithm start")
    searchlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f'[-] searchlist is {searchlist}')
    print(f'[-] Linear looking for 5 in searchlist {linear_search(searchlist, 5)}')
    print(f'[-] Linear looking for 20 in searchlist {linear_search(searchlist, 20)}')
    print(f'[-] Binary looking for 5 in searchlist {binary_search(searchlist, 0, len(searchlist)-1, 5)}')
    print(f'[-] Binary looking for 20 in searchlist {binary_search(searchlist, 0, len(searchlist)-1, 20)}')
    print("[+] Search Algorithm finish")


def main():
    ''' This is the main routine for the program '''
    print("[=] Start")
    # variousdemo()
    # constantdemo()
    lineagedemo()
    # searchdemo()
    print('[=] Finished')


if __name__ == '__main__':
    main()
