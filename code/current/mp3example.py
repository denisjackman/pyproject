'''
    mp3 python script
'''


def mp3format(t):
    '''
        mp3format(t)
    '''
    num = t
    d = t % 10
    num = t - d
    c = num
    a = 0
    b = 0
    if c > 600:
        num = c
        c = num % 600
        a = (num - c) / 600
    c = c / 10
    if len(str(c)) == 1:
        b = 0
    else:
        b = ""
    result = f"{str(a)}:{str(b)}{str(c)}.{str(d)}"
    return result


print(f"{mp3format(0)} = 0:00.0")
print(f"{mp3format(11)} = 0:01.1 ")
print(f"{mp3format(321)} = 0:32.1 ")
print(f"{mp3format(613)} = 1:01.3 ")
print(f"{mp3format(6613)} = 11:01.3 ")
