import sys
import pygame

class AlienInvasion:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.bg_immage = pygame.image.load('images/background.webp')

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    sys.exit()

            self.screen.blit(self.bg_immage, (0, 0))

            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()