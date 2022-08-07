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

# Custom import items
# Functions
# FIXME: this is a Fix Tag
# TODO: this is todo tag
# IDEA: This is an idea tag
# CONCEPT: this is a concept tag

from djgamemodule import dice as Dice
from djgamemodule import constants as StaticItems
#import PIL

# Main loops
if __name__ == "__main__":
    loop = 0
    while loop < 101:
        print("Die Rolls                   : " + str(loop) + " : "+  str(Dice.dice()) + " : " + str(Dice.number_generator(100)))
        loop = loop +1
    print("Dice roll one six sided     : " + str(Dice.dice()))
    print("Dice roll one hundred sided : " + str(Dice.dice(100)))
    print("Dice roll five six sided    : " + str(Dice.dice(rolls=5)))
    print("Dice roll ten four sided    : " + str(Dice.dice(4,10)))
    print("Insults                     : " + Dice.insult_generator())
    print("Insults                     : " + Dice.insult_generator())

    # print("Roman Numeral for five (5)  : " + Roman.Int_to_Roman(5))
    # print("Num for Roman Numeral (MM)  : " + str(Roman.Roman_to_Int("MM")))

    print("Direction is                : " + StaticItems.DIRECTIONS[Dice.number_generator(4)-1])
    print("Phonetic Alpha (J)          : " + StaticItems.PHONETIC_ALPHABET["j"])

    isbn="1-58488-540-8"
    # isbn="978-158488-540-5"
    print("ISBN                        : " + isbn)
    # if ISBN.isValid(isbn):
    #    print("ISBN                        : " + "isbn ok")
    # else:
    #    print("ISBN                        : " + "isbn BAD")
    # print("ISBN                        : " + ISBN.convert(isbn))
    isbn="978-158488-540-5"
    print("ISBN                        : " + isbn)
    # if ISBN.isValid(isbn):
    #    print("ISBN                        : " + "isbn ok")
    # else:
    #    print("ISBN                        : " + "isbn BAD")
    #print("ISBN                        : " + ISBN.convert(isbn))

    print("SYS                         : " + str(Dice.insult_generator))
    print("SYS                         : " + str(dir(Dice.insult_generator)))
    print("SYS                         : " + str(callable(Dice.insult_generator)))
    #open a file and read it in stripping the newline out of it
    shiplines = [line.strip() for line in open("Y:/Resources/text/shipnames.txt","r")]
    print("Shipname                    : " + shiplines[Dice.number_generator(len(shiplines)-1)])
    print("Shipname                    : " + str(len(shiplines)))

    size = (128, 128)
    saved = "y:/Resources/images/lenna.jpeg"
    try:
        original = Image.open("Y:/Resources/images/Lenna.png")
        # Blur the image
        blurred = original.filter(ImageFilter.BLUR)

        # Display both images
        original.show()
        blurred.show()

        # save the new image
        blurred.save("Y:/Resources/images/blurred.png")
        im =  Image.open("Y:/Resources/images/Lenna.png")
    except:
        print("Unable to load image")
    print("The size of the Image is: ")
    print(original.format, original.size, original.mode)
    im.thumbnail(size)
    im.save(saved)
    im.show()
