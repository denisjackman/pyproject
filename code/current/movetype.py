#!/usr/bin/env python
'''
    movetype
'''


def main():
    """ This is the main routine for the program """
    print("Starting the sequence:")
    print("Starting ")
    count = 0
    with open("Z:/Resources/text/500_inn_names.txt",
              "r",
              encoding='utf-8-sig') as file:
        filelines = file.readlines()
        for files in filelines:
            count += 1
            print(files.strip())
    print(f"count: {count} Length: {len(filelines)}")
    print("Finishing")
    print("finishing up and closing down:")


if __name__ == '__main__':
    main()
