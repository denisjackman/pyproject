''' toolkit.py '''

from pathlib import Path
import json

FILEPATH = Path(__file__).parent

def main():
    ''' main function '''
    filename = f"Y:/Resources/Data/allMimeTypes.json"
    with open(filename, "r", encoding='utf8') as file:
        result = json.load(file)

    mime_types = []
    mime_file = []
    test_example = "text/x-python"

    for item in result:
        #print(item.values())
        #print(item.keys())
        if test_example in item.keys():
            print("Found")
            print(item.values())
            result = list(item.values())
            print(result[0])
            if 'py' in result[0]:
                print("Found")
        mime_types.append(item.keys())
        mime_file.append(item.values())


    #print(mime_types)
    #print(mime_file)
    print(test_example)
    #print(mime_types.get(test_example))
if __name__ == "__main__":
    main()
