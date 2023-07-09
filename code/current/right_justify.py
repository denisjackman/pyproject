'''
    right justify
'''
import os
import sys

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.myfunctions.utensils import right_justify

if __name__ == "__main__":
    print(right_justify('denis'))
