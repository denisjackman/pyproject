'''
    knife tool for DnDProject
'''
def main():
    '''
        main function
    '''
    with open("knifeinput.txt", "r", encoding='utf-8-sig') as file:
        lines = file.readlines()

    with open("knifeoutput.txt", "w", encoding='utf-8-sig') as file:
        for line in lines:
            temp = line.split(',')
            file.write(f'"{temp[1].strip()}", \n')

if __name__ == "__main__":
    main()
