'''
a lineage example
'''
import os
import sys
# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))

from jackmanimation.lineage.lineage import fed
from jackmanimation.lineage.lineage import population_birth
from jackmanimation.lineage.lineage import population_decline
from jackmanimation.lineage.lineage import production


def lineagedemo():
    ''' This is the main routine for the program '''
    pop = 1000
    fu = 10
    happyfactors = 0
    globalfactors = 0
    localfactors = 0
    ldfed = fed(pop, fu)
    ldbirth = population_birth(pop,
                               happyfactors,
                               globalfactors,
                               localfactors)
    lddeath = population_decline(pop,
                                 happyfactors,
                                 globalfactors,
                                 localfactors)
    newpop = pop + ldbirth - lddeath
    production_factor = production(pop - (lddeath + ldbirth))
    print("[+] Starting the LINEAGE sequence:")
    for year in range(1, 10):
        ldfed = fed(pop, fu)
        ldbirth = population_birth(pop,
                                   happyfactors,
                                   globalfactors,
                                   localfactors)
        lddeath = population_decline(pop,
                                     happyfactors,
                                     globalfactors,
                                     localfactors)
        newpop = pop + ldbirth - lddeath
        production_factor = production(pop - (lddeath + ldbirth),
                                       happyfactors,
                                       globalfactors,
                                       localfactors)
        fu = ldfed[2] + production_factor
        localfactors = localfactors + ldfed[0]
        print(f"[-] year                : {year}")
        print(" [#] base numbers       : "
              f"pop {pop} "
              f"food {fu} "
              f"happyfactors {happyfactors} "
              f"globalfactors {globalfactors} "
              f"localfactors {localfactors}")
        print(f' [#] fed                : {ldfed}')
        print(f' [#] population_birth   : {ldbirth}')
        print(f' [#] population_decline : {lddeath}')
        print(f' [#] new population     : {newpop}')
        print(f' [#] production_factor  : {production_factor}')
        print(f' [#] food units         : {fu}')
        pop = newpop
    print('[+] Finished')


def main():
    ''' This is the main routine for the program '''
    lineagedemo()


if __name__ == "__main__":
    main()
