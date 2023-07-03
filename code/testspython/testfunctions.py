'''
    a list of useful functions built in python
'''
from djgamemodule import functions as fn

def main():
    '''
        main routine
    '''
    print("Starting now : ")
    arr = ['t','u','t','o','r','i','a','l']
    x = 'a'
    print("element found at index "+str(fn.linearsearch(arr,x)))
    print("Ending now")
    listofnumbers = [1, 2, 3, 5, 6, 7, 8, 9]
    print(fn.findmissingnumbers(listofnumbers))


if __name__ == '__main__':
    main()
