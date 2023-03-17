''' this is a function to check if a number is an armstrong number or not'''

def isArmstrong(number):
    ''' this is a function to check if a number is an armstrong number or not'''
    result = False
    total = 0
    temp = number

    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp //= 10
    if number == total:
        result = True
    return result

def main():
    ''' this is a function to check if a number is an armstrong number or not'''
    print (f"662 is an armstrong number {isArmstrong(662)}")
    print (f"663 is an armstrong number {isArmstrong(663)}")
    print (f"407 is an armstrong number {isArmstrong(407)}")
    
if __name__ == "__main__":
    main()
