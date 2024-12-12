''' username check '''


def username_check(uc_name):
    ''' username check'''
    result = []
    result_check = True
    uc_numbers = '0123456789'
    uc_lc_letters = 'abcdefghijklmnopqrstuvwxyz'
    uc_uc_letters = uc_lc_letters.upper()
    uc_uc_check = False
    uc_lc_check = False
    uc_nu_check = False
    uc_check = list(uc_name)
    for item in uc_check:
        if item in uc_lc_letters:
            uc_lc_check = True
        elif item in uc_uc_letters:
            uc_uc_check = True
    uc_nu_check = uc_check[-1].isdigit()
    if uc_uc_check is False:
        result_check = False
        result.append("You did not use an Uppercase Character")
    if uc_lc_check is False:
        result_check = False
        result.append("You did not use a Lowercase Character")
    if uc_nu_check is False:
        result_check = False
        result.append("You did not use a Number Character")

    if result_check:
        result.append("Your username passed all 3 requirements")
    return result_check, result


if __name__ == '__main__':
    print(f'1 {username_check("Denis1")}')
    print(f'2 {username_check("DENIS1")}')
    print(f'3 {username_check("denis1")}')
    print(f'4 {username_check("111111")}')
    print(f'5 {username_check("######")}')
