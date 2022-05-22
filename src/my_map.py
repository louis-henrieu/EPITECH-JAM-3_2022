import pygame, pytmx, pyscroll
from dataclasses import dataclass
from typing import List
from src.info import Info
from src.win import Win

@dataclass
class Portal:
    from_world: str
    origin_point: str
    target_world: str
    teleport_point: str

@dataclass
class Map:
    name: str
    walls: List[pygame.Rect]
    group: pyscroll.PyscrollGroup
    tmx_data: pytmx.TiledMap
    portals: List[Portal]

class MapManager:
    donut_nb = 0
    donut_nb1 = 0

    def __init__(self, screen, player, player2):
        self.maps = dict()
        self.screen = screen
        self.player = player
        self.player2 = player2
        self.current_map = "world"

        self.info = Info()

        self.register_map("world", portals=[
            Portal(from_world="world", origin_point="enter_house",
            target_world="house", teleport_point="spawn_house")
        ])
        self.register_map("house", portals=[
            Portal(from_world="house", origin_point="exit_house",
            target_world="world", teleport_point="enter_house_exit")
        ])

        self.teleport_player("player_1")
        self.teleport_player("player_2")

        donut1 = self.get_object("donut_1")
        self.rect1 = pygame.Rect(donut1.x, donut1.y, donut1.width, donut1.height)
        donut2 = self.get_object("donut_2")
        self.rect2 = pygame.Rect(donut2.x, donut2.y, donut2.width, donut2.height)
        self.myWin = Win(self.screen)
    
    def display_donut(self):
        if self.donut_nb == 1 and self.donut_nb1 == 1:
            my_font = pygame.font.SysFont('symbola', 30, bold=True)
            text_surface = my_font.render("2/2 donuts! Bravo!", False,(3,37,126))
            self.screen.blit(text_surface, (450, 450))
            pygame.display.flip()
            pygame.event.pump()
            pygame.time.delay(1000)
            self.info.update_quests_done(self.screen)
        elif self.donut_nb == 1 or self.donut_nb1 == 1:
            my_font = pygame.font.SysFont('symbola', 30, bold=True)
            text_surface = my_font.render("1/2 donuts trouvés", False, (3,37,126))
            self.screen.blit(text_surface, (470, 450))
            pygame.display.flip()
            pygame.event.pump()
            pygame.time.delay(1000)
    
    def check_collision(self):
        running = True
        #Vérifier si portails
        for portal in self.get_map().portals:
            if portal.from_world == self.current_map:
                point = self.get_object(portal.origin_point)
                rect = pygame.Rect(point.x, point.y, point.width, point.height)
            
            if self.player.feet.colliderect(rect) or self.player2.feet.colliderect(rect):#and self.player2.feet.colliderect(rect) and self.donut_nb == 1 and self.donut_nb1 == 1:
                copy_portal = portal
                self.current_map = portal.target_world
                self.teleport_player(copy_portal.teleport_point)
        
        #Vérifier si donut
        if self.player.feet.colliderect(self.rect1) and self.donut_nb != 1:
            self.donut_nb = 1
            self.display_donut()
        if self.player2.feet.colliderect(self.rect2) and self.donut_nb1 != 1:
            self.donut_nb1 = 1
            self.display_donut()
        if self.current_map == "house":
            self.baby = self.get_object("baby")
            self.rectbaby = pygame.Rect(self.baby.x, self.baby.y, self.baby.width, self.baby.height)
            if (self.player.feet.colliderect(self.rectbaby) or self.player2.feet.colliderect(self.rectbaby)):
                self.myWin.win(False)
                running = False


        #Vérifier si collision
        for sprite in self.get_group().sprites():
            if sprite.feet.collidelist(self.get_walls()) > -1:
                sprite.move_back()
        return running

    def teleport_player(self, name):
        point = self.get_object(name)
        self.player.position[0] = point.x
        self.player.position[1] = point.y
        self.player2.position[0] = point.x
        self.player2.position[1] = point.y
        self.player.save_location()
        self.player2.save_location()
    
    def register_map(self, name, portals=[]):
        # Charger la carte clasique
        tmx_data = pytmx.util_pygame.load_pygame(f"./map/{name}.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Les collisions
        walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner les différents calques
        group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        group.add(self.player)
        group.add(self.player2)

        #Créer l'objet map
        self.maps[name] = Map(name, walls, group, tmx_data, portals)

    def get_map(self):
        return self.maps[self.current_map]
    
    def get_group(self):
        return self.get_map().group

    def get_walls(self):
        return self.get_map().walls
    
    def get_object(self, name):
        return self.get_map().tmx_data.get_object_by_name(name)

    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)
        self.get_group().center(self.player2.rect.center)
        self.info.render(self.screen)
    
    def update(self):
        self.get_group().update()
        return self.check_collision()