"""
weight.py
    This convert weight measure to and from weight units.
    it uses the basis that
    1 pound = 10 weight unit
    1 kilo = 20 Weight units (this is approx)
    This will allow us to store an items weight as WU in the game data.

"""


def pound_to_wu(amount):
    '''
        pound to weight unit
    '''
    result = amount * 10
    return result


def kilo_to_wu(amount):
    '''
        kilo to weight unit
    '''
    result = amount * 20
    return result


def ounce_to_wu(amount):
    '''
        ounce to weight unit
    '''
    result = amount * (10.0/16.0)
    return result


def gram_to_wu(amount):
    '''
        grams to weight unit (wu)
    '''
    result = amount * (20.0 / 1000)
    return result


def wu_to_pound(amount):
    '''
        weight unit to pounds
    '''

    result = amount / 10
    return result


def wu_to_kilo(amount):
    '''
        weight unit to kilo
    '''

    result = amount / 20
    return result


def wu_to_ounce(amount):
    '''
        weight unit to ounce
    '''

    result = amount / (10*16)
    return result


def wu_to_gram(amount):
    '''
        weight unit to grams
    '''
    result = amount / (20*1000)
    return result


if __name__ == '__main__':
    print("This is a test for the weight function")
    print("Test 1: 1 pound = "
          f"{str(pound_to_wu(1))} Weight units = "
          f"{str(wu_to_kilo(pound_to_wu(1.0)))} Kilos")
    print("Test 2: 1 kilo = "
          f"{str(kilo_to_wu(1))} Weight units = "
          f"{str(wu_to_pound(kilo_to_wu(1.0)))} pounds")
    print("Test 3: 16 oz = "
          f"{str(ounce_to_wu(16.0))} Weight units = "
          f"{str(wu_to_pound(ounce_to_wu(16)))} pounds")
    print("Test 4: 1000g = "
          f"{str(gram_to_wu(1000.0))} Weight units = "
          f"{str(wu_to_kilo(gram_to_wu(1000)))} kilos")
