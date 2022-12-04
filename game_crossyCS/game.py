import pygame
from player import Player
from map import MapManager
from car import Car

from menu import *
from time import sleep

from pygame import mixer


class Game:

    def __init__(self):
        pygame.display.set_caption("Crossy-CS")
        self.screen = pygame.display.set_mode((500, 750))

        # initialise le menu
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.display = pygame.Surface((500, 750))
        self.window = pygame.display.set_mode(((500, 750)))
        self.font_name = 'graphic/police/8-BIT WONDER.TTF'
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.level = Level(self)
        self.personnage = Personnage(self)
        self.curr_menu = self.main_menu

    def check_events(self):  # pour le menu
        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def draw_text(self, text, size, x, y):  # pour le menu
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def reset_keys(self):  # pour le menu
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def update(self):
        self.map_manager.update()
        self.map_manager.move(self.car_num)

    def draw(self):
        self.map_manager.draw()

    def run(self):

        clock = pygame.time.Clock()
        self.crash_sound = pygame.mixer.Sound('sounds/crashsound.wav')
        self.jump_sound = pygame.mixer.Sound('sounds/jumpsound.wav')

        # self.personnage.perso détermine le perso
        self.player = Player(0, 0, self.personnage.perso)
        self.car_num = 26       # le nombre de voitures présentes sur la carte
        self.car = []
        self.velocity = self.level.niveaux  # on détermine les vitesses
        for i in range(int(self.car_num/2)):
            self.car.append(Car(0, 0, f"{i}", self.velocity))
        for i in range(int(self.car_num/2), int(self.car_num)):
            self.car.append(Car(0, 0, f"{i}", self.velocity))

        # on appelle la map

        self.map_manager = MapManager(
            self.screen, self.player, self.car, self.car_num)

        # tant que l'on joue une partie :

        while self.playing:

            self.player.save_location()

            self.update()

            self.draw()

            pygame.display.flip()  # mettre à jour notre écran

            # gère la collision avec les voitures (mort)

            for sprite in self.map_manager.get_group().sprites():
                if type(sprite) is Car:
                    if sprite.rect.colliderect(self.player.rect):
                        mixer.music.stop()
                        self.display.fill(self.BLACK)
                        self.draw_text('Perdu', 20, 250, 375)
                        self.window.blit(self.display, (0, 0))
                        pygame.display.update()
                        mixer.music.load('sounds/GameOver.wav')
                        mixer.music.play(-1)
                        sleep(1.4)

                        self.playing = False

            for event in pygame.event.get():

                if event.type == pygame.QUIT:  # retour à l'acceuil
                    self.playing = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:  # détecte si un joueur lache une touche de clavier
                        self.player.move_right()  # mouvement du joueur
                        # pour changer l'image du joueur dans la direction adéquate
                        self.player.change_animation("right")
                    elif event.key == pygame.K_UP:
                        self.player.move_up()
                        self.player.change_animation("up")
                    elif event.key == pygame.K_LEFT:
                        self.player.change_animation("left")
                        self.player.move_left()
                    elif event.key == pygame.K_DOWN:
                        self.player.move_down()
                        self.player.change_animation("down")
                    self.player.adapt_color(self.personnage.perso)
                    self.jump_sound.play()  # son lors d'un déplacement

                    self.update()

                    for sprite in self.map_manager.get_group().sprites():  # detecte les collisions avec les obstacles
                        if sprite.feet.collidelist(self.map_manager.get_walls()) > -1:
                            self.player.move_back()

                    for sprite in self.map_manager.get_group().sprites():  # detecte les lieux de mort
                        if sprite.feet.collidelist(self.map_manager.dead) > -1:
                            mixer.music.stop()
                            self.display.fill(self.BLACK)
                            self.draw_text('Perdu', 20, 250, 375)
                            self.window.blit(self.display, (0, 0))
                            pygame.display.update()
                            # musique de mort
                            mixer.music.load('sounds/GameOver.wav')
                            mixer.music.play(-1)
                            sleep(1.4)

                            self.playing = False
                    for sprite in self.map_manager.get_group().sprites():
                        if sprite.feet.collidelist(self.map_manager.win) > -1:
                            mixer.music.stop()
                            self.display.fill(self.BLACK)
                            self.draw_text('gagne', 20, 250, 375)
                            self.window.blit(self.display, (0, 0))
                            pygame.display.update()
                            # musique de victoire
                            mixer.music.load('sounds/Won!.wav')
                            mixer.music.play(-1)
                            sleep(2)

                            self.playing = False

            clock.tick(60)
        self.__init__()
