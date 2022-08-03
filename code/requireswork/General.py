#!/usr/bin/python
"""
General.py

This program is a template for python programs

All this stuff at the top of the script is just optional metadata;
the real code starts on the "if __name__" line
"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.1 $"
__date__ = "$Date: 2013/12/04 17:17:00 $"
__copyright__ = "Copyright (c) 2013 Denis J Jackman"
__license__ = "Python"

# System imports
import sys
from PIL import Image, ImageFilter
sys.path.append('./Functions')

# Custom import items
# Functions
#FIXME: this is a Fix Tag
#TODO: this is todo tag
#IDEA: This is an idea tag
#CONCEPT: this is a concept tag

import Dice
import Roman
import InsultGenerator
import StaticItems
import ISBN
#import PIL

# Main loops
if __name__ == "__main__":
    loop = 0
    try:
        while loop < 101:
            print("Die Rolls                   : " + str(loop) + " : "+  str(Dice.Dice()) + " : " + str(Dice.NumGen(100)))
            loop = loop +1
        print("Dice roll one six sided     : " + str(Dice.Dice()))
        print("Dice roll one hundred sided : " + str(Dice.Dice(100)))
        print("Dice roll five six sided    : " + str(Dice.Dice(rolls=5)))
        print("Dice roll ten four sided    : " + str(Dice.Dice(4,10)))
    except:
        print("OOPS: Dice ")
    try:
        print("Insults                     : " + InsultGenerator.InsultGenerator())
        print("Insults                     : " + InsultGenerator.InsultGenerator())
    except:
        print("OOPS: InsultGenerator")
    try:
        print("Roman Numeral for five (5)  : " + Roman.Int_to_Roman(5))
        print("Num for Roman Numeral (MM)  : " + str(Roman.Roman_to_Int("MM")))
    except:
        print("OOPS: Roman ")
    try:
        print("Direction is                : " + StaticItems.DIRECTIONS[Dice.NumGen(4)-1])
        print("Phonetic Alpha (J)          : " + StaticItems.PHONETIC_ALPHABET["j"])
    except:
        print("OOPS: StaticItems")
    try:
        isbn="1-58488-540-8"
        # isbn="978-158488-540-5"
        print("ISBN                        : " + isbn)
        if ISBN.isValid(isbn):
            print("ISBN                        : " + "isbn ok")
        else:
            print("ISBN                        : " + "isbn BAD")
        print("ISBN                        : " + ISBN.convert(isbn))
        isbn="978-158488-540-5"
        print("ISBN                        : " + isbn)
        if ISBN.isValid(isbn):
            print("ISBN                        : " + "isbn ok")
        else:
            print("ISBN                        : " + "isbn BAD")
        print("ISBN                        : " + ISBN.convert(isbn))
    except:
        print("OOPS: ISBN")
    try:
        print("SYS                         : " + str(InsultGenerator.InsultGenerator))
        print("SYS                         : " + str(dir(InsultGenerator.InsultGenerator)))
        print("SYS                         : " + str(callable(InsultGenerator.InsultGenerator)))
    except:
        print("OOPS: SYS Calls")
    try:
        #open a file and read it in stripping the newline out of it
        shiplines = [line.strip() for line in open("Resources/shipnames.txt","r")]
        print("Shipname                    : " + shiplines[Dice.NumGen(len(shiplines)-1)])
        print("Shipname                    : " + str(len(shiplines)))
    except:
        print("OOPS: File failure - shipnames.txt")
    size = (128, 128)
    saved = "Resources/lenna.jpeg"
    try:
        original = Image.open("Resources/Lenna.png")
        # Blur the image
        blurred = original.filter(ImageFilter.BLUR)

        # Display both images
        original.show()
        blurred.show()

        # save the new image
        blurred.save("Resources/blurred.png")
        im =  Image.open("Resources/Lenna.png")
    except:
        print("Unable to load image")
    print("The size of the Image is: ")
    print(original.format, original.size, original.mode)
    im.thumbnail(size)
    im.save(saved)
    im.show()
