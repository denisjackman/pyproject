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
    print(f'{df.columns}')
    print(f'{df.loc[:, "continent"]}')
    df2 = df.copy()
    df2.loc[1, "name"] = "JOHN"
    df2.replace("USA", "United States")
    print(f'{df2}')
    print('[-] dapandas.py main()   : end')
    users = pd.DataFrame(data=[" mArk ", "JOHN ", "Tim", " jenny"],
                         columns=["name"])
    print(f'{users}')
    users_clean = users.loc[:, "name"].str.strip().str.capitalize()
    print(f'{users_clean}')


if __name__ == '__main__':
    main()
