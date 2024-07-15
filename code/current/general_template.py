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

import platform
from PIL import Image, ImageFilter

from djgamemodule import dice as Dice
from djgamemodule import constants as StaticItems

if platform.system() == "Windows":
    SAVED = "Z:/Resources/images/lenna.jpeg"
    SHIPNAMES = "Z:/Resources/text/shipnames.txt"
    BLURRED = "Z:/Resources/images/lenna_blurred.jpeg"
else:
    SAVED = "/mnt/y/Resources/images/lenna.jpeg"
    SHIPNAMES = "/mnt/y/Resources/text/shipnames.txt"
    BLURRED = "/mnt/y/Resources/images/lenna_blurred.jpeg"
# Main loops
if __name__ == "__main__":
    LOOP = 0
    while LOOP < 101:
        print("Die Rolls                   : "
              f"{str(LOOP)} : "
              f"{str(Dice.dice())} : "
              f"{str(Dice.number_generator(100))}")
        LOOP = LOOP + 1
    print(f"Dice roll one six sided     : {str(Dice.dice())}")
    print(f"Dice roll one hundred sided : {str(Dice.dice(100))}")
    print(f"Dice roll five six sided    : {str(Dice.dice(rolls=5))}")
    print(f"Dice roll ten four sided    : {str(Dice.dice(4, 10))}")
    print(f"Insults                     : {Dice.insult_generator()}")
    print(f"Insults                     : {Dice.insult_generator()}")
    print("Direction is                : "
          f"{StaticItems.DIRECTIONS[Dice.number_generator(4)-1]}")
    print('Phonetic Alpha (J)          : '
          f'{StaticItems.PHONETIC_ALPHABET["j"]}')
    ISBN = "1-58488-540-8"
    print(f"ISBN                        : {ISBN}")
    ISBN = "978-158488-540-5"
    print(f"ISBN                        : {ISBN}")

    print(f"SYS                         : {str(Dice.insult_generator())}")
    # open a file and read it in stripping the newline out of it
    with open(SHIPNAMES,
              "r",
              encoding='utf-8-sig') as shipfile:
        shiplines = shipfile.read().strip()
        print("Shipname                    : "
              f"{shiplines[Dice.number_generator(len(shiplines)-1)]}")
        print(f"Shipname                    : {str(len(shiplines))}")

    size = (128, 128)

    try:
        with Image.open(SAVED) as original:
            original.load()
        # Blur the image
        blurred = original.filter(ImageFilter.BLUR)

        # Display both images
        original.show()
        blurred.show()

        # save the new image
        blurred.save(BLURRED)
        im = Image.open(SAVED)
    except FileNotFoundError as err:
        print(f"Unable to load image : lenna.jpg with {err}")
    print("The size of the Image is: ")
    print(original.format, original.size, original.mode)
    im.thumbnail(size)
    im.save(SAVED)
    im.show()
