import pygame

class Win:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.images  = [
            pygame.transform.scale(pygame.image.load("./assets/family/daughter.png").convert_alpha(), (120, 120)),
            pygame.transform.scale(pygame.image.load("./assets/family/father.png").convert_alpha(),   (120, 120)),
            pygame.transform.scale(pygame.image.load("./assets/family/mother.png").convert_alpha(),   (120, 120)),
            pygame.transform.scale(pygame.image.load("./assets/family/son.png").convert_alpha(),      (120, 120)),
            pygame.transform.scale(pygame.image.load("./map/baby.png").convert_alpha(),   (250, 250))]

    def draw_text(self, text, menu_font, color, surface, x, y):
        textobj = menu_font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def win(self, ingame):
        clock = pygame.time.Clock()
        menu_font = pygame.font.SysFont("symbola", 50)
        button_font = pygame.font.SysFont("symbola", 60)
        choose_font = pygame.font.SysFont("symbola", 40)
        name_font = pygame.font.SysFont("symbola", 25)
        #menu_font = pygame.font.SysFont("symbola", 80)
        #button_font = pygame.font.SysFont("symbola", 40)
        #choose_font = pygame.font.SysFont("symbola", 25)
        #name_font = pygame.font.SysFont("symbola", 15)
        #menu_text = menu_font.render('Menu' , True , (255, 255, 255))
       # button_1_text = button_font.render('Play', True , (255, 255, 255))
        button_2_text = button_font.render('Quitter' , True , (255, 255, 255))
        choose_text = choose_font.render('Choisis ta famille' , True , (255, 255, 255))
        name_text = [
            name_font.render('Petrik (le père)' , True , (255, 255, 255)),
            name_font.render('Yuyu (la mère)' , True , (255, 255, 255)),
            name_font.render('Mattéo (le fils)' , True , (255, 255, 255)),
            name_font.render('Lise (la fille)' , True , (255, 255, 255))]
        menu_loop = True
        click = False
        while menu_loop:
            # Récupérer les touches du clavier
            pressed = pygame.key.get_pressed()

            # Initialisation du fond de l'écran
            width, height = self.screen.get_size()
            mx, my = pygame.mouse.get_pos()
            self.screen.fill((122, 91, 225))
            self.draw_text('Bravo la famille est rassemblée !', menu_font, (255, 255, 255), self.screen, width/2-250, 20)
            self.draw_text('Vous avez trouvé Sasha et elle a bien mangé les donuts !', choose_font, (255, 255, 255), self.screen, width/2-370, 70)
            # Boutons Play/Resume et Quit
            #button_1 = pygame.Rect(70, 230, 200, 50)
            button_2 = pygame.Rect(70, 500, 200, 50)
           # pygame.draw.rect(self.screen, (77, 146, 98), button_1, 25, border_radius=17)
            pygame.draw.rect(self.screen, (191, 35, 35), button_2, 25, border_radius=17)
           # if button_1.collidepoint((mx, my)):
           #     pygame.draw.rect(self.screen, (122, 176, 85), button_1, 25, border_radius=17)
           #     if click:
           #         menu_loop = False
            if button_2.collidepoint((mx, my)):
                pygame.draw.rect(self.screen, (209, 38, 38), button_2, 25, border_radius=17)
                if click:
                    menu_loop = False
                    self.running = False
            #self.screen.blit(button_1_text, (130, 235)  if ingame else (90, 235))
            self.screen.blit(button_2_text, (95, 505))
            #self.screen.blit(choose_text, (500, 150))

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
            self.screen.blit(self.images[4], (100, 200)) # Son
            self.screen.blit(name_text[0], (450, 325)) # Father
            self.screen.blit(name_text[1], (600, 325)) # Mother
            self.screen.blit(name_text[3], (450, 525)) # Daughter
            self.screen.blit(name_text[2], (600, 525)) # Son

        
            # Choix des personnages
            father_rect = pygame.Rect(448, 198, 122, 125)
            mother_rect = pygame.Rect(598, 198, 122, 125)
            daughter_rect = pygame.Rect(448, 398, 122, 125)
            son_rect = pygame.Rect(598, 398, 122, 125)

            # Boucle du menu
            click = False
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
        return self.running