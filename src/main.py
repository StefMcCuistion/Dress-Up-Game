from settings import *

class Game():

    def __init__(self):

        class Player(pg.sprite.Sprite):
            def __init__(self, groups, surf, parts):
                super().__init__(groups)
                self.parts = parts
                self.skin_colors = ['fair']
                self.races = ['human', 'cat']
                self.hairstyles = ['emo']
                self.hair_colors = ['black', 'blond', 'brown']
                self.bottoms = ['shorts']
                self.tops = ['crop', 'coat']
                self.image = self.change_appearance()
                self.rect = self.image.get_frect(center = (W / 2, H / 2))

            def change_appearance(self):
                surf = pg.Surface((1766, 2513), pg.SRCALPHA)
                skin_color_idx = randint(len(self.skin_colors))
                hairstyle_idx = randint(len(self.hairstyles))
                hair_color_idx = randint(len(self.hair_colors))
                for part in self.parts:


                # surf.blit(pg.image.load(join('img', f'player_legs_{self.skin}.png')))
                # if self.race == 'cat':
                #     surf.blit(pg.image.load(join('img', f'player_tail_{self.hair_color}.png')))
                # surf.blit(pg.image.load(join('img', f'player_bottom_{self.bottom}.png')))
                # surf.blit(pg.image.load(join('img', f'player_hair_back_{self.hair}_{self.hair_color}.png')))
                # surf.blit(pg.image.load(join('img', f'player_torso_{self.skin}.png')))
                # surf.blit(pg.image.load(join('img', f'player_top_{self.top}.png')))
                # surf.blit(pg.image.load(join('img', f'player_head_{self.skin}_{self.race}.png')))
                # if self.race == 'cat':
                #     surf.blit(pg.image.load(join('img', f'player_ears_{self.hair_color}.png')))
                # surf.blit(pg.image.load(join('img', f'player_face.png')))
                # surf.blit(pg.image.load(join('img', f'player_hair_front_{self.hair}_{self.hair_color}.png')))
                # surf = pg.transform.scale_by(surf, .3)
                # self.image = surf

        # Setup
        pg.init
        pg.font.init
        ctypes.windll.user32.SetProcessDPIAware() # keeps Windows GUI scale settings from messing with resolution
        self.display = pg.display.set_mode((W, H), pg.FULLSCREEN)
        self.fullscreen = True
        pg.display.set_caption('Dress Up Game')
        if not self.fullscreen: # These just slow down game launch if done in fullscreen
            os.environ['SDL_VIDEO_CENTERED'] = '1' # Centers window
            app = pywinauto.Application().connect(title_re='Dress Up Game')
            app.top_window().set_focus() #Activates window
        self.clock = pg.time.Clock()
        self.running = True

        # Imports
        self.player_surf = pg.image.load(join('img', 'player_test.png')).convert_alpha()
        self.player_surf = pg.transform.scale_by(self.player_surf, .3)

        self.player_parts = {'legs':[], 'cat_tails':[], 'bottoms':[], 'emo_hair_backs':[], 'torsos':[], 'tops':[], 'human_heads':[], 'cat_heads':[], 'cat_ears':[], 'faces':[], 'emo_hair_fronts':[]}
        for part in self.player_parts.keys():
            for folder_path, sub_folders, file_names in walk(join('img', 'parts', part)):
                if file_names:
                    for file_name in sorted(file_names, key = lambda name: int(name.split('.')[0])):
                        path = join(folder_path, file_name)
                        surf = pg.image.load(path).convert_alpha()
                        self.player_parts[part].append(surf)

        # Sprites
        self.sprites = pg.sprite.Group()
        self.player = Player(self.sprites, self.player_surf, self.player_parts)

    def run(self):

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
                            self.display = pg.display.set_mode((W, H), pg.FULLSCREEN)
                        else:
                            self.display = pg.display.set_mode((W, H))
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.player.change_appearance()
            # Render
            self.display.fill('dark gray')
            self.sprites.draw(self.display)
            pg.display.flip()

        pg.quit()
        exit()

if __name__ == "__main__":
    game = Game()
    game.run()