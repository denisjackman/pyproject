'''
    BJTest
'''
import random

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# DEBUG mode
DEBUG = False

# define card class
class Card:
    '''
        Card Object
    '''
    def __init__(self, bjsuit, bjrank):
        if (bjsuit in SUITS) and (bjrank in RANKS):
            self.suit = bjsuit
            self.rank = bjrank
            self.status = False
        else:
            self.suit = None
            self.rank = None
            self.status = None
            print("Invalid card: {bjsuit} {bjrank}")

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        '''
            get_suit function
        '''
        return self.suit

    def get_rank(self):
        ''' get rank '''
        return self.rank

    def dealt(self):
        ''' is the hand dealt '''
        return self.status

    def set_dealt(self):
        '''
            set the hand to dealt
        '''
        self.status = True

    def draw(self, canvas, pos):
        '''
            draw a card
        '''
        print(canvas, pos)

class Hand:
    '''
        hand object
    '''
    def __init__(self):
        self.hand=[]

    def __str__(self):
        result = "Hand is  : "
        for card in self.hand:
            result += str(card)+":"
        return result

    def __len__(self):
        return len(self.hand)


    def add_card(self, card):
        '''
            add a card
        '''
        self.hand.append(card)

    def get_value(self):
        '''
            get the card value
        '''
        ace = False
        value=0
        for bjcard in self.hand:
            if ace:
                value += VALUES[bjcard.get_rank()]
                if bjcard.get_rank() == "A":
                    if value < 12:
                        value += 10
                else:
                    if value > 21:
                        value -= 10
            else:
                value += VALUES[bjcard.get_rank()]
                if bjcard.get_rank() == "A":
                    if value < 12:
                        value += 10
                    ace = True
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        return value

    def draw(self, canvas, pos):
        '''
            draw the card
        '''
        print(canvas, pos)

class Deck:
    '''
        deck object
    '''
    def __init__(self):
        self.bjdeck=[]
        for suit in SUITS:
            for rank in RANKS:
                self.bjdeck.append(Card(suit,rank))

    def shuffle(self):
        '''
            shuffle the deck
        '''
        random.shuffle(self.bjdeck)

    def deal_card(self):
        '''
            deal a card
        '''
        card = random.choice(self.bjdeck)
        while card.dealt():
            card = random.choice(self.bjdeck)
        card.set_dealt()
        return card

    def __str__(self):
        result = " Deck : "
        for card in self.bjdeck:
            result += str(card) + " : "
        return result

    def __len__(self):
        return len(self.bjdeck)


# initialise the game
def init():
    '''
        initialise the game
    '''
    GAME_DECK = Deck()
    GAME_DECK.shuffle()

    FOUNDATION_HEARTS = Hand()
    FOUNDATION_SPADES = Hand()
    FOUNDATION_CLUBS = Hand()
    FOUNDATION_DIAMONDS = Hand()

    BASE1= Hand()
    BASE2= Hand()
    BASE3= Hand()
    BASE4= Hand()
    BASE5= Hand()
    BASE6 = Hand()
    BASE7 = Hand()

    PILE = Hand()
    WASTE = Hand()

    card=0
    while card < len(GAME_DECK):
        if len(BASE1) < 1:
            BASE1.add_card(GAME_DECK.deal_card())
        elif len(BASE2) < 2:
            BASE2.add_card(GAME_DECK.deal_card())
        elif len(BASE3) < 3:
            BASE3.add_card(GAME_DECK.deal_card())
        elif len(BASE4) < 4:
            BASE4.add_card(GAME_DECK.deal_card())
        elif len(BASE5) < 5:
            BASE5.add_card(GAME_DECK.deal_card())
        elif len(BASE6) < 6:
            BASE6.add_card(GAME_DECK.deal_card())
        elif len(BASE7) < 7:
            BASE7.add_card(GAME_DECK.deal_card())
        else:
            PILE.add_card(GAME_DECK.deal_card())
        card += 1
        print(f"Base 1: {str(len(BASE1))} : {str(BASE1)}")
        print(f"Base 2: {str(len(BASE2))} : {str(BASE2)}")
        print(f"Base 3: {str(len(BASE3))} : {str(BASE3)}")
        print(f"Base 4: {str(len(BASE4))} : {str(BASE4)}")
        print(f"Base 5: {str(len(BASE5))} : {str(BASE5)}")
        print(f"Base 6: {str(len(BASE6))} : {str(BASE6)}")
        print(f"Base 7: {str(len(BASE7))} : {str(BASE7)}")
        print(f"Pile  : {str(len(PILE))} : {str(PILE)}")
        print(f"Waste : {str(len(WASTE))} : {str(WASTE)}")

if __name__ == '__main__':
    init()
