import enum
import sys
import random
import pygame

class SUIT(enum.Enum):
    HEART = 0
    SPADE = 1
    DIAMOND = 2
    CLUB = 3
SuitStrings = {
    SUIT.HEART:   'hearts',
    SUIT.SPADE:   'spades',
    SUIT.DIAMOND: 'diamonds',
    SUIT.CLUB:    'clubs',
}

class VALUE(enum.Enum):
    TWO = 0
    THREE = 1
    FOUR = 2
    FIVE = 3
    SIX = 4
    SEVEN = 5
    EIGHT = 6
    NINE = 7
    TEN = 8
    JACK = 9
    QUEEN = 10
    KING = 11
    ACE = 12

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __le__(self, other):
        return self.value <= other.value

ValueStrings = {
    VALUE.TWO:   '2',
    VALUE.THREE: '3',
    VALUE.FOUR:  '4',
    VALUE.FIVE:  '5',
    VALUE.SIX:   '6',
    VALUE.SEVEN: '7',
    VALUE.EIGHT: '8',
    VALUE.NINE:  '9',
    VALUE.TEN:   '10',
    VALUE.JACK:  'jack',
    VALUE.QUEEN: 'queen',
    VALUE.KING:  'king',
    VALUE.ACE:   'ace'
}

class Card:
    def __init__(self, suit, value, image=None):
        if suit not in SUIT:
            raise ValueError("Recieved Suit not in SUIT, Suit=" + str(suit))

        if value not in VALUE:
            raise ValueError("Recieved Value not in VALUE, Value=" + str(value))

        self.Suit = suit
        self.Value = value
        self.Image = image

class Deck:
    def __init__(self, full=True, shuffle=False):
        self.cards = []
        for suit in SUIT:
            for val in VALUE:
                if full or val >= VALUE.SIX:
                    image = pygame.image.load("Cards/" + ValueStrings[val] + 
                        "_of_" + SuitStrings[suit] + ".png")
                    self.cards.append(Card(suit, val, image))
        if shuffle:
            self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def pop(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        return None

    def draw(self, numCards=1):
        return [self.pop() for _ in range(min(numCards, len(self.cards)))]












