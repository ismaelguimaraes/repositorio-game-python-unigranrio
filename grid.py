import pygame
import random

#TILES
DIRT = 0
GRASS = 1
WATER = 2
WALL = 3

# class Fence:
#     def __init__(self):
#         self.X_POS = 

TEXTURES = {
    DIRT: pygame.image.load('./sprites/textures/dirt.png'),
    GRASS: pygame.image.load('./sprites/textures/grass.png'),
    WATER: pygame.image.load('./sprites/textures/water.png'),
}

# GRID = [
#     [WATER, WATER, WATER, WATER, WATER, WATER, WATER, GRASS, GRASS, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT],
#     [WATER, WATER, WATER, WATER, WATER, WATER, GRASS, GRASS, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT],
#     [WATER, WATER, WATER, WATER, WATER, GRASS, GRASS, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT],
#     [WATER, WATER, WATER, WATER, GRASS, GRASS, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT],
#     [WATER, WATER, WATER, GRASS, GRASS, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT],
#     [WATER, WATER, GRASS, GRASS, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT],
#     [WATER, GRASS, GRASS, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT],
#     [GRASS, GRASS, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT],
#     [DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT],
#     [DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT]
# ]

## GRIDE RESERVA
GRID = [
    [WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER],
    [WATER, WATER, GRASS, GRASS, GRASS, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER],
    [WATER, WATER, GRASS, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER],
    [WATER, WATER, GRASS, DIRT, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, DIRT, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER],
    [WATER, WATER, GRASS, DIRT, GRASS, WATER, WATER, WATER, WATER, WATER, WATER, GRASS, GRASS, GRASS, WATER, WATER, WATER, WATER, WATER, WATER, WATER],
    [WATER, WATER, GRASS, DIRT, GRASS, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER],
    [WATER, WATER, GRASS, DIRT, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER],
    [WATER, WATER, GRASS, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, GRASS, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER],
    [WATER, WATER, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, DIRT, GRASS, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER],
    [WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, GRASS, DIRT, GRASS, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER]
]

TILESIZE = 60
MAPWIDTH = 21
MAPHEIGHT = 10
pygame.init()
pygame.display.set_caption('Adventure Student')

DISPLAYSURFACE = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))
