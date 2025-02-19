'''
    example of dumping csv to json
'''
import csv


def main():
    '''
        main routine
    '''
    count = 0
    with open("Z:/Store/house-data/consolidated.csv",
              'r',
              encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            if line['Transaction Date'].endswith('/2022'):
                print(line)
                count += 1
    print(f'count: {count}')


if __name__ == '__main__':
    main()
