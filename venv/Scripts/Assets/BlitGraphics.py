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

def TitleScreen():
    PressAnyButton = NewButton([0.3, 0.1])
    LoadGame = NewButton([0.3, 0.1])
    NewGame = NewButton([0.3, 0.1])
    ExitButton = NewButton([0.3, 0.1])
    
    START = 0
    MAIN_MENU = 1
    LOAD_GAME = 2
    NEW_GAME = 3
    EXIT_GAME = 4

    PressAnyButton.fill([255,0,0])
    pressanytext = pygame.font.SysFont("arial",22).render("Press Any Button", True, [0,0,0], [255,255,255])
    screen.blit(PressAnyButton, [ceil(SCREEN_SIZE[0]*0.35), ceil(SCREEN_SIZE[1]*0.7)])
    PressAnyButton.blit(pressanytext, [0,0])
    
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    ScreenUpdate()
    TitleScreen()
    CursorUpdate(event)
    pygame.display.update()