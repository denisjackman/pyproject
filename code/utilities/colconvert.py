#!/usr/bin/python
'''
    colour converter routine
'''
rgb_file = open('rgb.py', 'w', encoding='utf8')
hex_file = open('hex.py', 'w', encoding='utf8')
rgbdict_file = open('rgbdict.py', 'w', encoding='utf8')
hexdict_file = open('hexdict.py', 'w', encoding='utf8')
rgbdict_file.write("COLOURS_HEX_LIST = {")
hexdict_file.write("COLOURS_HEX_LIST = {")

with open('y:/resources/colours.csv', encoding="utf8") as input_file:
    for item in input_file.readlines():
        item = item.strip()
        new_item = item.split(',')
        name = new_item[0].upper()
        nametable = name.maketrans(' ','_')
        newname = name.translate(nametable)
        colorrgb = new_item[1].split('-')
        outputrgb = (colorrgb[0], colorrgb[1], colorrgb[2])
        colorhex = ('0x'+new_item[2][:2].upper(),
                    '0x'+new_item[2][2:4].upper(),
                    '0x'+new_item[2][4:].upper())
        rgb_file.write(f"{newname} =  {outputrgb}\n")
        hex_file.write(f"{newname} = {colorhex}\n")
        rgbdict_file.write(f',\n"{newname}" : {outputrgb}')
        hexdict_file.write(f',\n"{newname}" : {colorhex}')
rgbdict_file.write("}\n")
hexdict_file.write("}\n")
input_file.close()
rgb_file.close()
hex_file.close()
