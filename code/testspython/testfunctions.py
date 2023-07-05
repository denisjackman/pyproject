'''
    a list of useful functions built in python
'''
import os
import sys
# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from djmodule.gameitems.gamefunctions import bubbleSort

def main():
    '''
        main routine
    '''
    print("Starting now : ")
    arr = ['t','u','t','o','r','i','a','l']
    print(f"array is : {str(arr)}")
    print(f"after array is {str(bubbleSort(arr))}")
    print("Ending now")


if __name__ == '__main__':
    main()
