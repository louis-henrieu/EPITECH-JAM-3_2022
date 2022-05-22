import pygame

class TalkBox(pygame.sprite.Sprite):
    X_POS = 250
    Y_POS = 117
    def __init__(self):
        self.text = "Mon premier est une note de musique"
        self.text1 = "Mon deuxième est la partie intérieure du pain"
        self.text2 = "Grâce à mon troisième je te vois"
        self.text3 = "Mon tout est le plus important dans la vie!"
        self.font = pygame.font.SysFont("Helvetica", 15, bold = "True")
    
    def render(self, screen):
        text = self.font.render(self.text, False, (255, 11, 51))
        screen.blit(text, (self.X_POS - 30, self.Y_POS - 95))
        text1 = self.font.render(self.text1, False, (255, 11, 51))
        screen.blit(text1, (self.X_POS - 30, self.Y_POS - 80))
        text2 = self.font.render(self.text2, False, (255, 11, 51))
        screen.blit(text2, (self.X_POS - 30, self.Y_POS - 65))
        text3 = self.font.render(self.text3, False, (255, 11, 51))
        screen.blit(text3, (self.X_POS - 30, self.Y_POS - 50))