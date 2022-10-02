import pygame
from colors import *
from level import Level


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Punch")
        self.clock = pygame.time.Clock()
        self.running = True

        self.level = Level(self.screen)

    def run(self):
        while self.running:
            self.clock.tick(60)
            dt = self.clock.get_time() / 1000
            self.events()
            self.update(dt)
            self.draw(self.screen)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    pygame.quit()
                    exit()
            self.level.handle_event(event)

    def update(self, dt):
        self.level.update(dt)
        pygame.display.update()

    def draw(self, surface):
        self.screen.fill(DARK_PURPLE)
        self.level.draw(surface)



if __name__ == '__main__':
    game = Game()
    game.run()
