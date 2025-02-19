'''
    99 bottles of beer
'''
SUFFIX = ''
for quant in range(99, 0, -1):
    if quant > 1:
        print(f"{quant}"
              "bottles of beer on the wall , "
              f"{quant}"
              " bottles of beer.")
        if quant > 2:
            SUFFIX = str(quant - 1) + " bottles of beer on the wall."
        else:
            SUFFIX = "1 bottle of beer on the wall."
    elif quant == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        SUFFIX = "no more beer on the wall!"


print(f'Take one down, pass it around, {SUFFIX}')
