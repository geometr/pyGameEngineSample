import World
import pygame
from pygame.locals import *

class Game:
    FPS = 0
    running = True
    make_step = -1
    def __init__(self):
        self.world = World.World()
        self.clock = pygame.time.Clock()
        self.mainLoop()
        self.make_step = -1

    def mainLoop(self):
        while self.running:
            self.inputPlayer()
            if self.make_step > 0:
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
                    self.make_step = -self.make_step
                if event.key == pygame.K_d:
                    self.world.screen.debug = -self.world.screen.debug
                    self.world.screen.fullscreen_render= True
                    self.render()
game = Game()
