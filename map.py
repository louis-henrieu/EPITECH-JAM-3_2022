import pygame
import pytmx
import pyscroll
from dataclasses import dataclass

class Map:
    name: str
    walls: list[pygame.Rect]
    group: pyscroll.PyscrollGroup

class MapManager:

    def __init__(self, screen, player1, player2):
        self.maps = dict()
        self.current_map = "carte"
        self.screen = screen
        self.player1 = player1
        self.player2 = player2

        self.register_map("carte")
        self.register_map("house")
        self.register_map("ender")

    def register(self, name):
        # Charger la carte clasique
        tmx_data = pytmx.util_pygame.load_pygame(f"./assets/map_config/{name}.tmx")
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
        group.add(self.player1)
        group.add(self.player2)

        #créer un objet map
        map = Map(name, walls, group)
        self.maps[name] = map
