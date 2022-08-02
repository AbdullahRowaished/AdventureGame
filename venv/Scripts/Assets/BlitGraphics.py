import pygame
from pygame.locals import *
from sys import *
from math import ceil
from random import randint

SCREEN_SIZE = (1280, 720)
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
cursor = pygame.transform.scale(pygame.image.load("Images\Spear of Longinus.png").convert_alpha(), [160,90])
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()
randR = 0
randG = 0
randB = 0
total_time = 0

def ScreenUpdate():
    screen.fill((25, 25, 25))

def CursorUpdate(event):
    screen.blit(cursor, pygame.mouse.get_pos())
    
def NewButton(size):
    width, height = SCREEN_SIZE
    return pygame.surface.Surface([width * size[0], height * size[1]])
#Button Surface Objects
PressAnyButton = NewButton([0.3, 0.1])

def TitleScreenUpdate():
    global PressAnyButton
    buttonX = ceil(SCREEN_SIZE[0]*0.35)
    buttonY = ceil(SCREEN_SIZE[1]*0.7)
    if PressAnyButton.get_rect(topleft=([buttonX, buttonY])).collidepoint(pygame.mouse.get_pos()):
        fill_color = 255
    else:
        fill_color = 150
    PressAnyButton.fill([fill_color, 0, 0])
    global total_time, random_color, randR, randG, randB
    total_time += clock.get_time()
    if total_time > 120:
        total_time = 0
        randR = randint(0,255)
        randG = randint(0,255)
        randB = randint(0,255)
    textbox = pygame.font.SysFont("arial",34).render("Press Any Button", True, [randR,randG,randG], PressAnyButton.get_colorkey())
    PressAnyButton.blit(textbox, [(PressAnyButton.get_width()-textbox.get_width())/2, (PressAnyButton.get_height()-textbox.get_height())/2])

    screen.blit(PressAnyButton, [buttonX, buttonY])

while True:
    clock.tick(75)
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    ScreenUpdate()
    TitleScreenUpdate()
    CursorUpdate(event)
    pygame.display.update()