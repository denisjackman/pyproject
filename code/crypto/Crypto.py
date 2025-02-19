"""
Crypto.py

This program is a template for python programs

All this stuff at the top of the script is just optional metadata;
the real code starts on the "def Dice(side = 6, rolls = 1)" line
"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2014/04/02 00:31:00 $"
__copyright__ = "Copyright (c) 2013 Denis J Jackman"
__license__ = "Python"


def encryptScytal(code, columns=5, debug=False):
    '''
        encryptScytal
    '''
    result = ""
    result = code.replace(' ', '')
    result = result.lower()
    d = []
    loop = 0
    aloop = 0

    while loop <= columns:
        a = ""
        d.append(a)
        loop += 1
    loop = 0
    while loop < len(result):
        while aloop < columns:
            d[aloop] += result[loop]
            aloop += 1
            loop += 1
            if loop >= len(result):
                aloop = 10
        aloop = 0
    loop = 0
    a = ""
    while loop <= columns:
        a += d[loop]
        loop += 1
    result = a
    if debug is True:
        print("debug mode")

    return result


def decryptScytal(code, columns=5, debug=False):
    '''
        decrypt Scytal
    '''
    result = ""
    print(code)
    b = len(code) / columns
    c = len(code) / columns
    e = len(code) % columns
    print(b, c, e)
    if e > 0:
        b += 1
    else:
        oldcode = code
        code = code[:-(len(code) % columns)]
        print(oldcode)
    print(code)
    d = []
    loop = 0
    while loop <= b:
        a = ""
        d.append(a)
        loop += 1
    loop = 0
    aloop = 0
    while loop < len(code):
        while aloop < b:
            d[aloop] += code[loop]
            print(aloop, loop, d[aloop], code[loop])
            aloop += 1
            loop += 1

            if loop >= len(code):
                aloop = 9999
        aloop = 0
    loop = 0
    a = ""
    while loop <= c:
        a += d[loop]
        loop += 1
    result = a
    if debug is True:
        print("debug mode")
    return result


def encryptCaesar(code, offset=5, debug=False):
    '''
        encrypt the code
    '''
    result = ""
    core = []
    core.append("abcdefghijklmnopqrstuvwxyz")
    core.append("bcdefghijklmnopqrstuvwxyza")
    core.append("cdefghijklmnopqrstuvwxyzab")
    core.append("defghijklmnopqrstuvwxyzabc")
    core.append("efghijklmnopqrstuvwxyzabcd")
    core.append("fghijklmnopqrstuvwxyzabcde")
    core.append("ghijklmnopqrstuvwxyzabcdef")
    core.append("hijklmnopqrstuvwxyzabcdefg")
    core.append("ijklmnopqrstuvwxyzabcdefgh")
    core.append("jklmnopqrstuvwxyzabcdefghi")
    core.append("klmnopqrstuvwxyzabcdefghij")
    core.append("mnopqrstuvwxyzabcdefghijkl")
    core.append("nopqrstuvwxyzabcdefghijklm")
    core.append("opqrstuvwxyzabcdefghijklmn")
    core.append("pqrstuvwxyzabcdefghijklmno")
    core.append("qrstuvwxyzabcdefghijklmnop")
    core.append("rstuvwxyzabcdefghijklmnopq")
    core.append("stuvwxyzabcdefghijklmnopqr")
    core.append("tuvwxyzabcdefghijklmnopqrs")
    core.append("uvwxyzabcdefghijklmnopqrst")
    core.append("vwxyzabcdefghijklmnopqrstu")
    core.append("wxyzabcdefghijklmnopqrstuv")
    core.append("xyzabcdefghijklmnopqrstuvw")
    core.append("yzabcdefghijklmnopqrstuvwx")
    core.append("zabcdefghijklmnopqrstuvwxy")
    loop = 0
    store = code.lower()
    offset -= 1
    while loop < len(code):
        seek = core[0].find(store[loop])
        if core[0].find(store[loop]) > -1:
            result += core[offset][seek]
        else:
            result += store[loop]
        loop += 1
    if debug is True:
        print("debug mode")
    return result


def decryptCaesar(code, offset=5, debug=False):
    '''
        decrypt the code
    '''
    result = ""
    core = []
    core.append("abcdefghijklmnopqrstuvwxyz")
    core.append("bcdefghijklmnopqrstuvwxyza")
    core.append("cdefghijklmnopqrstuvwxyzab")
    core.append("defghijklmnopqrstuvwxyzabc")
    core.append("efghijklmnopqrstuvwxyzabcd")
    core.append("fghijklmnopqrstuvwxyzabcde")
    core.append("ghijklmnopqrstuvwxyzabcdef")
    core.append("hijklmnopqrstuvwxyzabcdefg")
    core.append("ijklmnopqrstuvwxyzabcdefgh")
    core.append("jklmnopqrstuvwxyzabcdefghi")
    core.append("klmnopqrstuvwxyzabcdefghij")
    core.append("mnopqrstuvwxyzabcdefghijkl")
    core.append("nopqrstuvwxyzabcdefghijklm")
    core.append("opqrstuvwxyzabcdefghijklmn")
    core.append("pqrstuvwxyzabcdefghijklmno")
    core.append("qrstuvwxyzabcdefghijklmnop")
    core.append("rstuvwxyzabcdefghijklmnopq")
    core.append("stuvwxyzabcdefghijklmnopqr")
    core.append("tuvwxyzabcdefghijklmnopqrs")
    core.append("uvwxyzabcdefghijklmnopqrst")
    core.append("vwxyzabcdefghijklmnopqrstu")
    core.append("wxyzabcdefghijklmnopqrstuv")
    core.append("xyzabcdefghijklmnopqrstuvw")
    core.append("yzabcdefghijklmnopqrstuvwx")
    core.append("zabcdefghijklmnopqrstuvwxy")
    loop = 0
    store = code.lower()
    offset -= 1
    while loop < len(code):
        seek = core[offset].find(store[loop])
        if core[offset].find(store[loop]) > -1:
            result += core[0][seek]
        else:
            result += store[loop]
        loop += 1
    if debug is True:
        print("debug mode")
    return result


def bruteCaesar(code):
    '''
        brute force caesar
    '''
    loop = 0
    result = ''
    while loop <= 23:
        result = decryptCaesar(code, loop)
        print(f'{loop+1} {decryptCaesar(code, loop)} ')
        code = result
        loop += 1
    return result


if __name__ == '__main__':
    ENCODE = "Denis was here and here and here "\
             "coding happily and working away "\
             "thinking about a makeup selfie"

    bruteCaesar(encryptCaesar("Denis was here!", 12))
