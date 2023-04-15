'''
    example of dumping csv to json
'''
import csv
import json

def main():
    '''
        main routine
    '''
    with open("Y:/Resources/Data/data.csv", 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        with open("Y:/Resources/Data/data.json", 'w', encoding='utf-8') as json_file:
            json_file.write("[")
            for line in csv_reader:
                json.dump(line, json_file)
                json_file.write(",")
            json_file.write("]")

if __name__ == '__main__':
    main()
