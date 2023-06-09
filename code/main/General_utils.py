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

from PIL import Image, ImageFilter
from djgamemodule import dice as Dice
from djgamemodule import constants as StaticItems

# Main loops
if __name__ == "__main__":
    LOOP = 0
    while LOOP < 101:
        print("Die Rolls                   : " + str(LOOP) + " : "+  str(Dice.dice()) + " : " + str(Dice.number_generator(100)))
        LOOP = LOOP +1
    print("Dice roll one six sided     : " + str(Dice.dice()))
    print("Dice roll one hundred sided : " + str(Dice.dice(100)))
    print("Dice roll five six sided    : " + str(Dice.dice(rolls=5)))
    print("Dice roll ten four sided    : " + str(Dice.dice(4,10)))
    print("Insults                     : " + Dice.insult_generator())
    print("Insults                     : " + Dice.insult_generator())
    print("Direction is                : " + StaticItems.DIRECTIONS[Dice.number_generator(4)-1])
    print("Phonetic Alpha (J)          : " + StaticItems.PHONETIC_ALPHABET["j"])
    ISBN="1-58488-540-8"
    print("ISBN                        : " + ISBN)
    ISBN="978-158488-540-5"
    print("ISBN                        : " + ISBN)

    print("SYS                         : " + str(Dice.insult_generator()))
    #open a file and read it in stripping the newline out of it
    with open("Y:/Resources/text/shipnames.txt", "r", encoding='utf-8-sig') as shipfile:
        shiplines = shipfile.read().strip()
        print(f"Shipname                    : {shiplines[Dice.number_generator(len(shiplines)-1)]}")
        print(f"Shipname                    : {str(len(shiplines))}")

    size = (128, 128)
    SAVED = "y:/Resources/images/lenna.jpeg"
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
    except FileNotFoundError as err:
        print(f"Unable to load image : lenna.jpg with {err}")
    print("The size of the Image is: ")
    print(original.format, original.size, original.mode)
    im.thumbnail(size)
    im.save(SAVED)
    im.show()
