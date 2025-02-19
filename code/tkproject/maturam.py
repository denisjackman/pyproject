''' This is a DM helper for Maturam'''

import os
import sys

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.DndProject.dndother import book_title_generator
from jackmanimation.DndProject.dndother import riddle_generator
from jackmanimation.DndProject.dndother import currency_converter
from jackmanimation.DndProject.dndother import organization_name_generator
from jackmanimation.DndProject.dndnames import dwarven_name
from jackmanimation.DndProject.dndnames import elfname_generator
from jackmanimation.DndProject.dndnames import orc_name_generator
from jackmanimation.DndProject.dndnames import lizardman_name_generator
from jackmanimation.DndProject.dnddice import dice


def organization_name(on_num):
    ''' generate organization names '''
    on_list = []
    for _ in range(on_num):
        on_list.append(organization_name_generator())
    return on_list


def convert_currency(cc_amount, cc_from, cc_to):
    ''' convert currency '''
    return currency_converter(cc_amount, cc_from, cc_to)


def name_generator(ng_number, ng_type="random"):
    ''' generate names '''
    name_list = []
    if ng_type == "dwarf":
        for _ in range(ng_number):
            name_list.append(f'(d): {dwarven_name()}')
    elif ng_type == "elf":
        for _ in range(ng_number):
            name_list.append(f'(e): {elfname_generator()}')
    elif ng_type == "orc":
        for _ in range(ng_number):
            name_list.append(f'(o): {orc_name_generator()}')
    elif ng_type == "lizardman":
        for _ in range(ng_number):
            name_list.append(f'(l): {lizardman_name_generator()}')
    else:
        for _ in range(ng_number):
            ng_roll = dice(4, 1)
            if ng_roll == 1:
                name_list.append(f'(d): {dwarven_name()}')
            elif ng_roll == 2:
                name_list.append(f'(e): {elfname_generator()}')
            elif ng_roll == 3:
                name_list.append(f'(o): {orc_name_generator()}')
            else:
                name_list.append(f'(l): {lizardman_name_generator()}')
    return name_list


def books(num_books):
    ''' generate book titles '''
    books_list = []
    for _ in range(num_books):
        books_list.append(book_title_generator(True))
    return books_list


def riddles(num_riddles):
    ''' generate riddles '''
    riddles_list = []
    for _ in range(num_riddles):
        r_temp = riddle_generator()
        riddles_list.append(r_temp)
    return riddles_list


def main():
    ''' main function'''
    print("[Maturam] Starting...")
    print("[Maturam] Generating a book title...")
    book_list = books(10)
    count = 0
    for book_title in book_list:
        print(f"\t[-] [{count}] The book title is: {book_title}")
        count += 1
    print("[Maturam] Generating a riddle...")
    riddle_list = riddles(10)
    count = 0
    for riddle in riddle_list:
        print(f"\t[-] [{count}] The riddle is: {riddle}")
        count += 1
    print("[Maturam] Generating names...")
    name_list = name_generator(10)
    for name in name_list:
        print(f"\t[-] The name is: {name}")

    print("[Maturam] Converting currency...")
    main_temp = convert_currency(1000, 'gold', 'silver')
    print(f"\t[-] 1000 gold pieces is {main_temp} silver pieces")

    print("[Maturam] Generating organization names...")
    organisation_lists = organization_name(10)
    for organisation in organisation_lists:
        print(f"\t[-] The organization name is: {organisation}")
    print("[Maturam] Exiting...")


if __name__ == "__main__":
    main()
