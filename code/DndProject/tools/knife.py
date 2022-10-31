'''
    knife tool for DnDProject
'''
def main():
    '''
        main function
    '''
    with open("knifeinput.txt", "r", encoding='UTF8') as file:
        lines = file.readlines()

    with open("knifeoutput.txt", "w", encoding='UTF8') as file:
        for line in lines:
            temp = line.split(',')
            file.write(f'"{temp[1].strip()}", \n')

if __name__ == "__main__":
    main()
