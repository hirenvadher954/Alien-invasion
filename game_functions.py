import sys
from settings import Settings

import pygame


def checks_events():
    for event in pygame.event.get():
        if event == pygame.QUIT:
            sys.exit()
def update_screen(ai_setting,screen,ship):
    screen.fill(ai_setting.bg_color)
    ship.blitme()

    pygame.display.flip()