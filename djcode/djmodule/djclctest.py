''' this is to test the calculator module '''
from calculator import add
from calculator import subtract
from calculator import multiply
from calculator import divide

def main():
    ''' main function '''
    print(add(1,2) == 3)
    print(subtract(2,1) == 1)
    print(multiply(1,2) == 2)
    print(divide(1,2) == 0.5)

if __name__ == '__main__':
    main()
