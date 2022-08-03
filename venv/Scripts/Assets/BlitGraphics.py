import pygame
from pygame.locals import *
from sys import *
from math import ceil
from random import randint

SCREEN_SIZE = (960, 480)

#Navigation through the menus
PRESSANY = 1
TITLESCREEN = 2
NAVSTATE = PRESSANY

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
cursor = pygame.transform.scale(pygame.image.load("Images\Spear of Longinus.png").convert_alpha(), [160,90])
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()
total_time = 0
#Random numbers used for Press Any Button
randR = 0
randG = 0
randB = 0

#Updates the screen every frame
def ScreenUpdate():
    screen.fill((25, 25, 25))

#Updates the cursor
def CursorUpdate(event):
    screen.blit(cursor, pygame.mouse.get_pos())

#Creates a new button
def NewButton(size):
    width, height = SCREEN_SIZE
    return pygame.surface.Surface([width * size[0], height * size[1]])
#Button Surface Objects
PressAnyButton = NewButton([0.3, 0.1])

#Updates the display during the Press Any phase prior to title menu selection
def PressAnyUpdate():
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

#TODO: Updates the display during title menu selection
def TitleUpdate():
    return None

#Graphics Life Cycle
while True:
    clock.tick(75)
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if NAVSTATE == PRESSANY:
                NAVSTATE = TITLESCREEN
            elif NAVSTATE == TITLESCREEN and pygame.key.get_pressed()[K_ESCAPE]:
                NAVSTATE = PRESSANY
    ScreenUpdate()
    if NAVSTATE == PRESSANY:
        PressAnyUpdate()
    elif NAVSTATE == TITLESCREEN:
        TitleUpdate()
    CursorUpdate(event)
    pygame.display.update()