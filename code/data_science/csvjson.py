'''
    example of dumping csv to json
'''
import csv
import json


def main():
    '''
        main routine
    '''
    with open("Z:/Resources/Data/data.csv",
              'r',
              encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        with open("Z:/Resources/Data/data.json",
                  'w',
                  encoding='utf-8-sig') as json_file:
            json_file.write("[")
            for line in csv_reader:
                json.dump(line, json_file)
                json_file.write(",")
            json_file.write("]")


if __name__ == '__main__':
    main()
