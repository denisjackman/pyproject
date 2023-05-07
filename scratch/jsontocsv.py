''' JSON to CSV converter script'''
import json

INPUTFILE = "y:/pyproject/data/input.json"
OUTPUTFILE = "y:/pyproject/data/output.csv"

def jsontocsv(inputfile, outputfile):
    '''Converts JSON file to CSV file'''
    try:
        with open(inputfile, 'r', encoding='utf8') as infile:
            data = json.loads(infile.read())

        output = ','.join([*data[0]])
        for obj in data:
            output += f'\n{obj["Name"]},{obj["age"]},{obj["birthyear"]}'

        with open(outputfile, 'w', encoding='utf8') as outfile:
            outfile.write(output)
    except Exception as ex:
        print(f'Error: {str(ex)}')

def main():
    '''Main function'''
    jsontocsv(INPUTFILE, OUTPUTFILE)

if __name__ == '__main__':
    main()
