'''
    this is a test of the card function
'''
import random

def deck():
    '''
        this is the deck function
    '''
    playdeck = []
    for suit in range(4):
        for rank in range(1, 14):
            card = (suit, rank)
            playdeck.append(card)
    random.shuffle(playdeck)
    return playdeck

def main():
    '''
        this is the main function
    '''
    mydeck = deck()
    print(mydeck)
    print(len(mydeck))

if __name__ == "__main__":
    main()
