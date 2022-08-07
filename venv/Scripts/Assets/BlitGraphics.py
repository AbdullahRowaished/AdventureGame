import pygame
from pygame.locals import *
from sys import *
from math import ceil
from random import randint

SCREEN_SIZE = (960, 480)

#Navigation through the menus
PRESSANY = 1
TITLESCREEN = 2
NEWGAME = 3
NAVSTATE = PRESSANY

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
cursor = pygame.transform.scale(pygame.image.load("Images\Spear of Longinus.png").convert_alpha(), [160,90])
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()
#Random numbers used for Press Any Button
randR = 0
randG = 0
randB = 0

#Updates the screen every frame
def ScreenUpdate():
    screen.fill((25, 25, 25))

#Updates the cursor
def CursorUpdate():
    screen.blit(cursor, pygame.mouse.get_pos())

#Creates a new button
def NewButton(size):
    width, height = SCREEN_SIZE
    return pygame.surface.Surface([width * size[0], height * size[1]])
#Button Surface Objects
PressAnyButton = NewButton([0.3, 0.1])
LoadGameButton = NewButton([0.3, 0.1])
NewGameButton = NewButton([0.3, 0.1])
QuitButton = NewButton([0.3, 0.1])

#Updates the display during the Press Any phase prior to title menu selection
def PressAnyUpdate():
    global PressAnyButton
    buttonX = ceil(SCREEN_SIZE[0]*0.35)
    buttonY = ceil(SCREEN_SIZE[1]*0.7)
    PressAnyButton.fill((25, 25, 25))
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
    global LoadGameButton, NewGameButton, QuitButton
    buttonX = ceil(SCREEN_SIZE[0] * 0.35)
    buttonY = ceil(SCREEN_SIZE[1] * 0.25)
    counter = 1
    for button in [LoadGameButton, NewGameButton, QuitButton]:
        if button.get_rect(topleft=([buttonX, buttonY])).collidepoint(pygame.mouse.get_pos()):
            fill_color = 255
        else:
            fill_color = 150
        button.fill([fill_color, 0, 0])
        textstr = ""
        if counter == 1:
            textstr = "Load Game"
        elif counter == 2:
            if button.get_rect(topleft=([buttonX, buttonY])).collidepoint(pygame.mouse.get_pos()) \
                    and pygame.mouse.get_pressed(num_buttons=3)[0]:
                ChangeState(NEWGAME)
            textstr = "New Game"
        elif counter == 3:
            if button.get_rect(topleft=([buttonX, buttonY])).collidepoint(pygame.mouse.get_pos())\
                    and pygame.mouse.get_pressed(num_buttons=3)[0]:
                exit()
            textstr = "Exit"
        elif counter > 3:
            counter = 0
        counter += 1
        textbox = pygame.font.SysFont("arial", 34).render(textstr, True, [255, 255, 255],
                                                          button.get_colorkey())
        button.blit(textbox, [(button.get_width() - textbox.get_width()) / 2,
                                      (button.get_height() - textbox.get_height()) / 2])
        screen.blit(button, [buttonX, buttonY])
        buttonY += button.get_height() + 20

def NewGameUpdate():
    return None

def ChangeState(state):
    global NAVSTATE
    NAVSTATE = state

def EventHandler():
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if NAVSTATE == PRESSANY\
                and not pygame.key.get_pressed()[K_ESCAPE]:
                ChangeState(TITLESCREEN)
            elif NAVSTATE == TITLESCREEN:
                    if pygame.key.get_pressed()[K_ESCAPE]:
                        ChangeState(PRESSANY)

def StateUpdate():
    if NAVSTATE == PRESSANY:
        PressAnyUpdate()
    elif NAVSTATE == TITLESCREEN:
        TitleUpdate()
    elif NAVSTATE == NEWGAME:
        NewGameUpdate()

#Graphics Life Cycle
while True:
    clock.tick(75)
    ScreenUpdate()
    EventHandler()
    StateUpdate()
    CursorUpdate()
    pygame.display.update()