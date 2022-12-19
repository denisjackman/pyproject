''' toolkit.py '''

from pathlib import Path
import json

FILEPATH = Path(__file__).parent

def main():
    ''' main function '''
    filename = f"{FILEPATH}/allMimeTypes.json"
    with open(filename, "r", encoding='utf8') as file:
        result = json.load(file)
    print(result)
    mime_types = []
    mime_file = []


if __name__ == "__main__":
    main()
