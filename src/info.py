import pygame

class Info(pygame.sprite.Sprite):
    def __init__(self):
        self.quests_done = 0
        self.info = pygame.image.load('./assets/text/info.png')
        self.info = pygame.transform.scale(self.info, (220, 120))
        self.text = str(self.quests_done) + "/2 quests done !"
        self.font = pygame.font.SysFont("Helvetica", 15, bold=True)
    
    def render(self, screen):
        screen.blit(self.info, (0, 0))
        text = self.font.render(self.text, False, (255, 255, 255))
        screen.blit(text, (40, 45))
    
    def update_quests_done(self, screen):
        self.quests_done += 1
        self.text = str(self.quests_done) + "/2 quests done !"
        text = self.font.render(self.text, False, (255, 255, 255))
        screen.blit(text, (470, 450))