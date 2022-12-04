import pygame
import sys
import random
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((500, 750))
pygame.display.set_caption('Jeu CrossyCS')
clock = pygame.time.Clock()


poulet = pygame.Surface((50, 50))
poulet.fill('White')

position = [250, 525]

poulet_rect = poulet.get_rect(topleft=(position[0], position[1]))


def del_cars(liste):
    for el in liste:
        if el.centerx <= -100:
            liste.remove(el)
    return liste


crash_sound = pygame.mixer.Sound(
    'sounds/crashsound.wav')
jump_sound = pygame.mixer.Sound(
    'sounds/jumpsound.wav')
mixer.music.load('sounds//bgsound.wav')
mixer.music.play(-1)

road_surface = pygame.image.load(
    'graphic/mvp/route1voie.png')
road_surface = pygame.transform.scale(road_surface, (500, 50))

grass_surface = pygame.image.load(
    'graphic/mvp/herbe.png')
grass_surface = pygame.transform.scale(grass_surface, (500, 50))


def new_road():
    new_road = road_surface.get_rect(topleft=(0, -50))
    return new_road


def new_grass():
    new_grass = grass_surface.get_rect(topleft=(0, -50))
    return new_grass


speed = 50

liste_décor = []
for i in range(15):
    liste_décor.append(
        [grass_surface, grass_surface.get_rect(topleft=(0, i*50))])


def add_line(liste):
    a = random.random()
    if a < 0.5:
        liste.append([road_surface, new_road()])
    else:
        liste.append([grass_surface, new_grass()])
    return liste


def move_lines(liste):  # type de la liste : rectangle
    for line in liste:
        line[1].centery += 50


def draw_lines(liste):
    for line in liste:
        screen.blit(line[0], line[1])


list_cars = []


# mouvement de la voiture selon x opéré à chaque tour de boucle de jeu
def move_cars_x(list_cars):
    for car in list_cars:
        car.centerx -= 5
    return list_cars


def move_cars_y(list_cars):
    for car in list_cars:
        car.centery += 50
    return list_cars


# créer la liste de voiture
car = pygame.Surface((50, 50))
car.fill('Red')


def create_cars(liste, list_cars):
    pos_list = [550, 600, 500, 650, 700]
    for el in liste:
        if el[0] == road_surface:
            list_cars.append(car.get_rect(
                center=(random.choice(pos_list), el[1].centery)))
    return list_cars


def draw_cars(liste):
    for el in liste:
        screen.blit(car, el)


def check_collision(list_cars, score):
    for el in list_cars:
        if poulet_rect.colliderect(el):
            crash_sound.play()
            score = 0
    return score


game_font = pygame.font.Font(
    'graphic/police/04B_19.TTF', 40)

score = 0


def score_display():
    score_surface = game_font.render(
        f'Score : {score} ', True, (255, 255, 255))
    score_rect = score_surface.get_rect(center=(250, 50))
    screen.blit(score_surface, score_rect)


SPAWNCAR = pygame.USEREVENT
pygame.time.set_timer(SPAWNCAR, 1200)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            jump_sound.play()
            if event.key == pygame.K_RIGHT:
                position[0] += speed
            elif event.key == pygame.K_LEFT:
                position[0] -= speed
            elif event.key == pygame.K_UP:
                add_line(liste_décor)
                move_lines(liste_décor)
                move_cars_y(list_cars)
                score += 1

        if event.type == SPAWNCAR:
            create_cars(liste_décor, list_cars)

    draw_lines(liste_décor)
    list_cars = move_cars_x(list_cars)
    draw_cars(list_cars)
    check_collision(list_cars, score)

    poulet_rect.centerx = position[0]
    poulet_rect.centery = position[1]

    del_cars(list_cars)

    screen.blit(poulet, poulet_rect)

    score_display()

    pygame.display.update()

    clock.tick(60)
