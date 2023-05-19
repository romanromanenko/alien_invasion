import pygame

class Settings():

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_immage = pygame.image.load('images/background.webp')
        self.ship_speed = 3

        self.bullet_speed = 5
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (100, 0, 0)