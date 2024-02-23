'''
a trawl through inn names
'''


def main():
    ''' main function '''
    with open('Z:/Resources/text/500_inn_names.txt',
              'r',
              encoding='utf-8-sig') as file:
        for index, line in enumerate(file):
            print(f'Index: {index + 1} Line: {line.strip()}')


if __name__ == "__main__":
    main()
