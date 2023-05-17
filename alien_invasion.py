import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width,
            self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def _check_events(self):
        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()

    def _upgrade_screen(self):
        self.screen.blit(self.settings.bg_immage, (0, 0))
        self.ship.blitme()

        pygame.display.flip()

    def run_game(self):
        while True:
            self._check_events()
            self._upgrade_screen()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()