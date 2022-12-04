import pygame


class Car(pygame.sprite.Sprite):

    def __init__(self, x, y, number, velocity):
        super().__init__()
        self.image = pygame.image.load(f'graphic/cars/car_{number}.png')
        self.image = pygame.transform.scale(
            self.image, (25, 25))  # on redimensionne les voituresÒ
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.velocity = velocity
        self.rect.x = 200
        self.rect.y = 600
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
        self.angle = 90
        self.rotate(90)  # pour avoir les voitures dans le sens de la longueur

    def save_location(self): self.old_position = self.position.copy()

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_right(self): self.position[0] += self.velocity

    def move_left(self): self.position[0] -= self.velocity

    def rotate(self, angle):
        self.image = pygame.transform.rotozoom(self.image, angle, 1)
