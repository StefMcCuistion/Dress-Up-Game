import pygame as pg
from pygame import mixer
from os.path import join
import os
from sys import exit
import tkinter
import ctypes
import pywinauto
import pyautogui

def main():

    class Player(pg.sprite.Sprite):
        def __init__(self, groups, surf):
            super().__init__(groups)
            self.image = surf
            self.rect = self.image.get_frect(center = (W / 2, H / 2))
            self.skin = 'fair'
            self.hair = 'brown'
            self.race = 'cat'
            self.top = 'crop'
            self.bottom = 'shorts'

        def change_appearance(self):
            surf = pg.image.load(join('img', 'player_empty.png')).convert_alpha
            surf.blit()

    # Setup
    W, H = (
            1280,
            720
    )       # Window width and height
    pg.init
    pg.font.init
    ctypes.windll.user32.SetProcessDPIAware() # keeps Windows GUI scale settings from messing with resolution
    display = pg.display.set_mode((W, H), pg.FULLSCREEN)
    fullscreen = True
    pg.display.set_caption('Dress Up Game')
    if not fullscreen: # These just slow down game launch if done in fullscreen
        os.environ['SDL_VIDEO_CENTERED'] = '1' # Centers window
        app = pywinauto.Application().connect(title_re='Dress Up Game')
        app.top_window().set_focus() #Activates window
    clock = pg.time.Clock()
    running = True

    # Imports
    player_surf = pg.image.load(join('img', 'player_test.png')).convert_alpha()
    player_surf = pg.transform.scale_by(player_surf, .3)

    # Sprites
    sprites = pg.sprite.Group()
    player = Player(sprites, player_surf)

    # Loop
    while running:
        dt = clock.tick() / 1000
        # Event loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
                if event.key == pg.K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        display = pg.display.set_mode((W, H), pg.FULLSCREEN)
                    else:
                        display = pg.display.set_mode((W, H))
        # Render
        display.fill('dark gray')
        sprites.draw(display)
        pg.display.flip()

    pg.quit()
    exit()




if __name__ == "__main__":
    main()