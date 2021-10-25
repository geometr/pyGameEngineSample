import World
import pygame
from pygame.locals import *

class Game:
    FPS = 0
    running = True

    def __init__(self):
        self.world = World.World()
        self.clock = pygame.time.Clock()
        self.mainLoop()

    def mainLoop(self):
        while self.running:
            self.make_step = False
            self.inputPlayer()
            if self.make_step:
                self.update()
            self.render()
            self.clock.tick(self.FPS)

    def render(self):
        self.world.render(self.clock)

    def update(self):
        self.world.tick()

    def inputPlayer(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.running = False
                if event.key == pygame.K_n:
                    self.make_step = True

game = Game()
