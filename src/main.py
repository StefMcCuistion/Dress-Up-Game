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
    display = pg.display.set_mode((W, H))
    pg.display.set_caption('Dress Up Game')
    clock = pg.time.Clock()
    running = True

    while running: 
        dt = clock.tick() / 1000
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
    pg.quit()




if __name__ == "__main__":
    main()