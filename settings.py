import pygame

class Settings():

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_immage = pygame.image.load('images/background.webp')
        self.ship_speed = 3