import pygame, sys, random, math
from pygame.locals import *
from lib import heroes, items
from grid import *
from key_events import KeyEvents

## Instanciandos as dependencias dos objetos
PLAYER = heroes.ENZO()
key_events = KeyEvents(PLAYER)
SWORD = items.SWORD()

## Algumas configurações extras
INV_FONT = pygame.font.SysFont('FreeSansBold.ttf', 20)
HEALTH_FONT = pygame.font.SysFont('FreeSansBold.ttf', 40)

GAME_OVER = False

# Início do loop do jogo
while not GAME_OVER:
    for event in pygame.event.get():

        keys = pygame.key.get_pressed()
        key_events.global_events()

        if event.type == QUIT:
            key_events.quit()

        # Movimentação pra direita
        if (keys[K_RIGHT]) and PLAYER.PLAYER_POS[0] < MAPWIDTH - 1:
            key_events.key_right()

        # Movimentação pra esquerda
        if (keys[K_LEFT]) and PLAYER.PLAYER_POS[0] > 0:
            key_events.key_left()

        # Movimentação pra cima
        if (keys[K_UP]) and PLAYER.PLAYER_POS[1] > 0:
            key_events.key_up()

        # Movimentação pra baixo
        if (keys[K_DOWN]) and PLAYER.PLAYER_POS[1] < MAPHEIGHT -1:
            key_events.key_down()


    # Renderização do Mapa
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURFACE.blit(TEXTURES[GRID[row][column]], (column*TILESIZE, row*TILESIZE))

    # Renderização do personagem
    DISPLAYSURFACE.blit(PLAYER.SPRITE_POS, (PLAYER.PLAYER_POS[0]*TILESIZE, PLAYER.PLAYER_POS[1]*TILESIZE))

    # Renderização das árvores
    for tree in sorted(trees, key=lambda t: t.Y_POS):
        DISPLAYSURFACE.blit(tree.SPRITE, (tree.X_POS, tree.Y_POS))

    # Update do jogo
    pygame.display.update()
# Final do loop do jogo