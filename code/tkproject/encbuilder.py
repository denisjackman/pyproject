'''
    encounter builder
    References: https://github.com/blawson69/ItemDB

'''

import csv
import os
import sys

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.DndProject.dnddice import number_generator

BEAST_NAME = 0

ENC_FILE = "Z:/Maturam/data/encbuilder.csv"
BESTIARY_FILE = "Z:/Maturam/data/d20-bestiary.csv"
NPC_FILE = "Z:/Maturam/data/d20-npcs.csv"
SPELLS_FILE = "Z:/Maturam/data/d20-spells.csv"
FEATS_FILE = "Z:/Maturam/data/d20-feats.csv"
MONSTERS_FILE = "Z:/Maturam/data/d20-monsters.csv"
MAGIC_ITEMS_FILE = "Z:/Maturam/data/d20-magicitems.csv"
CONSTRUCTS_FILE = "Z:/Maturam/data/d20-constructs.csv"


def enc_budget_multiplier(ebm_num_creatures, ebm_party_size):
    ''' encounter budget multiplier '''
    ebm_result = 1
    choice = ebm_num_creatures
    party = ebm_party_size
    match choice:
        case 1:
            match party:
                case 2:
                    ebm_result = 0.67
                case party if 3 <= party <= 5:
                    ebm_result = 1.00
                case _:
                    ebm_result = 1.50
        case 2:
            match party:
                case 2:
                    ebm_result = 0.5
                case party if 3 <= party <= 5:
                    ebm_result = 0.67
                case _:
                    ebm_result = 1.00
        case choice if 3 <= choice <= 6:
            match party:
                case 2:
                    ebm_result = 0.4
                case party if 3 <= party <= 5:
                    ebm_result = 0.5
                case _:
                    ebm_result = 0.67
        case choice if 7 <= choice <= 10:
            match party:
                case 2:
                    ebm_result = 0.33
                case party if 3 <= party <= 5:
                    ebm_result = 0.4
                case _:
                    ebm_result = 0.33
        case choice if 11 <= choice <= 14:
            match party:
                case 2:
                    ebm_result = 0.25
                case party if 3 <= party <= 5:
                    ebm_result = 0.33
                case _:
                    ebm_result = 0.25
        case choice if choice >= 15:
            match party:
                case 2:
                    ebm_result = 0.20
                case party if 3 <= party <= 5:
                    ebm_result = 0.25
                case _:
                    ebm_result = 0.20
        case _:
            print("[-] Error Defaulting to 1.0")
    return ebm_result


def enc_read_csv_file(ercf_filename):
    ''' read csv file '''
    ercf_result = []
    with open(ercf_filename,
              'r',
              encoding='utf-8-sig') as ercf_csvfile:
        ercf_data = csv.reader(ercf_csvfile, delimiter=',')
        for row in ercf_data:
            ercf_result.append(row)
    return ercf_result


def main():
    ''' encounter builder'''
    print("[Encounter Builder] Starting...")
    enc_data = enc_read_csv_file(ENC_FILE)
    beast_data = enc_read_csv_file(BESTIARY_FILE)
    npc_data = enc_read_csv_file(NPC_FILE)
    spell_data = enc_read_csv_file(SPELLS_FILE)
    feat_data = enc_read_csv_file(FEATS_FILE)
    monsters_data = enc_read_csv_file(MONSTERS_FILE)
    magic_items_data = enc_read_csv_file(MAGIC_ITEMS_FILE)
    constructs_data = enc_read_csv_file(CONSTRUCTS_FILE)
    enc_budget = 0
    print("[Encounter Builder] Data loaded from CSV files"
          f"\n\t[*] beasts      : {len(beast_data)} LOADED"
          f"\n\t[*] npcs        : {len(npc_data)} LOADED"
          f"\n\t[*] feats       : {len(feat_data)} LOADED"
          f"\n\t[*] monsters    : {len(monsters_data)} LOADED"
          f"\n\t[*] spells      : {len(spell_data)} LOADED"
          f"\n\t[*] magic items : {len(magic_items_data)} LOADED"
          f"\n\t[*] constructs  : {len(constructs_data)} LOADED")
    print("[Encounter Builder] Generating an encounter")
    main_input = input("\t[-] Party Level : ")
    if not main_input.isnumeric():
        print("[+] Please enter a number")
    else:
        main_input = input("\t[-] Party Size  : ")
        if not main_input.isnumeric():
            print("[+] Please enter a number")
        else:
            if int(main_input) > 5:
                print("[+] Party size is too large")
                party = 5
            else:
                party = int(main_input)
            enc_budget = enc_data[int(main_input)][party-1]
        main_monster = input("\t[-] Monster     : ")
        if not main_monster.isnumeric():
            print("[+] Please enter a number")
        else:
            main_bm = enc_budget_multiplier(int(main_monster),
                                            party)
            final_enc_budget = float(enc_budget) * main_bm
            print(f'\t[*] Budget      : {int(final_enc_budget)}')
    print("[Encounter Builder] Generating a monster...")
    beast_number = number_generator(len(beast_data))
    print(f'\t[-] Monster:[{beast_number}]'
          f' {beast_data[beast_number][BEAST_NAME]}')
    print("[Encounter Builder] Complete")


if __name__ == "__main__":
    main()
