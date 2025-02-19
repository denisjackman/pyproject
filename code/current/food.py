'''
    food generator
'''
from __future__ import annotations
import os
import sys

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.genfunctions.utensils import dish


def main():
    '''
        main function
    '''
    for _ in range(10):
        print(dish())


# Main loops
if __name__ == "__main__":
    main()
