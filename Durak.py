import enum
import sys



class SUIT(enum.Enum):
    HEART = 0
    SPADE = 1
    DIAMOND = 2
    CLUB = 3


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



class Card:
    def __init__(self, suit, value):
        if suit not in SUIT:
            raise ValueError("Recieved Suit not in SUIT, Suit=" + str(suit))

        if value not in VALUE:
            raise ValueError("Recieved Value not in VALUE, Value=" + str(value))

        self.Suit = suit
        self.Value = value











