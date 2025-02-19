'''
    solitaire
'''
import random

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
          '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}

# DEBUG mode
DEBUG = False


class Card:
    '''
    # define card class
    '''
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
            self.status = False
        else:
            self.suit = None
            self.rank = None
            self.status = None
            print("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        ''' get the suite '''
        return self.suit

    def get_rank(self):
        ''' get the rank '''
        return self.rank

    def dealt(self):
        ''' have we dealt a hand '''
        return self.status

    def set_dealt(self):
        ''' return the dealt status '''
        self.status = True

    def draw(self, canvas, pos):
        ''' render the stuff '''
        print(canvas, pos)


class Hand:
    ''' define hand class '''
    def __init__(self):
        self.hand = []

    def __str__(self):
        result = "Hand is  : "
        for card in self.hand:
            result += str(card)+":"
        return result

    def __len__(self):
        return len(self.hand)

    def add_card(self, card):
        ''' add a card '''
        self.hand.append(card)

    def get_value(self):
        ''' get the value '''
        ace = False
        value = 0
        for card in self.hand:
            if ace:
                value += VALUES[card.get_rank()]
                if card.get_rank() == "A":
                    if value < 12:
                        value += 10
                else:
                    if value > 21:
                        value -= 10
            else:
                value += VALUES[card.get_rank()]
                if card.get_rank() == "A":
                    if value < 12:
                        value += 10
                    ace = True
        # count aces as 1,
        # if the hand has an ace,
        # then add 10 to hand value
        # if it doesn't bust
        return value

    def draw(self, canvas, pos):
        ''' draw '''
        print(canvas, pos)


class Deck:
    ''' define the Deck class '''
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        ''' shuffle the deck '''
        random.shuffle(self.deck)

    def deal_card(self):
        ''' deal a card '''
        card = random.choice(self.deck)
        while card.dealt():
            card = random.choice(self.deck)
        card.set_dealt()
        return card

    def __str__(self):
        result = " Deck : "
        for card in self.deck:
            result += str(card) + " : "
        return result

    def __len__(self):
        return len(self.deck)


def init():
    ''' initialise the game '''

    game_deck = Deck()
    game_deck.shuffle()

    # foundation_hearts = Hand()
    # foundation_spades = Hand()
    # foundation_clubs = Hand()
    # foundation_diamonds = Hand()

    base1 = Hand()
    base2 = Hand()
    base3 = Hand()
    base4 = Hand()
    base5 = Hand()
    base6 = Hand()
    base7 = Hand()

    pile = Hand()
    waste = Hand()

    card = 0
    while card < len(game_deck):
        if len(base1) < 1:
            base1.add_card(game_deck.deal_card())
        elif len(base2) < 2:
            base2.add_card(game_deck.deal_card())
        elif len(base3) < 3:
            base3.add_card(game_deck.deal_card())
        elif len(base4) < 4:
            base4.add_card(game_deck.deal_card())
        elif len(base5) < 5:
            base5.add_card(game_deck.deal_card())
        elif len(base6) < 6:
            base6.add_card(game_deck.deal_card())
        elif len(base7) < 7:
            base7.add_card(game_deck.deal_card())
        else:
            pile.add_card(game_deck.deal_card())
        card += 1

        print("Base 1: " + str(len(base1))+" : " + str(base1))
        print("Base 2: " + str(len(base2))+" : " + str(base2))
        print("Base 3: " + str(len(base3))+" : " + str(base3))
        print("Base 4: " + str(len(base4))+" : " + str(base4))
        print("Base 5: " + str(len(base5))+" : " + str(base5))
        print("Base 6: " + str(len(base6))+" : " + str(base6))
        print("Base 7: " + str(len(base7))+" : " + str(base7))
        print("Pile  : " + str(len(pile))+" : " + str(pile))
        print("Waste : " + str(len(waste))+" : " + str(waste))


# Main loop for the game
if __name__ == '__main__':
    init()
