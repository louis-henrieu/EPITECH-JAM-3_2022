import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, choose_p):
        super().__init__()
        self.sprite_sheet = pygame.image.load("sprites_family.png")
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.images = {
            "up": self.get_image(111, 99 if choose_p else 232),
            "down": self.get_image(111, 0 if choose_p else 132),
            "right": self.get_image(111, 66 if choose_p else 198),
            "left": self.get_image(111, 33 if choose_p else 165)
        }
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
        self.speed = 3

    def get(self):
        self.image = self.images["down"]
        self.image.set_colorkey([0, 0, 0])
        return self.image

    def save_location(self): self.old_position = self.position.copy()

    def move_player(self, type):
        self.image = self.images[type]
        self.image.set_colorkey([0, 0, 0])
        if type == "up":
            self.position[1] -= self.speed
        elif type == "down":
            self.position[1] += self.speed
        elif type == "right":
            self.position[0] += self.speed
        elif type == "left":
            self.position[0] -= self.speed

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.update()

    def get_image(self, x, y):
        image = pygame.Surface([21, 33])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 21, 33))
        return image

class Player2(pygame.sprite.Sprite):

    def __init__(self, x, y, choose_p):
        super().__init__()
        self.sprite_sheet = pygame.image.load("sprites_family.png")
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.images = {
            "up": self.get_image(44, 232 if choose_p else 99),
            "down": self.get_image(44, 132 if choose_p else 0),
            "right": self.get_image(44, 198 if choose_p else 66),
            "left": self.get_image(44, 165 if choose_p else 33)
        }
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
        self.speed = 3

    def get(self):
        self.image = self.images["down"]
        self.image.set_colorkey([0, 0, 0])
        return self.image

    def save_location(self): self.old_position = self.position.copy()

    def move_player(self, type):
        self.image = self.images[type]
        self.image.set_colorkey([0, 0, 0])
        if type == "up":
            self.position[1] -= self.speed
        elif type == "down":
            self.position[1] += self.speed
        elif type == "right":
            self.position[0] += self.speed
        elif type == "left":
            self.position[0] -= self.speed

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.update()

    def get_image(self, x, y):
        image = pygame.Surface([21, 33])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 21, 33))
        return image