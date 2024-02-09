'''Data builder '''

from faker import Faker

def fk_email(fk_em_gen):
    '''Email generator'''
    result = []
    for _ in range(fk_em_gen):
        result.append(Faker().email())
    return result

def fk_name(fk_name_gen):
    '''Name generator'''
    result = []
    for _ in range(fk_name_gen):
        result.append(Faker().name())
    return result

def fk_url(fk_url_gen):
    '''URL generator'''
    result = []
    for _ in range(fk_url_gen):
        result.append(Faker().url())
    return result

def main():
    '''Main function'''
    print('[+] Main Function Starting...')
    gen_emails = fk_email(10)
    gen_names = fk_name(10)
    gen_urls = fk_url(10)
    for item in gen_emails:
        print(f'[*] {item}')
    for item in gen_names:
        print(f'[*] {item}')
    for item in gen_urls:
        print(f'[*] {item}')
            
#    for _ in range(10):
#        print(f'[*] {fake.address()}')
#        print(f'[*] {fake.text()}')
#        print(f'[*] {fake.date()}')
#        print(f'[*] {fake.country()}')
    print('[-] Main Function Finished.')

if __name__ == '__main__':
    main()
