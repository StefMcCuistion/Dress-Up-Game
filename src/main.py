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
    # Setup
    W, H = (
            1280, 
            720
    )       # Window width and height
    pg.init
    pg.font.init
    os.environ['SDL_VIDEO_CENTERED'] = '1' # centers window when not in fullscreen
    ctypes.windll.user32.SetProcessDPIAware() # keeps Windows GUI scale settings from messing with resolution
    display = pg.display.set_mode((W, H), pg.FULLSCREEN)
    fullscreen = True
    pg.display.set_caption('Dress Up Game')
    app = pywinauto.Application().connect(title_re='Dress Up Game')
    app.top_window().set_focus() #Activates window if it isn't launched in fullscreen
    clock = pg.time.Clock()
    running = True

    while running: 
        dt = clock.tick() / 1000
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

        pg.display.flip()

    pg.quit()
    exit()




if __name__ == "__main__":
    main()