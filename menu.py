import pygame

class Menu:
    def __init__(self, screen, player_1, player_2):
        self.screen = screen
        self.running = True
        self.player_1 = player_1
        self.player_2 = player_2
        self.images  = [
            pygame.transform.scale(pygame.image.load("./assets/family/daughter.png").convert_alpha(), (120, 120)),
            pygame.transform.scale(pygame.image.load("./assets/family/father.png").convert_alpha(),   (120, 120)),
            pygame.transform.scale(pygame.image.load("./assets/family/mother.png").convert_alpha(),   (120, 120)),
            pygame.transform.scale(pygame.image.load("./assets/family/son.png").convert_alpha(),      (120, 120))]
        #self.menu(pygame.time.Clock(), False)

    def draw_text(self, text, menu_font, color, surface, x, y):
        textobj = menu_font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def menu(self, clock, ingame):
        menu_font = pygame.font.SysFont("comicsansms", 60)
        button_font = pygame.font.SysFont("comicsansms", 35)
        #menu_text = menu_font.render('Menu' , True , (255, 255, 255))
        button_1_text = button_font.render('Play' if ingame else 'Resume' , True , (255, 255, 255))
        button_2_text = button_font.render('Quit' , True , (255, 255, 255))
        menu_loop = True
        click = False
        while menu_loop:
            # Récupérer les touches du clavier
            pressed = pygame.key.get_pressed()

            # Initialisation du fond de l'écran
            width, height = self.screen.get_size()
            mx, my = pygame.mouse.get_pos()
            self.screen.fill((122, 91, 225))
            self.draw_text('Menu', menu_font, (255, 255, 255), self.screen, width/2-100, 20)

            # Boutons Play/Resume et Quit
            button_1 = pygame.Rect(70, 230, 200, 50)
            button_2 = pygame.Rect(70, 350, 200, 50)
            pygame.draw.rect(self.screen, (77, 146, 98), button_1, 25, border_radius=17)
            pygame.draw.rect(self.screen, (77, 146, 98), button_2, 25, border_radius=17)
            if button_1.collidepoint((mx, my)):
                pygame.draw.rect(self.screen, (122, 176, 85), button_1, 25, border_radius=17)
                if click:
                    menu_loop = False
            if button_2.collidepoint((mx, my)):
                pygame.draw.rect(self.screen, (122, 176, 85), button_2, 25, border_radius=17)
                if click:
                    menu_loop = False
                    self.running = False
            self.screen.blit(button_1_text, (130, 230)  if ingame else (110, 230))
            self.screen.blit(button_2_text, (130, 350))

            # Ligne pour relier les personnages (arbre généalogique)
            pygame.draw.line(self.screen, (255, 255, 255), [510, 275], [660, 275], 7)
            pygame.draw.line(self.screen, (255, 255, 255), [585, 275], [585, 370], 7)
            pygame.draw.line(self.screen, (255, 255, 255), [510, 370], [660, 370], 7)
            pygame.draw.line(self.screen, (255, 255, 255), [510, 367], [510, 500], 7)
            pygame.draw.line(self.screen, (255, 255, 255), [660, 367], [660, 500], 7)

            # Photos des personnages choix des personnages
            self.screen.blit(self.images[1], (450, 200)) # Father
            self.screen.blit(self.images[2], (600, 200)) # Mother
            self.screen.blit(self.images[0], (450, 400)) # Daughter
            self.screen.blit(self.images[3], (600, 400)) # Son


            # Boucle du menu
            for event in pygame.event.get():
                # Que faire si on clique sur la croix pour fermer la fenêtre
                if event.type == pygame.QUIT:
                    menu_loop = False
                    self.running = False
                # Actionner le clique de la souris
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            # Actualisation de l'affichage
            pygame.display.update()
            clock.tick(60)
        return self.running, self.player_1, self.player_2