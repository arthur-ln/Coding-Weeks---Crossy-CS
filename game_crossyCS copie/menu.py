import pygame
from time import sleep


import pygame
from time import sleep


class Menu():
    def __init__(self, game):
        pygame.init()
        self.game = game
        self.mid_w, self.mid_h = 250, 375
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.levelx, self.levely = self.mid_w, self.mid_h + 50
        self.persox, self.persoy = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):  # affiche le menu principal
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Main Menu', 20, 250, 355)
            self.game.draw_text("Start Game", 20, self.startx, self.starty)
            self.game.draw_text("Niveau", 20, self.levelx, self.levely)
            self.game.draw_text("Personnage", 20, self.persox, self.persoy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (
                    self.levelx + self.offset, self.levely)
                self.state = 'Level'
            elif self.state == 'Level':
                self.cursor_rect.midtop = (
                    self.persox + self.offset, self.persoy)
                self.state = 'Personnage'
            elif self.state == 'Personnage':
                self.cursor_rect.midtop = (
                    self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (
                    self.persox + self.offset, self.persoy)
                self.state = 'Personnage'
            elif self.state == 'Level':
                self.cursor_rect.midtop = (
                    self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Personnage':
                self.cursor_rect.midtop = (
                    self.levelx + self.offset, self.levely)
                self.state = 'Level'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Level':
                self.game.curr_menu = self.game.level
            elif self.state == 'Personnage':
                self.game.curr_menu = self.game.personnage
            self.run_display = False


class Level(Menu):
    def __init__(self, game):
        pygame.init()
        Menu.__init__(self, game)
        self.state = 'Facile'
        self.unx, self.uny = self.mid_w, self.mid_h + 20
        self.deuxx, self.deuxy = self.mid_w, self.mid_h + 40
        self.troisx, self.troisy = self.mid_w, self.mid_h + 60
        self.cursor_rect.midtop = (self.unx + self.offset, self.uny)
        self.niveaux = 8  # niveau par défault si on ne choisit pas la difficulté

    def display_menu(self):  # affiche le menu level
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Niveaux', 20, 250, 345)
            self.game.draw_text("Facile", 15, self.unx, self.uny)
            self.game.draw_text("Moyen", 15, self.deuxx, self.deuxy)
            self.game.draw_text("Difficile", 15, self.troisx, self.troisy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY:
            if self.state == 'Facile':
                self.state = 'Difficile'
                self.cursor_rect.midtop = (
                    self.troisx + self.offset, self.troisy)
            elif self.state == 'Moyen':
                self.state = 'Facile'
                self.cursor_rect.midtop = (self.unx + self.offset, self.uny)
            elif self.state == 'Difficile':
                self.state = 'Moyen'
                self.cursor_rect.midtop = (
                    self.deuxx + self.offset, self.deuxy)
        elif self.game.DOWN_KEY:
            if self.state == 'Moyen':
                self.state = 'Difficile'
                self.cursor_rect.midtop = (
                    self.troisx + self.offset, self.troisy)
            elif self.state == 'Difficile':
                self.state = 'Facile'
                self.cursor_rect.midtop = (self.unx + self.offset, self.uny)
            elif self.state == 'Facile':
                self.state = 'Moyen'
                self.cursor_rect.midtop = (
                    self.deuxx + self.offset, self.deuxy)
        elif self.game.START_KEY:
            if self.state == 'Facile':
                self.niveaux = 1
            elif self.state == 'Moyen':
                self.niveaux = 8
            elif self.state == 'Difficile':
                self.niveaux = 15
            self.game.curr_menu = self.game.main_menu
            self.run_display = False


class Personnage(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Premier'
        self.un_persox, self.un_persoy = self.mid_w, self.mid_h + 20
        self.deux_persox, self.deux_persoy = self.mid_w, self.mid_h + 40
        self.trois_persox, self.trois_persoy = self.mid_w, self.mid_h + 60
        self.cursor_rect.midtop = (
            self.un_persox + self.offset, self.un_persoy)
        self.perso = 0  # personnage par défault si on ne choisit pas la difficulté

    def display_menu(self):  # affiche le menu player
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Personnage', 20, 250, 345)
            self.game.draw_text("Premier", 15, self.un_persox, self.un_persoy)
            self.game.draw_text(
                "Deuxieme", 15, self.deux_persox, self.deux_persoy)
            self.game.draw_text(
                "Troisieme", 15, self.trois_persox, self.trois_persoy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY:
            if self.state == 'Premier':
                self.state = 'Troisième'
                self.cursor_rect.midtop = (
                    self.trois_persox + self.offset, self.trois_persoy)
            elif self.state == 'Deuxième':
                self.state = 'Premier'
                self.cursor_rect.midtop = (
                    self.un_persox + self.offset, self.un_persoy)
            elif self.state == 'Troisième':
                self.state = 'Deuxième'
                self.cursor_rect.midtop = (
                    self.deux_persox + self.offset, self.deux_persoy)
        elif self.game.DOWN_KEY:
            if self.state == 'Deuxième':
                self.state = 'Troisième'
                self.cursor_rect.midtop = (
                    self.trois_persox + self.offset, self.trois_persoy)
            elif self.state == 'Troisième':
                self.state = 'Premier'
                self.cursor_rect.midtop = (
                    self.un_persox + self.offset, self.un_persoy)
            elif self.state == 'Premier':
                self.state = 'Deuxième'
                self.cursor_rect.midtop = (
                    self.deux_persox + self.offset, self.deux_persoy)
        elif self.game.START_KEY:
            if self.state == 'Premier':
                self.perso = 0
            elif self.state == 'Deuxième':
                self.perso = 1
            elif self.state == 'Troisième':
                self.perso = 2
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
