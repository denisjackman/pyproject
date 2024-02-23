''' JSON to CSV converter script'''
import json

INPUTFILE = "Z:/Resources/development/input.json"
OUTPUTFILE = "Z:/Resources/development/output.csv"


def jsontocsv(inputfile, outputfile):
    '''Converts JSON file to CSV file'''
    try:
        with open(inputfile, 'r', encoding='utf-8-sig') as infile:
            data = json.loads(infile.read())

        output = ','.join([*data[0]])
        for obj in data:
            output += f'\n{obj["Name"]},{obj["age"]},{obj["birthyear"]}'

        with open(outputfile, 'w', encoding='utf-8-sig') as outfile:
            outfile.write(output)
    except Exception as ex:
        print(f'Error: {str(ex)}')


def main():
    '''Main function'''
    jsontocsv(INPUTFILE, OUTPUTFILE)


if __name__ == '__main__':
    main()
