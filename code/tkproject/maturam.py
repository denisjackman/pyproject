''' This is a DM helper for Maturam'''

import os
import sys

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.DndProject.dndother import book_title_generator  # noqa: E402, E501


def main():
    ''' main function'''
    print("[Maturam] Starting...")
    print("[Maturam] Generating a book title...")
    book_title = book_title_generator()
    print(f"[-] The book title is: {book_title}")
    print("[Maturam] Exiting...")


if __name__ == "__main__":
    main()
