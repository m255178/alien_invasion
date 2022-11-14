import sys
import pygame

from settings import Settings

from raindrop import Raindrop

from random import randint


class Rocketgame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.raindrops = pygame.sprite.Group()
        pygame.display.set_caption("Raindrops")

        self._create_raindrops()

    def run_game(self):
        """Start the main loop for the game."""
        while True:

            self._update_screen()


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)

        pygame.display.flip()


    def _update_raindrops(self):
        self._check_raindrops_edges()
        self.raindrops.update()
    def _create_raindrops(self):
        raindrop = Raindrop(self)
        raindrop_width = raindrop.rect.width
        available_space_x = self.settings.screen_width - (2*raindrop_width)
        number_raindrops_x = available_space_x // (2*raindrop_width)

        for raindrop_number in range(number_raindrops_x):
            self._create_raindrop(raindrop_number)

    def _create_raindrop(self, raindrop_number):
        raindrop = Raindrop(self)
        raindrop_width = raindrop.rect.width
        raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
        raindrop.rect.x = raindrop.x
        self.raindrops.add(raindrop)


    def _change_raindrops_direction(self):
        for raindrop in self.raindrops.sprites():
            raindrop.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_raindrops_edges(self):
        for raindrop in self.raindrops.sprites():
            if alien.check_edges():
                self._change_raindrops_direction()
                break












if __name__ == '__main__':
    ai = Rocketgame()
    ai.run_game()
