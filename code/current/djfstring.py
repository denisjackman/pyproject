''' F string example'''
import datetime
import random
import requests
from bs4 import BeautifulSoup

URL = "https://www.maidenheadthicketbowls.org/"


def webscrape(url):
    '''Returns title of webpage'''
    page = requests.get(url, timeout=5)
    soup = BeautifulSoup(page.content, 'html.parser')
    links = soup.find_all('a')
    return links


def password_generator(passlen=8, uppernum=2, numlen=2, symlen=2):
    '''Returns password'''
    password = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    upperalpha = alpha.upper()
    numbers = '0123456789'
    symbols = '!@#$%^&*()_+'
    upnum = uppernum
    numnum = numlen
    numsym = symlen
    for _ in range(passlen):
        item = random.randint(1, 4)
        if item == 1 and upnum > 0:
            password += random.choice(upperalpha)
            upnum -= 1
        elif item == 2 and numnum > 0:
            password += random.choice(numbers)
            numnum -= 1
        elif item == 3 and numsym > 0:
            password += random.choice(symbols)
            numsym -= 1
        else:
            password += random.choice(alpha)
    return password


def get_vowels(String):
    '''Returns vowels from a string'''
    vowels = [char for char in String if char in 'aeiou']
    return vowels


def defang_ip(ip):
    '''Returns defanged IP'''
    defanged = ip.replace('.', '[.]')
    return defanged


def main():
    '''Main function'''
    strnow = datetime.datetime.now()
    salary = 100000
    name = 'Derek'
    age = 43
    message = f'Hello {name}, you are {age} years old.'
    ip = '40.124.45.157'
    print("[+] Main function Started""")
    print(f'[-] Today is {strnow:%Y-%m-%d %H:%M}')
    print(f'[-] My Salary is : £{salary:,}')
    print("[-] Message Length :  "
          f"{len(message):<10}"
          ", message : '"
          f"{message:^20}'")
    print(f"[-] Vowels in message : {get_vowels(message)}")
    print(f'[-] IP: {ip} Defanged IP : {defang_ip(ip)}')
    print(f'[-] Password : {password_generator()} {len(password_generator())}')
    print(f'[-] Getlinks : {webscrape(URL)}')
    print("[+] Main function Complete")


if __name__ == '__main__':
    main()
