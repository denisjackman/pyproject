'''
    password checker
        get the password froma password file
        check if the password meets the listed requirements
        if it does not meet the requirements - print out a message
        if it does - print out a message

        Your password must conform to the following constraints:
            Minimum length: 12
            Maximum length: 45
            Minimum number of lowercase characters: 2
            Minimum number of uppercase characters: 2
            Minimum number of digits: 2
            Minimum number of special characters: 2
        Your new password may not be the same as your old password
        Your new password may not be the same as your login


        Minimum of 14 Characters
        Not the same as the previous 12 passwords
        Must be a complex password:
            The password contains characters from three of
            the following categories:
                Uppercase letters of European languages
                (A through Z, with diacritic marks,
                Greek and Cyrillic characters)
                Lowercase letters of European languages
                (a through z, sharp-s, with diacritic marks,
                Greek and Cyrillic characters)
                Base 10 digits (0 through 9)
                Non-alphanumeric characters (special characters):
                Currency symbols such as the Euro or British Pound
                are not counted as special characters for this policy setting.
                Any Unicode character that is categorized as an alphabetic
                character but is not uppercase or lowercase.
                This includes Unicode characters from Asian languages.

'''
MINPASSWORDLENGTH = 12
MAXPASSWORDLENGTH = 45
PASSWORDALPHA = 'abcdefghijklmnopqrstuvwxyz'
PASSWORDUPPERALPHA = PASSWORDALPHA.upper()
PASSWORDNUMBERS = '0123456789'
PASSWORDSYMBOLS = r"~!@#$%^&*_-+=`|\(){}[]:;'<>,.?/"
MINALPHA = 2
MINNUMBERS = 2
MINSYMBOLS = 2
MINUPPER = 2


def read_password_file():
    ''' read the password file '''
    with open(r'Z:/Resources/project/password.txt',
              'r',
              encoding='utf-8-sig') as passwordfile:
        reqs = passwordfile.readlines()
    return reqs


def check_password(password):
    ''' check the password'''
    password = password.strip()
    result = f"[ ] Password - {password}"
    fail = False
    if len(password) <= MINPASSWORDLENGTH - 1:
        print(f"{result} is too short...{len(password)}")
        fail = True
    if len(password) > MAXPASSWORDLENGTH:
        print(f"{result} is too long...{len(password)}")
        fail = True
    return fail


def password_integrity(password):
    '''check password integrity'''
    password = password.strip()
    result = True
    isupper = 0
    islower = 0
    isnumber = 0
    issymbol = 0

    for _ in range(len(password)):
        if password[_] in PASSWORDUPPERALPHA:
            isupper += 1
        if password[_] in PASSWORDALPHA:
            islower += 1
        if password[_] in PASSWORDNUMBERS:
            isnumber += 1
        if password[_] in PASSWORDSYMBOLS:
            issymbol += 1
    if isupper < MINUPPER:
        result = False
        print(f"[FAIL] Password - {password}"
              f" is missing uppercase characters {isupper}")
    if isupper < MINALPHA:
        result = False
        print(f"[FAIL] Password - {password}"
              f" is missing lowerase characters {isupper}")
    if isupper < MINNUMBERS:
        result = False
        print(f"[FAIL] Password - {password}"
              f" is missing numbers {isupper}")
    if isupper < MINSYMBOLS:
        result = False
        print(f"[FAIL] Password - {password}"
              f" is missing symbols {isupper}")
    return result


def main():
    ''' main function '''
    print("[+] Password Checker starting up...")
    print("[+] Reading password file...")
    passwordlist = read_password_file()
    print(f"[-] Total passwords is {len(passwordlist):,}")
    print("[+] Checking password requirements...")
    for password in passwordlist:
        if check_password(password) is False:
            if password_integrity(password) is False:
                print(f"[FAIL] Password - {password.strip()} is invalid")
    print("[+] Password meets requirements...")
    print("[+] Password accepted...")
    print("[+] Password Checker shutting down...")


if __name__ == "__main__":
    main()
