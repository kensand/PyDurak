import sys
import pygame
import Durak


def createHand(width, height, images):
    ret = pygame.Surface((width, height))
    count = 0
    for card in images:
        rect = card.get_rect()
        rect.inflate_ip(height/rect.height, height/rect.height);
        rect.move_ip(rect.left * -1 + count * (width / len(images)), rect.top * -1)
        ret.blit(card, rect)
    return ret

        
cardImages = {}
for suit in Durak.SUIT:
    for val in Durak.VALUE:
        if (suit, val) not in cardImages:
            cardImages[(suit, val)] = pygame.image.load("Cards/" + Durak.ValueStrings[val] + "_of_" + Durak.SuitStrings[suit] + ".png")

pygame.init()


size = width, height = 1440, 900
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

cards = list(cardImages.values())
hand = createHand(width, height, cards[:10])


    


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    screen.blit(hand, hand.get_rect())
    pygame.display.flip()
