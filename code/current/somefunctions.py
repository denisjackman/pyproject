''' some example functions '''


def censor(text, word):
    '''Censor the word in the text'''
    ban = "*" * len(word)
    result = []
    temp = text.split(" ")
    for item in temp:
        if item == word:
            result.append(ban)
        else:
            result.append(item)
    return ' '.join(result)


def print_spam():
    '''Print spam'''
    print("spam")


def print_twice(arg):
    ''' Print twice'''
    print(arg)


def do_twice(f, arg):
    ''' Do twice'''
    f(arg)
    f(arg)


def do_four(f, arg):
    ''' Do four'''
    do_twice(f, arg)
    do_twice(f, arg)


doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
cubes_by_four = [x ** 3 for x in range(1, 11) if (x ** 3) % 4 == 0]


def grid():
    ''' Grid'''
    for y in range(1, 13):
        if y in (1, 6, 12):
            for dx in range(1, 13):
                if dx in (1, 6, 12):
                    print('+',)
                else:
                    print('-',)
            print("")
        else:
            for dx in range(1, 13):
                if dx in (1, 6, 12):
                    print('|',)
                else:
                    print(' ',)
            print("")


def grid4():
    ''' Grid4'''
    for y in range(1, 25):
        if y in (1, 6, 12, 18, 24):
            for dx in range(1, 25):
                if dx in (1, 6, 12, 18, 24):
                    print('+',)
                else:
                    print('-',)
            print("")
        else:
            for dx in range(1, 25):
                if dx in (1, 6, 12, 18, 24):
                    print('|',)
                else:
                    print(' ',)
            print("")


l = [i ** 2 for i in range(1, 11)]
my_list = range(1, 11)
# List of numbers 1 - 10
backwards = my_list[::-1]

to_21 = range(1, 22)
odds = to_21[::2]
middle_third = to_21[7:14]
print(to_21)
print(odds)
print(middle_third)

my_list = range(16)
print(filter(lambda ax: ax % 3 == 0, my_list))

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print(filter(lambda bx: bx == 'Python', languages))

squares = [x ** 2 for x in range(1, 11)]
print(squares)
print(filter(lambda sx: 30 < sx < 70, squares))

threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]
print(threes_and_fives)

GARBLED = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
UNGARBLED = GARBLED[::-2]
print(GARBLED)
print(UNGARBLED)

GARBLED = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt "\
          "mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda wx: wx.replace('X', ''), GARBLED)
print(f"MSG: {message}")

print("---------------------------------------------------------------------")
print(5 >> 4)
print(5 << 1)
print(8 & 5)
print(9 | 4)
print(12 ^ 42)
print(~88)
print("---------------------------------------------------------------------")
print(0b1,)
print(0b10,)
print(0b11,)
print(0b100,)
print(0b101,)
print(0b110,)
print(0b111)
print("******")
print(0b1 + 0b11)
print(0b11 * 0b11)
print("---------------------------------------------------------------------")


def flip_bit(number, n):
    ''' Flip bit'''''
    mask = 0b1 << (n-1)
    result = number ^ mask
    return bin(result)


print(flip_bit(0b111, 2))
