'''
    colour converter routine
'''

with open('Z:/resources/sample-data/colours.csv',
          encoding='utf-8-sig') as input_file, \
     open('Z:/Store/target/rgb.py',
          'w',
          encoding='utf-8-sig') as rgb_file, \
     open('Z:/Store/target/hex.py',
          'w',
          encoding='utf-8-sig') as hex_file, \
     open('Z:/Store/target/rgbdict.py',
          'w',
          encoding='utf-8-sig') as rgbdict_file, \
     open('Z:/Store/target/hexdict.py',
          'w',
          encoding='utf-8-sig') as hexdict_file:

    rgb_file.write("'''\n RGB COLOR CODES\n'''\n")
    hex_file.write("'''\n HEX COLOR CODES\n'''\n")
    rgbdict_file.write("'''\n Dictionary RGB COLOR CODES\n'''\n")
    hexdict_file.write("'''\n Dictionary HEX COLOR CODES\n'''\n")
    rgbdict_file.write("COLOURS_RGB_LIST = {")
    hexdict_file.write("COLOURS_HEX_LIST = {")
    FIRST_TIME = True
    for item in input_file.readlines():
        item = item.strip()
        new_item = item.split(',')
        name = new_item[0].upper()
        nametable = name.maketrans(' ', '_')
        newname = name.translate(nametable)
        colorrgb = new_item[1].split('-')
        outputrgb = (colorrgb[0], colorrgb[1], colorrgb[2])
        colorhex = ('0x'+new_item[2][:2].upper(),
                    '0x'+new_item[2][2:4].upper(),
                    '0x'+new_item[2][4:].upper())
        rgb_file.write(f"{newname} = {outputrgb}\n")
        hex_file.write(f"{newname} = {colorhex}\n")
        if FIRST_TIME:
            rgbdict_file.write(f'"{newname}" : {outputrgb}')
            hexdict_file.write(f'"{newname}" : {colorhex}')
            FIRST_TIME = False
        else:
            rgbdict_file.write(f',\n"{newname}" : {outputrgb}')
            hexdict_file.write(f',\n"{newname}" : {colorhex}')

    rgbdict_file.write("}\n")
    hexdict_file.write("}\n")
