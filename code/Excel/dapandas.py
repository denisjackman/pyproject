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
    df.index.name = 'user_id'
    print(f'{df.index}')
    print(f'{df}')
    df.reindex([1000,1001,1002,1003])
    print(f'{df}')
    df.sort_index()
    print(f'{df}')
    print(f'{df.columns}')
    print(f'{df.loc[:, "continent"]}')
    print('[-] dapandas.py main()   : end')

if __name__ == '__main__':
    main()
