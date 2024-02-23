''' This script converts an XML file to JSON format.'''
import json
import xmltodict
INPUTFILE = "Z:/Resources/development/input.xml"
OUTPUTFILE = "Z:/Resources/development/output.json"


def xmltojson(inputfile, outputfile):
    '''Converts XML file to JSON file'''
    with open(inputfile, 'r', encoding='utf-8-sig') as xml_file:
        parsed_data = xmltodict.parse(xml_file.read())

        xml_file.close()

        json_conversion = json.dumps(parsed_data)

        with open(outputfile, 'w', encoding='utf-8-sig') as json_file:
            json_file.write(json_conversion)
            json_file.close()


def main():
    '''Main function'''
    xmltojson(INPUTFILE, OUTPUTFILE)


if __name__ == '__main__':
    main()
