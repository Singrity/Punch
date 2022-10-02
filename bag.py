import pygame
from pygame.math import Vector2
from colors import *
import random


class Bag:

    def __init__(self, x=0, y=0, width=32, height=32):
        self.screen = pygame.display.get_surface()
        self.rect = pygame.Rect(x, y, width, height)
        self.velocity = 0
        self.direction = Vector2(0, 0)

        self.reduce_acceleration_speed = 0.9
        self.acceleration = 0

        self.collisions = 0

        self.win = True

    def draw(self, screen):
        pygame.draw.circle(screen, (CHOCOLATE_WEB), self.rect.center, 16)
        # pygame.draw.line(screen, (255, 0, 0), self.rect.center, (self.rect.centerx + self.direction.x * 16, self.rect.centery + self.direction.y * 16), 2)

    def motion(self, dt):
        if self.acceleration > 0:
            self.acceleration -= self.reduce_acceleration_speed
        else:
            self.acceleration = 0
            self.direction = Vector2(0, 0)
        if self.direction != Vector2(0, 0):
            self.direction.normalize_ip()

        self.velocity = self.acceleration
        self.rect.centerx += self.velocity * self.direction.x * self.acceleration * dt
        self.rect.centery += self.velocity * self.direction.y * self.acceleration * dt

    def check_collisions(self, win_rect):
        if self.rect.right >= self.screen.get_width():
            self.rect.right = self.screen.get_width()
            self.direction.x = -self.direction.x
            self.collisions += 1
        if self.rect.left <= 0:
            self.rect.left = 0
            self.direction.x = -self.direction.x
            self.collisions += 1
        if self.rect.bottom >= self.screen.get_height():
            self.rect.bottom = self.screen.get_height()
            self.direction.y = -self.direction.y
            self.collisions += 1
        if self.rect.top <= 0:
            self.rect.top = 0
            self.direction.y = -self.direction.y
            self.collisions += 1

        if self.rect.colliderect(win_rect) and self.velocity == 0:
            print("win")

    def set_acceleration(self, score):
        self.acceleration = score
        print("set acceleration: ", self.acceleration)

    def set_random_direction(self):
        x = random.random()
        y = random.random()
        print(x, y)
        self.direction = Vector2(x, y)

    def set_mouse_direction(self, mouse_pos):
        self.direction = Vector2(mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery)

    def update(self, dt, win_rect):
        self.motion(dt)
        self.check_collisions(win_rect)
