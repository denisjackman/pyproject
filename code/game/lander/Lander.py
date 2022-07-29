#!/usr/bin/python
'''
lunar_lander.py
basic lunar lander simulation based on constraints found at:
http://www.cs.carleton.edu/faculty/dmusican/cs111s10/lunarlander.html
'''

#lunar_lander.py
import sys
sys.path.append('./Classes')
import LunarLander

def main():
    '''
        main function
    '''
    print('Welcome to Lunar Lander!')
    lander = LunarLander.LunarLander()
    running = True
    while running:
        lander.report()
        x = 0
        x = input('input thrust: ')
        lander.tick(x)

main()
