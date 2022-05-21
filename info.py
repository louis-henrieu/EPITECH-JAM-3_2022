import pygame

class Info(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 0
        self.info = pygame.image.load('info.png')
        self.info = pygame.transform.scale(self.info, (220, 120))
        self.text = str(self.x) + "/3 quests done !"
        self.font = pygame.font.SysFont("Helvetica", 15, bold=True)
    
    def render(self, screen):
        screen.blit(self.info, (0, 0))
        text = self.font.render(self.text, False, (255, 255, 255))
        screen.blit(text, (40, 45))