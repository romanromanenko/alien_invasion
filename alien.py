import pygame
from pygame.sprite import Sprite
class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.pick = pygame.image.load('images/alian.webp')
        self.image = pygame.transform.scale(self.pick, (50, 50))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)