'''
    a list of useful functions built in python
'''
import os
import sys
# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.genfunctions.searchutils import bubble_sort


def main():
    '''
        main routine
    '''
    print("Starting now : ")
    arr = ['t', 'u', 't', 'o', 'r', 'i', 'a', 'l']
    print(f"array is : {str(arr)}")
    print(f"after array is {str(bubble_sort(arr))}")
    print("Ending now")


if __name__ == '__main__':
    main()
