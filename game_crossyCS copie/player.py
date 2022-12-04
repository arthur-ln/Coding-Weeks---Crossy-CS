import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, number):  # initie ses composants
        super().__init__()  # initie sa classe
        self.sprite_sheet = pygame.image.load(
            f'graphic/players/player{number}.png')
        self.image = self.get_image(0, 0)
        self.adapt_color(number)
        self.rect = self.image.get_rect()  # position en rectangle
        self.position = [x, y]
        self.velocity = 32
        self.rect.x = 200
        self.rect.y = 600
        self.images = {
            'down': self.get_image(0, 0),
            'left': self.get_image(0, 32),
            'right': self.get_image(0, 64),
            'up': self.get_image(0, 96)
        }
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()

    def adapt_color(self, number):
        if number == 1:
            self.image.set_colorkey([120, 195, 128])
        elif number == 0:
            self.image.set_colorkey([0, 0, 0])
        elif number == 2:
            self.image.set_colorkey([255, 255, 255])

    def save_location(self): self.old_position = self.position.copy()

    def change_animation(self, name):
        self.image = self.images[name]
        self.image.set_colorkey([120, 195, 128])

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def get_image(self, x, y):  # pour selectionner l'image du jouer que l'on souhaite
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image

    def move_right(self):
        self.position[0] += self.velocity

    def move_left(self): self.position[0] -= self.velocity

    def move_up(self): self.position[1] -= self.velocity

    def move_down(self): self.position[1] += self.velocity
