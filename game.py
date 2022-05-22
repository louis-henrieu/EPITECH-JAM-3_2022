import pygame
import pytmx
import pyscroll

from pygame import mixer
from player import Player, Player2
from menu import Menu
from info import Info
from quest import Quest

class Game:
    donut_nb = 0
    donut_nb1 = 0

    def __init__(self):
        # Démarrage
        self.running = True
        self.map = "world"

        # Affichage de la fenêtre
        self.screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
        pygame.display.set_caption("Family Reunion")

        # Charger la carte clasique
        tmx_data = pytmx.util_pygame.load_pygame("./assets/map_config/carte.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Charger la musique
        #mixer.music.load('simpson.mp3')
        #mixer.music.play(-1)

        # Choix du personnage
        self.player_1 = True # Dad (true) / Mom (false)
        self.player_2 = True # Son (true) / Daughter (false)

        self.myMenu = Menu(self.screen, self.player_1, self.player_2)
        self.running, self.player_1, self.player_2 = self.myMenu.menu(True)

        # Générer le joeur
        player_position = tmx_data.get_object_by_name("player_1")
        self.player = Player(player_position.x, player_position.y, self.player_1)

        # Définir le logo du jeu
        pygame.display.set_icon(self.player.get())

        player_position2 = tmx_data.get_object_by_name("player_2")
        self.player2 = Player2(player_position2.x, player_position2.y, self.player_2)

        # Afficher la box avec les informations
        self.info = Info()
        self.quest = Quest()

        # Définir le logo du jeu
        pygame.display.set_icon(self.player2.get())


        # Les collisions
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner les différents calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)
        self.group.add(self.player2)

        # Porte de la maison
        enter_house = tmx_data.get_object_by_name("enter_house")
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

        # Définir les donuts
        donut1 = tmx_data.get_object_by_name("donut_1")
        self.donut1 = pygame.Rect(donut1.x, donut1.y, donut1.width, donut1.height)
        donut2 = tmx_data.get_object_by_name("donut_2")
        self.donut2 = pygame.Rect(donut2.x, donut2.y, donut2.width, donut2.height)

    def handle_input(self, pressed):

        if pressed[pygame.K_ESCAPE]:
            self.running = False
        elif pressed[pygame.K_UP]:
            self.player.move_player("up")
        elif pressed[pygame.K_DOWN]:
            self.player.move_player("down")
        elif pressed[pygame.K_RIGHT]:
            self.player.move_player("right")
        elif pressed[pygame.K_LEFT]:
            self.player.move_player("left")

    def handle_input2(self, pressed):

        if pressed[pygame.K_ESCAPE]:
            self.running = False
        elif pressed[pygame.K_q]:
            self.player2.move_player("up")
        elif pressed[pygame.K_z]:
            self.player2.move_player("down")
        elif pressed[pygame.K_d]:
            self.player2.move_player("right")
        elif pressed[pygame.K_s]:
            self.player2.move_player("left")

    # Display if donuts found
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

    def switch_house(self):
        self.map = "house"

        # Charger la carte clasique
        tmx_data = pytmx.util_pygame.load_pygame("./assets/map_config/house.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Les collisions
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner les différents calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)
        self.group.add(self.player2)

        # Porte de la maison
        enter_house = tmx_data.get_object_by_name("exit_house")
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

        # Intérieur
        spawn_house_point = tmx_data.get_object_by_name("spawn_house")
        self.player.position[0] = spawn_house_point.x
        self.player.position[1] = spawn_house_point.y - 20
        self.player2.position[0] = spawn_house_point.x
        self.player2.position[1] = spawn_house_point.y - 20

    def switch_world(self):
        self.map = "world"

        # Charger la carte clasique
        tmx_data = pytmx.util_pygame.load_pygame("./assets/map_config/carte.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Les collisions
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner les différents calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)
        self.group.add(self.player2)

        # Porte de la maison
        enter_house = tmx_data.get_object_by_name("enter_house")
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

        # Intérieur
        spawn_house_point = tmx_data.get_object_by_name("enter_house_exit")
        self.player.position[0] = spawn_house_point.x
        self.player.position[1] = spawn_house_point.y + 20
        self.player2.position[0] = spawn_house_point.x
        self.player2.position[1] = spawn_house_point.y + 20

    def update(self):
        self.group.update()

        # Vérifier l'entrer de la maison
        if self.map == "world" and self.player.feet.colliderect(self.enter_house_rect) and\
                        self.player2.feet.colliderect(self.enter_house_rect) and self.info.quests_done == 1:
            self.switch_house()
        if self.map == "house" and self.player.feet.colliderect(self.enter_house_rect) and self.player2.feet.colliderect(self.enter_house_rect):
            self.switch_world()
        if self.map == "world" and self.player.feet.colliderect(self.donut1) and self.donut_nb != 1:
            self.donut_nb = 1
            self.display_donut()
        if self.map == "world" and self.player2.feet.colliderect(self.donut2) and self.donut_nb1 != 1:
            self.donut_nb1 = 1
            self.display_donut()

        # Vérification des collisions
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()

    def run(self):
        clock = pygame.time.Clock()
        # Clock
        while self.running:

            # Récupérer les touches du clavier
            pressed = pygame.key.get_pressed()

            # Gestion des évènements
            self.player.save_location()
            self.player2.save_location()
            self.handle_input(pressed)
            self.handle_input2(pressed)
            self.update()
            self.group.center(self.player.rect.center)
            self.group.center(self.player2.rect.center)
            self.group.draw(self.screen)
            self.info.render(self.screen)
            self.quest.render(self.screen)
            pygame.display.flip()

            # Fermeture de la window grâce à la croix
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.quest.next_text()
            # Fermeture de la window grâce à la touche P
            if pressed[pygame.K_p]:
                self.running = False
            # Ouverture du menu grâce à la touche M
            if pressed[pygame.K_m]:
                self.running, self.player_1, self.player_2 = self.myMenu.menu(False)
            clock.tick(60)

        pygame.quit()
