'''
lunar_lander.py
basic lunar lander simulation based on constraints found at:
http://www.cs.carleton.edu/faculty/dmusican/cs111s10/lunarlander.html
'''
from Classes import LunarLander


def main():
    '''
        main function
    '''
    print('Welcome to Lunar Lander!')
    lander = LunarLander.LunarLander()
    running = True
    while running:
        lander.report()
        x = int(input('input thrust: '))
        lander.tick(x)
        if lander.start is False:
            running = False


main()
