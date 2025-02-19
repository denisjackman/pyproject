''' panda example '''
import pandas as pd


def main():
    ''' main function '''
    address = pd.DataFrame({'empid': ['E87', 'E22', 'E49'],
                            'City': ['Mumbai', 'NY', 'London'],
                            'Country': ['India', 'US', 'UK']})

    employees = pd.DataFrame({'empid': ['E90', 'E87', 'E22'],
                              'Name': ['Asif', 'Basit', 'Arun']})

    inner = pd.merge(employees, address, on='empid')
    print(f'[-] result is : \n{inner}')
    inner = pd.merge(employees, address, on='empid', how='inner')
    print(f'[-] result is : \n{inner}')
    left = pd.merge(employees, address, on='empid', how='left')
    print(f'[-] result is : \n{left}')


if __name__ == "__main__":
    main()
