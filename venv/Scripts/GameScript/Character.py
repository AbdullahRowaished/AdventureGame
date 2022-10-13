import pygame

class Character:
    Name = ""
    Face = ""
    Health = 100
    Stamina = 50
    Melodite = 0
    Instruments = []
    Items = []
    Skills = []
    Relations = []
    ID = 0
    Position = []
    Sprite = []

    def __init__(self):
        self.Name = "Drumsy"