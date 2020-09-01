import pygame, sys
from pygame.locals import *

pygame.init()
maSurface=pygame.display.set_mode((500,300))
pygame.display.set_caption('hello cesi')
inProgress = True
maSurface.fill((255,255,255))
pygame.draw.line(maSurface,(0,255,255),(0,10),(300,50),2)
pygame.draw.rect(maSurface, (0,255,255), (300, 125, 115, 50), 1)
while inProgress:
    for event in pygame.event.get():
        if event.type == QUIT:
            inProgress = False
    pygame.display.update()
pygame.quit()