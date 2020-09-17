import pygame.image

rand = random.randint

class SWORD():
    def __init__(self):
        self.NAME = 'Espada ainda sem nome'
        self.IMAGE = pygame.image.load('./sprites/weapons/fire_blade_of_tai.png')
        self.IMAGE_ARMED = pygame.transform.scale(self.IMAGE, (35, 35))
        self.PLACED = True

class GOLD():
    NAME = ''
