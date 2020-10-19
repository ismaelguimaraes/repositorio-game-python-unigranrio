import pygame.image

class VALENTINA:
    def __init__(self):
        self.NAME = 'Valentina'
        self.SPRITE_POS = pygame.image.load('./sprites/chars/valentina/valentina_b0.png')
        self.PLAYER_POS = [10, 9]
        self.PLAYER_INV = []
        self.WEAPON = False
        self.HEALTH = 5
        self.DIRECTION = False
        self.TRANSFORM = False

    def TRANSFORMING(self):
        self.TRANSFORM = not self.TRANSFORM

class ENZO:
    def __init__(self):
        self.NAME = 'Enzo'
        self.SPRITE_POS = pygame.image.load('./sprites/chars/enzo/enzo_b0.png')
        self.PLAYER_POS = [10,9]
        self.PLAYER_INV = []
        self.WEAPON = False
        self.HEALTH = 5
        self.DIRECTION = False
        self.TRANSFORM = False

    def TRANSFORMING(self):
        self.TRANSFORM = not self.TRANSFORM 