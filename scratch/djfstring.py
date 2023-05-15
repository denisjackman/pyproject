''' F string example'''
import datetime
def main():
    '''Main function'''
    strnow = datetime.datetime.now()
    salary = 100000
    name = 'Derek'
    age = 43
    message = f'Hello {name}, you are {age} years old.'
    print("[+] Main function Started""")
    print(f'[-] Today is {strnow:%Y-%m-%d %H:%M}')
    print(f'[-] My Salary is : £{salary:,}')
    print(f"[-] Message Length :  {len(message):<10}, message : '{message:^20}'")

    print("[+] Main function Complete")

if __name__ == '__main__':
    main()
