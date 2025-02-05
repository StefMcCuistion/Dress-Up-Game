from settings import *

class Game():

    def __init__(self):

        class Player(pg.sprite.Sprite):
            def __init__(self, groups, surf):
                super().__init__(groups)
                self.image = surf
                self.rect = self.image.get_frect(center = (W / 2, H / 2))
                self.skin = 'fair'
                self.hair = 'emo'
                self.hair_color = 'blonde'
                self.race = 'cat'
                self.top = 'coat'
                self.bottom = 'shorts'

            def change_appearance(self):
                surf = pg.Surface((1766, 2513), pg.SRCALPHA)
                surf.blit(pg.image.load(join('img', f'player_legs_{self.skin}.png')))
                if self.race == 'cat':
                    surf.blit(pg.image.load(join('img', f'player_tail_{self.hair_color}.png')))
                surf.blit(pg.image.load(join('img', f'player_bottom_{self.bottom}.png')))
                surf.blit(pg.image.load(join('img', f'player_hair_back_{self.hair}_{self.hair_color}.png')))
                surf.blit(pg.image.load(join('img', f'player_torso_{self.skin}.png')))
                surf.blit(pg.image.load(join('img', f'player_top_{self.top}.png')))
                surf.blit(pg.image.load(join('img', f'player_head_{self.skin}_{self.race}.png')))
                if self.race == 'cat':
                    surf.blit(pg.image.load(join('img', f'player_ears_{self.hair_color}.png')))
                surf.blit(pg.image.load(join('img', f'player_face.png')))
                surf.blit(pg.image.load(join('img', f'player_hair_front_{self.hair}_{self.hair_color}.png')))
                surf = pg.transform.scale_by(surf, .3)
                self.image = surf

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

        # Sprites
        self.sprites = pg.sprite.Group()
        self.player = Player(self.sprites, self.player_surf)

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