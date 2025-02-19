''' this is a function to check if a number is an armstrong number or not'''
from __future__ import annotations
import os
import sys

# pylint: disable=C0413

sys.path.append(os.path.realpath('../..'))
from jackmanimation.genfunctions.various import isArmstrong


def main():
    '''
    this is a function to check if a
    number is an armstrong number or not
    '''
    print(f"662 is an armstrong number {isArmstrong(662)}")
    print(f"663 is an armstrong number {isArmstrong(663)}")
    print(f"407 is an armstrong number {isArmstrong(407)}")


if __name__ == "__main__":
    main()
