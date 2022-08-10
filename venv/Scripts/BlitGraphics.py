import pygame
from pygame.locals import *
from sys import *
from math import ceil
from random import randint

SCREEN_SIZE = (960, 480)
OptionSelected = False

#Navigation through the menus
PRESSANY = 1
TITLESCREEN = 2
NEWGAME = 3
PLAYING = 4
NAVSTATE = PRESSANY

#Difficulties
EASY = 1
NORMAL = 2
HARD = 3
DIFFICULTY = NORMAL

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
cursor = pygame.transform.scale(pygame.image.load("Assets\Images\Spear of Longinus.png").convert_alpha(), [160,90])
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
def CursorUpdate():
    x, y = pygame.mouse.get_pos()
    screen.blit(cursor, [x-15,y-10])

#Creates a new button
def NewButton(size):
    width, height = SCREEN_SIZE
    return pygame.surface.Surface([width * size[0], height * size[1]])
#Button Surface Objects
PressAnyButton = NewButton([0.3, 0.1])
LoadGameButton = NewButton([0.3, 0.1])
NewGameButton = NewButton([0.3, 0.1])
QuitButton = NewButton([0.3, 0.1])
EasyButton = NewButton([0.3, 0.1])
NormalButton = NewButton([0.3, 0.1])
HardButton = NewButton([0.3, 0.1])

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
    global LoadGameButton, NewGameButton, QuitButton, OptionSelected
    buttonX = ceil(SCREEN_SIZE[0] * 0.35)
    buttonY = ceil(SCREEN_SIZE[1] * 0.25)
    counter = 1
    for button in [LoadGameButton, NewGameButton, QuitButton]:
        textstr = ""
        if button.get_rect(topleft=([buttonX, buttonY])).collidepoint(pygame.mouse.get_pos()):
            fill_color = 255
            if pygame.mouse.get_pressed(num_buttons=3)[0] and not OptionSelected:
                OptionSelected = True
                if counter == 1:
                    print("")
                elif counter == 2:
                    ChangeState(NEWGAME)
                elif counter == 3:
                    exit()
        else:
            fill_color = 150
        button.fill([fill_color, 0, 0])

        if counter == 1:
            textstr = "Load Game"
        elif counter == 2:
            textstr = "New Game"
        elif counter == 3:
            textstr = "Exit"
        else:
            counter = 0
        counter += 1

        textbox = pygame.font.SysFont("arial", 34).render(textstr, True, [255, 255, 255],
                                                          button.get_colorkey())
        button.blit(textbox, [(button.get_width() - textbox.get_width()) / 2,
                                      (button.get_height() - textbox.get_height()) / 2])
        screen.blit(button, [buttonX, buttonY])
        buttonY += button.get_height() + 20

def NewGameUpdate():
    global EasyButton, NormalButton, HardButton, OptionSelected
    buttonX = ceil(SCREEN_SIZE[0] * 0.35)
    buttonY = ceil(SCREEN_SIZE[1] * 0.25)
    counter = 1
    for button in [EasyButton, NormalButton, HardButton]:
        textstr = ""
        if button.get_rect(topleft=([buttonX, buttonY])).collidepoint(pygame.mouse.get_pos()):
            fill_color = 255
            if pygame.mouse.get_pressed(num_buttons=3)[0] and not OptionSelected:
                OptionSelected = True
                ChangeState(PLAYING)
                if counter == 1:
                    ChangeDifficulty(EASY)
                elif counter == 2:
                    ChangeDifficulty(NORMAL)
                elif counter == 3:
                    ChangeDifficulty(HARD)
        else:
            fill_color = 150
        button.fill([fill_color, 0, 0])

        if counter == 1:
            textstr = "Easy"
        elif counter == 2:
            textstr = "Normal"
        elif counter == 3:
            textstr = "Hard"
        else:
            counter = 0
        counter += 1

        textbox = pygame.font.SysFont("arial", 34).render(textstr, True, [255, 255, 255],
                                                          button.get_colorkey())
        button.blit(textbox, [(button.get_width() - textbox.get_width()) / 2,
                              (button.get_height() - textbox.get_height()) / 2])
        screen.blit(button, [buttonX, buttonY])
        buttonY += button.get_height() + 20

def GameplayUpdate():
    return None

def ChangeState(state):
    global NAVSTATE
    NAVSTATE = state

def ChangeDifficulty(difficulty):
    global DIFFICULTY
    DIFFICULTY = difficulty

def EventHandler():
    global OptionSelected
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if NAVSTATE == PRESSANY\
                and not pygame.key.get_pressed()[K_ESCAPE]:
                ChangeState(TITLESCREEN)
            elif NAVSTATE > PRESSANY:
                    if pygame.key.get_pressed()[K_ESCAPE]:
                        ChangeState(NAVSTATE-1)
        elif event.type == MOUSEBUTTONUP:
            OptionSelected = False

def StateUpdate():
    if NAVSTATE == PRESSANY:
        PressAnyUpdate()
    elif NAVSTATE == TITLESCREEN:
        TitleUpdate()
    elif NAVSTATE == NEWGAME:
        NewGameUpdate()
    elif NAVSTATE == PLAYING:
        GameplayUpdate()

#Graphics Life Cycle
while True:
    clock.tick(75)
    ScreenUpdate()
    EventHandler()
    StateUpdate()
    CursorUpdate()
    #print("state: " + str(NAVSTATE) + " option selected: " + str(OptionSelected))
    pygame.display.update()