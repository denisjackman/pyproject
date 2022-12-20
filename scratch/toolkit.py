''' toolkit.py '''

from pathlib import Path
import json

FILEPATH = Path(__file__).parent

def main():
    ''' main function '''
    filename = f"{FILEPATH}/allMimeTypes.json"
    with open(filename, "r", encoding='utf8') as file:
        result = json.load(file)

    mime_types = []
    mime_file = []
    test_example = "text/x-python"

    for item in result:
        print(item.values())
        print(item.keys())
        mime_types.append(item.keys())
        mime_file.append(item.values())


    print(mime_types)
    print(mime_file)
    print(test_example)

if __name__ == "__main__":
    main()
