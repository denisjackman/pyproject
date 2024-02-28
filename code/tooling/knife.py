'''
    knife tool for DnDProject
'''
FILEPATH = "Z:/Resources/development/"


def main():
    '''
        main function
    '''
    with open('Z:/Resources/development/knifeinput.txt',
              "r",
              encoding='utf-8-sig') as file:
        lines = file.readlines()

    with open('Z:/Resources/development/knifeoutput.txt',
              "w",
              encoding='utf-8-sig') as file:
        for line in lines:
            temp = line.split(',')
            file.write(f'"{temp[1].strip()}", \n')


if __name__ == "__main__":
    main()
