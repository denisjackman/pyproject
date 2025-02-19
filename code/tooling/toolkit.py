''' toolkit.py '''

from pathlib import Path
import json

FILEPATH = Path(__file__).parent


def main():
    ''' main function '''
    filename = "Z:/Resources/Data/allMimeTypes.json"
    with open(filename, "r", encoding='utf-8-sig') as file:
        result = json.load(file)

    mime_types = []
    mime_file = []
    test_example = "text/x-python"

    for item in result:
        if test_example in item.keys():
            print("Found")
            print(item.values())
            result = list(item.values())
            print(result[0])
            if 'py' in result[0]:
                print("Found")
        mime_types.append(item.keys())
        mime_file.append(item.values())

    print(test_example)


if __name__ == "__main__":
    main()
