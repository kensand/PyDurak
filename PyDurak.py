#!/usr/bin/python3

import sys

WindowLocX = 0
WindowLocY = 0
fullDeck = False
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (WindowLocX, WindowLocY)

import pygame
import Cards


def createDeck(width, height, deck):
    ret = pygame.Surface((width, height))
    if deck.size() > 0:
        rect = deck.Image.get_rect()
        rect.width = width
        rect.height = height
        ret.blit(pygame.transform.scale(deck.Image, (rect.width, rect.height)), rect)
    return ret

def createHand(width, height, cards):
    ret = pygame.Surface((width, height))
    count = 0
    for card in cards:
        rect = card.get_rect()
        offset = 0
        if(len(cards) > 1):
            offset = (width - rect.width) / (len(cards) - 1)
        rect.inflate_ip(height/rect.height, height/rect.height);
        rect.move_ip(rect.left * -1 + count * offset, rect.top * -1)
        ret.blit(pygame.transform.scale(card, (rect.width, rect.height)), rect)
        count += 1
    return ret

def createField(width, height, attack, defense):

    ret = pygame.Surface((width, height))
    if len(attack) > 6 or len(defense) > 6:
        print("Error, more cards than should be in a field")
        return ret
    count = 0

    for card in attack:
        rect = card.Image.get_rect()
        scale = min(width / (rect.width * 6), height / (rect.height * 2))
        rect.width *= scale
        rect.height *= scale
        rect.left = (width - 6 * rect.width) / 2 + count * rect.width
        rect.top = 0#(height - rect.height) / 2
        ret.blit(pygame.transform.scale(card.Image, (rect.width, rect.height)), rect)
        count += 1
    count = 0
    for card in defense:
        rect = card.Image.get_rect()
        scale = min(width / (rect.width * 6), height / (rect.height * 2))
        rect.width *= scale
        rect.height *= scale
        rect.left = (width - 6 * rect.width) / 2 + count * rect.width
        rect.top = (height - rect.height) #/ 2 + rect.height
        ret.blit(pygame.transform.scale(card.Image, (rect.width, rect.height)), rect)
        count += 1
    return ret
        



pygame.init()

displayinfo = pygame.display.Info()
size = width, height = displayinfo.current_w, displayinfo.current_h
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

deck = Cards.Deck(full=False, shuffle=True)
cards = deck.draw(18)
#hand = createHand(width/2, height/6, cards[:6])
field = createField(3 * width / 6, 2 * height / 6, cards[6:12], cards[12:18])

    


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    """
    handRect = hand.get_rect()
    handRect.left = (width - handRect.width) / 2
    handRect.top = 0
    screen.blit(hand, handRect)
    """

    fieldRect = field.get_rect()
    fieldRect.left = (width - fieldRect.width) / 2
    fieldRect.top = (height - fieldRect.height) / 2
    screen.blit(field, fieldRect)
    
    pygame.display.flip()
