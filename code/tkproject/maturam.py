''' This is a DM helper for Maturam'''

import os
import sys
from random import randint

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.DndProject.dndother import book_title_generator  # noqa: E402, E501
from jackmanimation.DndProject.dndother import riddle_generator  # noqa: E402, E501
from jackmanimation.DndProject.dndnames import dwarven_name  # noqa: E402, E501
from jackmanimation.DndProject.dndnames import elfname_generator  # noqa: E402, E501
from jackmanimation.DndProject.dndnames import orc_name_generator  # noqa: E402, E501
from jackmanimation.DndProject.dndnames import lizardman_name_generator  # noqa: E402, E501


def name_generator(ng_number, ng_type="random"):
    ''' generate names '''
    name_list = []
    if ng_type == "dwarf":
        for _ in range(ng_number):
            name_list.append(dwarven_name())
    elif ng_type == "elf":
        for _ in range(ng_number):
            name_list.append(elfname_generator())
    elif ng_type == "orc":
        for _ in range(ng_number):
            name_list.append(orc_name_generator())
    elif ng_type == "lizardman":
        for _ in range(ng_number):
            name_list.append(lizardman_name_generator())
    else:
        for _ in range(ng_number):
            ng_roll = randint(1, 4)
            if ng_roll == 1:
                name_list.append(dwarven_name())
            elif ng_roll == 2:
                name_list.append(elfname_generator())
            elif ng_roll == 3:
                name_list.append(orc_name_generator())
            else:
                name_list.append(lizardman_name_generator())
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
        riddles_list.append(riddle_generator())
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
    print("[Maturam] Exiting...")


if __name__ == "__main__":
    main()
