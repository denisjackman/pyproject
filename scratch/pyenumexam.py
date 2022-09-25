'''
example of file enumerate
'''
def main():
    ''' main function '''
    with open('y:/Resources/text/500_inn_names.txt', 'r', encoding='utf8') as file:
        for index, line in enumerate(file):
            print(f'Index: {index + 1} Line: {line.strip()}')

if __name__ == "__main__":
    main()
