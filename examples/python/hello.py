#!/usr/bin/python

import pygame, sys
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED = (255,0,0)

pygame.init()

pygame.display.set_caption('Hello World')
size = [400, 200]
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 48)
text = font.render('Hello World!', True, BLACK, WHITE)
textrect = text.get_rect()
textrect.centerx = screen.get_rect().centerx
textrect.centery = screen.get_rect().centery

screen.fill(RED)
screen.blit(text, textrect)

pygame.display.update()

while True:
    for event in pygame.event.get():
        print event
        if event.type == pygame.QUIT:
 			pygame.display.quit()
			pygame.quit()
			sys.exit()
    clock.tick(20)
