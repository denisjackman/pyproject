'''
    roman numeral
'''
def int_to_roman (integer):
    '''
        integer to roman
    '''
    returnstring=''
    table=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
    for pair in table:
        while integer-pair[1]>=0:
            integer-=pair[1]
            returnstring+=pair[0]
    return returnstring

def roman_to_int(string):
    '''
        roman to integer
    '''
    table=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
    returnint=0
    for pair in table:
        continueyes=True
        while continueyes:
            if len(string)>=len(pair[0]):
                if string[0:len(pair[0])]==pair[0]:
                    returnint+=pair[1]
                    string=string[len(pair[0]):]
                else: continueyes=False
            else: continueyes=False
    return returnint

print(int_to_roman(2000))
print(int_to_roman(2) + " - " + int_to_roman(3) + " - " + int_to_roman(1965))
print(int_to_roman(3) + " - " + int_to_roman(2) + " - " + int_to_roman(1967))
print(int_to_roman(11) + " - " + int_to_roman(8) + " - " + int_to_roman(1990))
print(int_to_roman(12) + " - " + int_to_roman(8) + " - " + int_to_roman(1994))
print(int_to_roman(15) + " - " + int_to_roman(1) + " - " + int_to_roman(1997))
print(int_to_roman(2) + " - " + int_to_roman(2) + " - " + int_to_roman(1999))
