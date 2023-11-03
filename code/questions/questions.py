''' This is a questions scratch pad'''
def question1():
    ''' This is a question 1'''
    print('[-] This questions 1 ')
    name1 = 'Dhoni'
    name2 = 'Kohli'
    result = name1[:3] + name2[1:]
    print(f'[-] question 1 : {result}')

def question2():
    ''' This is a question 2'''
    mylist = ["python", "hub"]
    for i in mylist:
        mylist.append(i.upper())
    print(f'[-] question 2 : {mylist}')

def question3(a, b, c):
    ''' This is a question 3'''
    if a > b:
        if a > c:
            return a
    elif b > c:
        return b
    else:
        return c
    return 0
    
def main():
    ''' This is the main function'''
    print('[+] This is the main function starting')
    question1()
    #question2()
    print(f'[-] question 3 {question3(10,5,2)}')
    print('[+] This is the main function ending')

if __name__ == '__main__':
    main()
