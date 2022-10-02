import pygame
from colors import *


class UI:

    def __init__(self, screen):
        self.screen = screen
        self.learn_surface = pygame.surface.Surface((self.screen.get_width(), self.screen.get_height()))
        self.learn_surface.set_alpha(50)
        self.font = pygame.font.SysFont('Arial', 24)
        self.collision_font = pygame.font.SysFont('Arial', 12)

        self.dynamometer_surface = pygame.Surface((50, 100))
        self.dynamometer_surface.set_alpha(100)

        self.strong_height = 0

        self.speed = 300

        self.direction = 0

        self.score = 0

        self.blit_learn_surface = True

    def draw(self, collisions, win_rect_pos):
        self.dynamometer_surface.fill((0, 0, 0))
        pygame.draw.rect(self.dynamometer_surface, (MING), (0, self.strong_height, 50, 150))
        self.screen.blit(self.dynamometer_surface, (700, 400))

        # Draw the score and collisions
        text_score = self.font.render(str(self.score), True, (255, 255, 255))
        text_collisions = self.collision_font.render(str(collisions), True, (255, 255, 255))
        self.screen.blit(text_score, (self.screen.get_width() // 2 - text_score.get_width() / 2, self.screen.get_height() // 2 - text_score.get_height() / 2))
        self.screen.blit(text_collisions, (self.screen.get_width() // 2 - text_collisions.get_width() / 2, self.screen.get_height() // 2 - text_collisions.get_height() / 2 + 50))

        if self.blit_learn_surface:
            learn_text = self.font.render('Try to get here', True, (255, 255, 255))
            self.learn_surface.blit(learn_text, (win_rect_pos[0] + win_rect_pos[2] // 2 - learn_text.get_width() // 2, win_rect_pos[1] + win_rect_pos[3] // 2 - learn_text.get_height() // 2))
            self.screen.blit(self.learn_surface, (0, 0))

    def update(self, dt, stop=False):
        if not stop:

            if self.strong_height >= 100:
                self.direction = -1

            if self.strong_height <= 0:
                self.direction = 1
            self.strong_height += self.direction * self.speed * dt

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.blit_learn_surface = False
