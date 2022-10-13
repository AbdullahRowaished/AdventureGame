import pygame

class Game:
    Difficulty = ""
    NewOrLoad = ""
    Levels = []
    Characters = ""


    def __init__(self):
        self.Characters = FillCharacters()
        self.Levels = FillLevels()

    def LoadLevel(self):
        level = Levels.pop(0)

    @staticmethod
    def Start():
        BlitGraphics.RunGfx()