import sys

WindowLocX = 0
WindowLocY = 0
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (WindowLocX, WindowLocY)

import pygame
import Durak




def createHand(width, height, images):
    ret = pygame.Surface((width, height))
    count = 0
    for card in images:
        rect = card.get_rect()
        offset = 0
        if(len(images) > 1):
            offset = (width - rect.width) / (len(images) - 1)
        rect.inflate_ip(height/rect.height, height/rect.height);
        rect.move_ip(rect.left * -1 + count * offset, rect.top * -1)
        ret.blit(pygame.transform.scale(card, (rect.width, rect.height)), rect)
        count += 1
    return ret

def createField(width, height, images):

    ret = pygame.Surface((width, height))
    if len(images) > 6:
        print("Error, more cards than should be in a field")
        return ret
    count = 0
    for card in images:
        rect = card.get_rect()
        scale = width / rect.width
        scale /= 6
        rect.width *= scale
        rect.height *= scale
        rect.left = 0 + count * rect.width
        rect.top = (height - rect.height) / 2
        ret.blit(pygame.transform.scale(card,(rect.width, rect.height)), rect)
        count += 1
    return ret
        
cardImages = {}
for suit in Durak.SUIT:
    for val in Durak.VALUE:
        if (suit, val) not in cardImages:
            cardImages[(suit, val)] = pygame.image.load("Cards/" + Durak.ValueStrings[val] + "_of_" + Durak.SuitStrings[suit] + ".png")



pygame.init()

displayinfo = pygame.display.Info()
size = width, height = displayinfo.current_w, displayinfo.current_h
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

cards = list(cardImages.values())
hand = createHand(width/2, height/6, cards[:6])
attack = createField(width/2, height / 6, cards[6:11])

    


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    
    handRect = hand.get_rect()
    handRect.left = (width - handRect.width) / 2
    handRect.top = 0
    screen.blit(hand, handRect)

    attackRect = attack.get_rect()
    attackRect.left = (width - attackRect.width) / 2
    attackRect.top = (height - attackRect.height) / 2
    screen.blit(attack, attackRect)
    
    pygame.display.flip()
