'''
    this is a test of the card function
'''
import random

def create_deck():
    '''
        this is the deck function
    '''
    mydeck = []
    for mysuit in range(4):
        for myrank in range(1, 14):
            mycard = (mysuit, myrank)
            mydeck.append(mycard)
    random.shuffle(mydeck)
    return mydeck

def main():
    '''
        this is the main function
    '''
    deck = create_deck()
    print(deck)
    print(len(deck))
    rank = ''
    suit = ''
    count = 0
    for card in deck:
        count += 1
        if card[1] == 1:
            rank = "Ace of "
        if card[1] == 11:
            rank = "Jack of "
        if card[1] == 12:
            rank = "Queen of "
        if card[1] == 13:
            rank = "King of "
        if card[1] < 11 and card[1] > 1:
            rank = str(card[1]) + " of "
        if card[0] == 0:
            suit = "Clubs"
        if card[0] == 1:
            suit = "Diamonds"
        if card[0] == 2:
            suit = "Hearts"
        if card[0] == 3:
            suit = "Spades"
        print(f"{count} card : {rank} {suit}")
    print(count)
if __name__ == "__main__":
    main()
