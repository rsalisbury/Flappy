# Import the pygame module
import pygame
# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
    KEYDOWN,
    QUIT,
    K_SPACE
)

SCREENWIDTH = 288
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

# Create a string to hold the filename
BACKGROUND = "images/background.png"
BACKGROUNDSM = "images/background_sm.png"

# A new way to create a surface, blit it to the screen to see
background = pygame.image.load(BACKGROUND).convert()
backgroundsm = pygame.image.load(BACKGROUNDSM).convert()

pygame.init()
x = 0
gameover = False
while not gameover:
# Look at every event in the queue
    for event in pygame.event.get():
if event.type == QUIT:
            gameover = True

        if event.type == KEYDOWN: # Did the user hit a key?
            if event.key == K_SPACE:
pass # This is a place holder for future use
    x -= .01
    if x + backgroundsm.get_width() <= 0:
        x = 0

    pygame.draw.rect(SCREEN, (78, 192, 202), [0, 0, SCREENWIDTH, SCREENHEIGHT * .72])
    pygame.draw.rect(SCREEN, (94, 226, 112), [0, SCREENHEIGHT * .72, SCREENWIDTH, SCREENHEIGHT])
    SCREEN.blit(backgroundsm, (x, 300))
    SCREEN.blit(backgroundsm, (x + backgroundsm.get_width(), 300))

    pygame.display.flip()

pygame.quit()