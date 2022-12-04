import pygame
import pytmx
import pyscroll
from dataclasses import dataclass


@dataclass  # pas besoin de init car dataclass importe les éléments
class Map:
    name: str
    walls: list
    group: pyscroll.PyscrollGroup
    tmx_data: pytmx.TiledMap


class MapManager:

    def __init__(self, screen, player, car, car_num):
        self.maps = dict()
        self.screen = screen
        self.current_map = "map_level_1"

        # on génère le joueur et on initialise sa position
        self.player = player
        self.car = car
        self.car_num = car_num

        # on initialise pour chaque véhicule le point de départ et le point cible

        self.points = []
        self.current_point = [0 for i in range(car_num)]
        self.target_point = [0 for i in range(car_num)]

        for num in range(self.car_num):
            self.points.append([])
            self.current_point[num] = 0
            self.target_point[num] = 1

        # on appelle notre map générée depuis Tiled

        self.register_map("map_level_1", car_num)

        for num in range(self.car_num):
            self.load_points(num)

        self.teleport_player("spawn_player")  # teleporte le joueur
        self.teleport_all_cars(self.car_num)  # teleport toutes les voitures

    def move(self, car_num):  # déplace les vehicules

        for num in range(car_num):

            current_rect = self.points[num][self.current_point[num]]
            target_rect = self.points[num][self.target_point[num]]

            if current_rect.x > target_rect.x and abs(current_rect.y-target_rect.y) < 30:
                self.car[num].move_left()

            elif current_rect.x < target_rect.x and abs(current_rect.y-target_rect.y) < 30:
                self.car[num].move_right()

            if self.car[num].rect.colliderect(target_rect):
                self.current_point[num], self.target_point[num] = self.target_point[num], self.current_point[num]
                self.car[num].rotate(180)

    def teleport_player(self, name):
        point = self.get_object(name)
        self.player.position[0] = point.x
        self.player.position[1] = point.y
        # pour éviter problème de téléportiation infinie si collision
        self.player.save_location()

    def teleport_car(self, num):
        point = self.get_object(f'car{num}_path0')
        self.car[num].position[0] = point.x
        self.car[num].position[1] = point.y
        # pour éviter problème de téléportiation infinie si collision
        self.car[num].save_location()

    def teleport_all_cars(self, car_num):
        for num in range(car_num):
            self.teleport_car(num)

    def check_collision(self):
        # verification  de collision
        for sprite in self.get_group().sprites():
            if sprite.feet.collidelist(self.get_walls()) > -1:
                sprite.move_back()

    def register_map(self, name, car_num):
        tmx_data = pytmx.util_pygame.load_pygame(
            f'graphic/map/{name}.tmx')

        map_data = pyscroll.data.TiledMapData(tmx_data)

        map_layer = pyscroll.orthographic.BufferedRenderer(
            map_data, self.screen.get_size())

        map_layer.zoom = 1

        # on génère le joueur et on initialise sa position

        # on définit une liste qui va stocker les rect de collision
        walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                walls.append(pygame.Rect(
                    obj.x, obj.y, obj.width, obj.height))

        # on definit une liste qui va stocker les endroits ou le joueur meurt
        self.dead = []

        for obj in tmx_data.objects:
            if obj.type == "DEAD":
                self.dead.append(pygame.Rect(
                    obj.x, obj.y, obj.width, obj.height))

        # on definit une liste contenant l'endroit ou le joueur gagne
        self.win = []

        for obj in tmx_data.objects:
            if obj.type == "WIN":
                self.win.append(pygame.Rect(
                    obj.x, obj.y, obj.width, obj.height
                ))

        # dessiner le groupe de calque
        group = pyscroll.PyscrollGroup(
            map_layer=map_layer, default_layer=3)
        group.add(self.player)

        for num in range(car_num):
            group.add(self.car[num])

        # créer un objet map
        self.maps[name] = Map(name, walls, group, tmx_data)

    def load_points(self, num):
        point1 = self.get_object(f'car{num}_path0')
        point2 = self.get_object(f'car{num}_path1')
        rect1 = pygame.Rect(point1.x, point1.y, point1.width, point1.height)
        rect2 = pygame.Rect(point2.x, point2.y, point2.width, point2.height)
        self.points[num].append(rect1)
        self.points[num].append(rect2)

    def get_map(self): return self.maps[self.current_map]

    def get_group(self): return self.get_map().group

    def get_walls(self): return self.get_map().walls

    def get_object(self, name): return self.get_map(
    ).tmx_data.get_object_by_name(name)

    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)

    def update(self):
        self.get_group().update()
