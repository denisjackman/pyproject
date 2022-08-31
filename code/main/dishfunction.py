'''
    food generator
'''
from __future__ import annotations
from myfunctions.utensils import dish

def main():
    '''
        main function
    '''
    for _ in range(10):
        print(dish())

# Main loops
if __name__ == "__main__":
    main()
