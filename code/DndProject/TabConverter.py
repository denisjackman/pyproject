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
    question_list = []
    answers_list = []
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
                else:
                    if ',' in line:
                        question_list.append(line[line.index(',')+1:].strip())
            if answer:
                if ',' in line:
                    answers_list.append(line[line.index(',')+1:].strip())

    #for item in question_list:
    #    print(item)
    print(f' question_list : {question_list}')
    print(f' answers_list : {answers_list}')
    print(f"question list length: {len(question_list)}, answers list length: {len(answers_list)}")
    #print(f" question 1 : {question_list[0][question_list[0].index(',')+1:]} : {answers_list[0][answers_list[0].index(',')+1:]}")

if __name__ == "__main__":
    main()
