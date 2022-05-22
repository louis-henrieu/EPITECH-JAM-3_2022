import pygame
import pytmx
import pyscroll

from pygame import mixer
from src.player import Player, Player2
from src.menu import Menu
from src.info import Info
from src.quest import Quest
from src.talk_box import TalkBox
from src.my_map import MapManager

class Game:
    def __init__(self):
        # Démarrage
        self.running = True

        # Affichage de la fenêtre
        self.screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
        pygame.display.set_caption("Family Reunion")

        # Charger la musique
        #mixer.music.load('../assets/music/simpson.mp3')
        #mixer.music.play(-1)

        # Choix du personnage
        self.player_1 = True # Dad (true) / Mom (false)
        self.player_2 = True # Son (true) / Daughter (false)
#
        self.myMenu = Menu(self.screen, self.player_1, self.player_2)
        self.running, self.player_1, self.player_2 = self.myMenu.menu(True)

        # Générer le joeur
        self.player = Player(0, 0, self.player_1)

        self.player2 = Player2(0, 0, self.player_2)

        # Afficher la box avec les informations
        self.info = Info()
        self.quest = Quest()
        self.talk_box = TalkBox()
        self.map_manager = MapManager(self.screen, self.player, self.player2)

        # Définir le logo du jeu
        pygame.display.set_icon(self.player.get())
        pygame.display.set_icon(self.player2.get())

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

    def update(self):
        self.map_manager.update()

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
            self.map_manager.draw()
            self.quest.render(self.screen)
            if (self.map_manager.current_map == "house"):
                self.talk_box.render(self.screen)
        
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
