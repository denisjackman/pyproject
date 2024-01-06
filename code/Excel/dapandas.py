''' excel python example number 1'''
import pandas as pd

def main():
    ''' main function '''
    print('[-] dapandas.py main()   : start')
    print('[-] dapandas.py main()   : read excel')
    df = pd.read_excel('Z:/Store/xl/course_particpants.xlsx')
    print('[o]')
    print(f'{df}')
    df.sort_values(by=['continent', 'age'])
    print('[o]')
    print(f'{df}')
    print('[-] dapandas.py main()   : end')

if __name__ == '__main__':
    main()
