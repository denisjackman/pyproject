'''
    this converts a tab file into a json file
'''
FILE_ADDRESS = "Y:/Resources/data/Adventuring/Riddles.tab"

def main():
    '''
        main function
    '''
    question = False
    answer = False
    with open(FILE_ADDRESS, "r", encoding='UTF8') as file:
        lines = file.readlines()

    for line in lines:
        if line.startswith("#") is False:
            if line.startswith(":Question") is True:
                question = True
            if question:
                if line.startswith(":Answer") is True:
                    question = False
                    answer = True
                print(f'QUESTION: {line.strip()}')
            if answer:
                print(f'ANSWER: {line.strip()}')
        #print(line.strip())
if __name__ == "__main__":
    main()
