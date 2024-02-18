#!/usr/bin/env python
"""
Code for messing with ISBN numbers. Stuff for validating ISBN-10 and
ISBN-13 numbers, computing check digits and converting from one format
to the other.

This code doesn't know anything about proper hyphenation of ISBNs. Nor does
it know anything about the real "validity" of ISBNs - it just validates on
the basis of the check-digit.

Some examples:

>>> import isbn
>>> isbn.isValid("1-58488-540-8")
True
>>> isbn.isValid("1-58488-540-5")
False
>>> isbn.isValid("978-158488-540-5")
True
>>> isbn.isI10("978-158488-540-5")
False
>>> isbn.isI13("978-158488-540-5")
True
>>> isbn.convert("1-58488-540-8")
'9781584885405'
>>> isbn.convert("978-158488-540-5")
'1584885408'
>>> isbn.IsbnStrip("978-158488-540-5")
'9781584885405'
>>> isbn.check("1-58488-540")
'8'
>>> isbn.toI13("1-58488-540-8")
'9781584885405'
>>> isbn.toI13("978-158488-540-5")
'9781584885405'
>>> isbn.url("amazon","978-158488-540-5")
'http://www.amazon.com/exec/obidos/ASIN/1584885408'


The code is very simple pure python code in a single source file. Please
read the source code file (isbn.py) for further information about how
it works.

Please send bug reports, bug fixes, etc. to:
darrenjwilkinson@btinternet.com
Free GPL code, Copyright (C) 2007 Darren J Wilkinson
http://www.staff.ncl.ac.uk/d.j.wilkinson/
# isbn.py
# Code for messing with ISBN numbers
# Especially stuff for converting between ISBN-10 and ISBN-13
# Copyright (C) 2007 Darren J Wilkinson
# Free GPL code
# Last updated: 14/8/2007
"""
import re


def IsbnStrip(isbn):
    """
    Strip whitespace, hyphens, etc. from an ISBN number and return
    the result.
    """
    short = re.sub(r"\W", "", isbn)
    return re.sub(r"\D", "X", short)


def convert(isbn):
    """
    Convert an ISBN-10 to ISBN-13 or vice-versa.
    """
    short = IsbnStrip(isbn)
    if isValid(short) is False:
        raise TypeError("Invalid ISBN")
    if len(short) == 10:
        stem = f"978{short[:-1]}"
        return f"{stem}{check(stem)}"
    if short[:3] == "978":
        stem = short[3:-1]
        return f"{stem}{check(stem)}"
    raise TypeError("ISBN not convertible")


def isValid(isbn):
    """
    Check the validity of an ISBN. Works for either ISBN-10 or ISBN-13.
    """
    short = IsbnStrip(isbn)
    if len(short) == 10:
        return isI10(short)
    if len(short) == 13:
        return isI13(short)
    return False


def check(stem):
    """
    Compute the check digit for the stem of an ISBN. Works with either
    the first 9 digits of an ISBN-10 or the first 12 digits of an ISBN-13.
    """
    short = IsbnStrip(stem)
    if len(short) == 9:
        return checkI10(short)
    if len(short) == 12:
        return checkI13(short)
    return False


def checkI10(stem):
    """
    Computes the ISBN-10 check digit based on the first 9 digits of
    a stripped ISBN-10 number.
    """
    chars = list(stem)
    checksum = 0
    digit = 10
    for char in chars:
        checksum += digit*int(char)
        digit -= 1
    I10check = 11-(checksum % 11)
    if I10check == 10:
        return "X"
    if I10check == 11:
        return "0"
    return str(I10check)


def isI10(isbn):
    """
    Checks the validity of an ISBN-10 number.
    """
    short = IsbnStrip(isbn)
    if len(short) != 10:
        return False
    chars = list(short)
    checksum = 0
    digit = 10
    for char in chars:
        if char in ('X', 'x'):
            char = "10"
        checksum += digit*int(char)
        digit -= 1
    remainder = checksum % 11
    if remainder == 0:
        return True
    return False


def checkI13(stem):
    """
    Compute the ISBN-13 check digit based on the first 12 digits of a
    stripped ISBN-13 number.
    """
    chars = list(stem)
    checksum = 0
    count = 0
    for char in chars:
        if count % 2 == 0:
            checksum += int(char)
        else:
            checksum += 3*int(char)
        count += 1
    I13check = 10 - (checksum % 10)
    if I13check == 10:
        return "0"
    return str(I13check)


def isI13(isbn):
    """
    Checks the validity of an ISBN-13 number.
    """
    short = IsbnStrip(isbn)
    if len(short) != 13:
        return False
    chars = list(short)
    checksum = 0
    count = 0
    for char in chars:
        if count % 2 == 0:
            checksum += int(char)
        else:
            checksum += 3*int(char)
        count += 1
    remainder = checksum % 10
    return bool(remainder == 0)


def toI10(isbn):
    """
    Converts supplied ISBN (either ISBN-10 or ISBN-13) to a stripped ISBN-10.
    """
    if isValid(isbn) is False:
        raise TypeError("Invalid ISBN")
    if isI10(isbn):
        return IsbnStrip(isbn)
    return convert(isbn)


def toI13(isbn):
    """
    Converts supplied ISBN (either ISBN-10 or ISBN-13) to a stripped ISBN-13.
    """
    if isValid(isbn) is False:
        raise TypeError("Invalid ISBN")
    if isI13(isbn):
        return IsbnStrip(isbn)
    return convert(isbn)


def url(isbntype, isbn):
    """
    Returns a URL for a book, corresponding to the "type" and the "isbn"
    provided. This function is likely to go out-of-date quickly, and is
    provided mainly as an example of a potential use-case for the
    module. Currently allowed types are "google-books" (the default if
    the type is not recognised), "amazon", "amazon-uk", "blackwells".
    """
    short = toI10(isbn)
    if isbntype == "amazon":
        return f"http://www.amazon.com/o/ASIN/{short}"
    if isbntype == "amazon-uk":
        return f"http://www.amazon.co.uk/o/ASIN/{short}"
    if isbntype == "blackwells":
        return "http://bookshop.blackwell.co.uk/jsp/welcome"\
               f".jsp?action=search&type=isbn&term={short}"
    return f"http://books.google.com/books?vid={short}"
