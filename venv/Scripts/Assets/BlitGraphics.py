import pygame
from pygame.locals import *
from sys import *
from math import ceil

SCREEN_SIZE = (1280, 720)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
cursor = pygame.transform.scale(pygame.image.load("Images\Spear of Longinus.png").convert_alpha(), [160,90])
pygame.mouse.set_visible(False)

def ScreenUpdate():
    screen.fill((25, 25, 25))

def CursorUpdate(event):
    screen.blit(cursor, pygame.mouse.get_pos())
    
def NewButton(size):
    width, height = SCREEN_SIZE
    return pygame.surface.Surface([width * size[0], height * size[1]])

def TitleScreenUpdate():
    PressAnyButton = NewButton([0.3, 0.1])

    PressAnyButton.fill([255,0,0])
    pressanytext = pygame.font.SysFont("arial",22).render("Press Any Button", True, [255,255,255], PressAnyButton.get_colorkey())
    PressAnyButton.blit(pressanytext, [(PressAnyButton.get_width()-pressanytext.get_width())/2, (PressAnyButton.get_height()-pressanytext.get_height())/2])
    screen.blit(PressAnyButton, [ceil(SCREEN_SIZE[0]*0.35), ceil(SCREEN_SIZE[1]*0.7)])
    
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    ScreenUpdate()
    TitleScreenUpdate()
    CursorUpdate(event)
    pygame.display.update()