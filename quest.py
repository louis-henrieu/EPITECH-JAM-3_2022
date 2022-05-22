import pygame

class Quest(pygame.sprite.Sprite):
    X_POS = 35
    Y_POS = 320

    def __init__(self):
        self.quest = pygame.image.load('quest.png')
        self.quest = pygame.transform.scale(self.quest, (700, 350))
        self.texts = ["Trouvez Sasha en réalisant 3 défis !", "1) Trouvez chacun 1 donut pour Sasha.", "2) Resolvez l'énigme de la maison de Sasha !"]
        self.text_idx = 0
        self.ltr_idx = 0
        self.font = pygame.font.SysFont("symbola", 23)
        self.reading = True

    def render(self, screen):
        if self.reading:
            self.ltr_idx += 1
            if self.ltr_idx >= len(self.texts[self.text_idx]):
                self.ltr_idx = self.ltr_idx
            screen.blit(self.quest, (self.X_POS, self.Y_POS))
            texts = self.font.render(self.texts[self.text_idx][0:self.ltr_idx], False, (255, 255, 255))
            screen.blit(texts, (self.X_POS + 110, self.Y_POS + 200))
    
    def next_text(self):
        self.text_idx += 1
        self.ltr_idx = 0

        if self.text_idx >= len(self.texts):
            self.reading = False