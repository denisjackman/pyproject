'''
This is a quiz 97

based on the following code, what will be the output?
a) Dhohli
b) Kohni
c) Dhoohli
d) none of the above

the answer is : c) Dhoohli

the explanation is that the slice of name1 is 'Dho' and
the slice of name2 is 'ohli' so the result is 'Dhoohli'

'''


def question1():
    ''' This is a question 1'''
    name1 = 'Dhoni'
    name2 = 'Kohli'
    result = name1[:3] + name2[1:]
    print(f'[-] question 1 : {result}')


def main():
    ''' This is the main function'''
    print('[*] This is the main function starting')
    question1()
    print('[*] This is the main function ending')


if __name__ == '__main__':
    print('[+] This is the quiz 97 program starting')
    main()
    print('[+] This is the quiz 97 program ending')
