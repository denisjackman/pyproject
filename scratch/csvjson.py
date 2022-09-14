'''
    example of dumping csv to json
'''
import csv
import json

def main():
    '''
        main routine
    '''
    print(json.dumps(list(csv.reader(open("data.csv", 'r', encoding='utf-8')))))
    # TODO: change this to dump the json to a file instead of stdout

if __name__ == '__main__':
    main()
