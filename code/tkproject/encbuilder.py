'''
    encounter builder
    References: https://github.com/blawson69/ItemDB

'''

import csv
import os
import sys

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.DndProject.dnddice import number_generator  # noqa: E402, E501


ENC_FILE = "Z:/Maturam/data/encbuilder.csv"
BESTIARY_FILE = "Z:/Maturam/data/d20-bestiary.csv"
NPC_FILE = "Z:/Maturam/data/d20-npcs.csv"
SPELLS_FILE = "Z:/Maturam/data/d20-spells.csv"
FEATS_FILE = "Z:/Maturam/data/d20-feats.csv"


def enc_budget_multiplier(ebm_num_creatures, ebm_party_size):
    ''' encounter budget multiplier '''
    ebm_result = 1
    choice = ebm_num_creatures
    party = ebm_party_size
    match choice:
        case 1:
            match party:
                case 2:
                    return 0.67
                case party if 3 <= party <= 5:
                    return 1.00
                case _:
                    return 1.50
        case 2:
            match party:
                case 2:
                    return 0.5
                case party if 3 <= party <= 5:
                    return 0.67
                case _:
                    return 1.00
        case choice if 3 <= choice <= 6:
            match party:
                case 2:
                    return 0.4
                case party if 3 <= party <= 5:
                    return 0.5
                case _:
                    return 0.67
        case choice if 7 <= choice <= 10:
            match party:
                case 2:
                    return 0.33
                case party if 3 <= party <= 5:
                    return 0.4
                case _:
                    return 0.33
        case choice if 11 <= choice <= 14:
            match party:
                case 2:
                    return 0.25
                case party if 3 <= party <= 5:
                    return 0.33
                case _:
                    return 0.25
        case choice if choice >= 15:
            match party:
                case 2:
                    return 0.20
                case party if 3 <= party <= 5:
                    return 0.25
                case _:
                    return 0.20
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
    print("[Encounter Builder] Data loaded from CSV files"
          f"\n\tmonsters : {len(beast_data)} LOADED"
          f"\n\tnpcs     : {len(npc_data)} LOADED"
          f"\n\tfeats    : {len(feat_data)} LOADED"
          f"\n\tspells   : {len(spell_data)} LOADED")
    print("[Encounter Builder] Generating an encounter")
    main_input = input("[-] Party Level: ")
    if not main_input.isnumeric():
        print("[+] Please enter a number")
    else:
        main_party_size = input("[-] Party Size: ")
        if not main_party_size.isnumeric():
            print("[+] Please enter a number")
        else:
            enc_budget = enc_data[int(main_input)][int(main_party_size)-1]
        main_monster = input("[-] Monster: ")
        if not main_monster.isnumeric():
            print("[+] Please enter a number")
        else:
            main_bm = enc_budget_multiplier(int(main_monster),
                                            int(main_party_size))
            final_enc_budget = float(enc_budget) * main_bm
            print(f'[*] {int(final_enc_budget)}')
    print("[Encounter Builder] Generating a monster...")
    beast_number = number_generator(len(beast_data))
    beast_name = 0
    print(f'[-] Monster:[{beast_number}]'
          f' {beast_data[beast_number][beast_name]}')
    # print("[Encounter Builder] Generating a trap...")
    # print("[Encounter Builder] Generating a treasure...")
    # print("[Encounter Builder] Generating a name...")
    print("[Encounter Builder] Complete")


if __name__ == "__main__":
    main()