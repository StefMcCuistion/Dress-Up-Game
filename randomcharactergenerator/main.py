import io
from random import randint
import pygame as pg

# from pygame import mixer
from os.path import join
import os
from os import walk
from sys import exit

# import tkinter
import ctypes
import pywinauto

import pyautogui

# from random import randint

import settings


class Player(pg.sprite.Sprite):
    def __init__(self, groups, parts):
        super().__init__(groups)
        self.parts = parts
        self.skin_colors = ["fair", "pale_brown"]
        self.races = ["human", "cat"]
        self.hairstyles = ["emo"]
        self.hair_colors = ["black", "blonde", "brown"]
        self.bottoms = ["shorts", "skirt"]
        self.chests = ["cropped_shirt", "bra"]
        self.tops = ["none", "jacket", "coat", 'cropped_hoodie']
        self.socks = ["none", "leggings", "thigh_highs"]
        self.change_appearance()
        self.rect = self.image.get_frect(topleft=(settings.W * .5, 0))
        
        # Index Defaults
        self.skin_colors_idx = 0
        self.hairstyles_idx = 0
        self.hair_colors_idx = 0
        self.races_idx = 0
        self.tops_idx = 0
        self.bottoms_idx = 0
        self.socks_idx = 0
        self.chests_idx = 0

        
    def randomize_attributes(self):
        self.skin_colors_idx = randint(0, len(self.skin_colors) - 1)
        self.hairstyles_idx = randint(0, len(self.hairstyles) - 1)
        self.hair_colors_idx = randint(0, len(self.hair_colors) - 1)
        self.races_idx = randint(0, len(self.races) - 1)
        self.tops_idx = randint(0, len(self.tops) - 1)
        self.bottoms_idx = randint(0, len(self.bottoms) - 1)
        self.socks_idx = randint(0, len(self.socks) - 1)
        self.chests_idx = randint(0, len(self.chests) - 1)

    def change_appearance(self):
        surf = pg.Surface((1766, 2513), pg.SRCALPHA)

        self.randomize_attributes()

        if self.tops[self.tops_idx] != 'none': 
            surf.blit(self.parts[f'top_{self.tops[self.tops_idx]}_back1'])
        if self.races[self.races_idx] == "cat":
            surf.blit(self.parts[f'tail_cat_{self.hair_colors[self.hair_colors_idx]}'])
        if self.tops[self.tops_idx] != 'none': 
            surf.blit(self.parts[f'top_{self.tops[self.tops_idx]}_back2'])
        surf.blit(self.parts[f'hair_{self.hairstyles[self.hairstyles_idx]}_{self.hair_colors[self.hair_colors_idx]}_back'])
        surf.blit(self.parts[f'body_{self.skin_colors[self.skin_colors_idx]}'])
        surf.blit(self.parts[f'socks_{self.socks[self.socks_idx]}'])
        surf.blit(self.parts[f'bottom_{self.bottoms[self.bottoms_idx]}'])
        surf.blit(self.parts[f'chest_{self.chests[self.chests_idx]}'])
        surf.blit(self.parts[f'arm_{self.skin_colors[self.skin_colors_idx]}'])
        surf.blit(self.parts[f'top_{self.tops[self.tops_idx]}_front'])
        surf.blit(self.parts[f'face_purple'])
        if self.races[self.races_idx] == "cat":
            surf.blit(self.parts[f'catear_back_{self.hair_colors[self.hair_colors_idx]}'])
        else: 
            surf.blit(self.parts[f'humanear_{self.skin_colors[self.skin_colors_idx]}'])
        surf.blit(self.parts[f'hair_{self.hairstyles[self.hairstyles_idx]}_{self.hair_colors[self.hair_colors_idx]}_front'])
        if self.races[self.races_idx] == "cat":
            surf.blit(self.parts[f'catear_front_{self.hair_colors[self.hair_colors_idx]}'])

        data = pg.image.tobytes(surf, "RGBA")
        final_surf = pg.image.frombytes(data, (1766, 2513), "RGBA")
        final_surf = pg.transform.scale_by(final_surf, .4)
        self.image = final_surf


class Game:

    def __init__(self):

        # Setup
        pg.init()
        pg.font.init()
        ctypes.windll.user32.SetProcessDPIAware()  # keeps Windows GUI scale settings from messing with resolution
        monitor_size = pg.display.list_modes()[0]
        self.display = pg.display.set_mode((settings.W, settings.H))
        self.fullscreen = False
        pg.display.set_caption("Dress Up Game")
        if not self.fullscreen:  # These just slow down game launch if done in fullscreen
            os.environ["SDL_VIDEO_CENTERED"] = "1"  # Centers window
            # app = pywinauto.Application().connect(title_re="Dress Up Game")
            # app.top_window().set_focus() # Activates window
        self.clock = pg.time.Clock()
        self.running = True

        current_dir = os.path.dirname(os.path.abspath(__file__))
        asset_location = os.path.join(current_dir, "assets")

        # Imports
        self.player_parts = {}
        for folder_path, sub_folders, file_names in walk(join(asset_location, "img", "player_pieces")):
            if file_names:
                for file_name in file_names:
                    path = join(folder_path, file_name)
                    surf = pg.image.load(path).convert_alpha()
                    self.player_parts[file_name.split('.')[0]] = surf

        # Sprites
        self.sprites = pg.sprite.Group()
        self.player = Player(self.sprites, self.player_parts)

    def start(self):

        # Loop
        while self.running:
            self.dt = self.clock.tick() / 1000
            # Event loop
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.running = False
                    if event.key == pg.K_f:
                        self.fullscreen = not self.fullscreen
                        if self.fullscreen:
                            self.display = pg.display.set_mode((settings.W, settings.H), pg.FULLSCREEN)
                        else:
                            self.display = pg.display.set_mode((settings.W, settings.H))
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.player.change_appearance()
            # Render
            self.display.blit(pg.image.load(join('assets', 'img', 'test_bg.png')).convert_alpha())
            self.sprites.draw(self.display)
            pg.display.flip()


    def run(self):

        bg = pg.image.load(join('assets', 'img', 'test_bg.png')).convert_alpha()

        # Loop
        while self.running:
            self.dt = self.clock.tick() / 1000
            # Event loop
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.running = False
                    if event.key == pg.K_f:
                        self.fullscreen = not self.fullscreen
                        if self.fullscreen:
                            self.display = pg.display.set_mode((settings.W, settings.H), pg.FULLSCREEN)
                        else:
                            self.display = pg.display.set_mode((settings.W, settings.H))
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.player.change_appearance()
            # Render
            self.display.blit(bg)
            self.sprites.draw(self.display)
            pg.display.flip()

        pg.quit()
        exit()


if __name__ == "__main__":
    game = Game()
    game.run()
