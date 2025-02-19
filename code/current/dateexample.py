'''
    time zone script
'''
from datetime import datetime


def main():
    ''' main function '''

    naive = datetime.now()
    aware = naive.astimezone()
    print(f'naive: {naive}, aware: {aware}')


if __name__ == "__main__":
    main()
