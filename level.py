import pygame
from bag import Bag
from ui import UI
from random import randint


class Level:
    def __init__(self, screen):

        self.screen = screen

        self.bag = Bag(self.screen.get_width() // 2 - 16, self.screen.get_height() // 2 - 32, 32, 64)
        self.ui = UI(self.screen)

        self.wins_surface_size = randint(50, 300)
        self.win_surface = pygame.surface.Surface((self.wins_surface_size, self.wins_surface_size))
        self.win_surface.set_alpha(100)
        self.win_surface_pos = (randint(0, self.screen.get_width() - self.wins_surface_size), randint(0, self.screen.get_height() - self.wins_surface_size))
        self.stop = False

    def draw(self, surface):
        self.bag.draw(surface)
        self.ui.draw(self.bag.collisions, self.win_surface.get_rect(topleft=self.win_surface_pos))
        self.screen.blit(self.win_surface, self.win_surface_pos)

    def update(self, dt):
        if self.stop:
            self.bag.update(dt, self.win_surface.get_rect(topleft=self.win_surface_pos))

        self.ui.update(dt, self.stop)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.stop = not self.stop
                if self.stop:
                    self.ui.score = int(abs(self.ui.strong_height - self.ui.dynamometer_surface.get_height()))

                    self.bag.set_acceleration(self.ui.score)
                    #self.bag.set_random_direction()
                    self.bag.set_mouse_direction(pygame.mouse.get_pos())

        self.ui.handle_events(event)
