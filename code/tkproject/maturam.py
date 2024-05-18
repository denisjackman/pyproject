''' This is a DM helper for Maturam'''

import os
import sys

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.DndProject.dndother import book_title_generator  # noqa: E402, E501


def books(num_books):
    ''' generate book titles '''
    books_list = []
    for _ in range(num_books):
        books_list.append(book_title_generator())
    return books_list


def main():
    ''' main function'''
    print("[Maturam] Starting...")
    print("[Maturam] Generating a book title...")
    book_list = books(10)
    count = 0
    for book_title in book_list:
        print(f"\t[-] [{count}] The book title is: {book_title}")
        count += 1
    print("[Maturam] Exiting...")


if __name__ == "__main__":
    main()
