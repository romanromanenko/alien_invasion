import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (
                self.settings.screen_width,
                self.settings.screen_height
            ),
            #pygame.FULLSCREEN # uncomment for full screen displaying
        )
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _upgrade_screen(self):
        self.screen.blit(self.settings.bg_immage, (0, 0))
        self.ship.blitme()

        pygame.display.flip()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._upgrade_screen()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()