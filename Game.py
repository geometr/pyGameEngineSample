import Menu

import World

import pygame


class Game:
    def __init__(self):

        self.main_menu = Menu.Menu()
        self.stage = self.main_menu.mainLoop()

        self.FPS = 0
        self.running = True
        self.world = World.World()
        self.clock = pygame.time.Clock()
        self.make_step = -1
        self.mainLoop()

    def mainLoop(self):
        if self.stage == "NEW_GAME":
            while self.running:
                self.inputPlayer()
                if self.make_step > 0:
                    self.update()
                self.render()
                self.clock.tick(self.FPS)
        elif self.stage == "EXIT_GAME":
            pygame.quit()

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
                    self.world.screen.fullscreen_render = True
                    self.render()


game = Game()
