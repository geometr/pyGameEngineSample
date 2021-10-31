import Screen

import pygame


class Menu:

    def __init__(self):
        self.FPS = 0
        self.cursor_position = 0
        self.screen = Screen.Screen()
        self.clock = pygame.time.Clock()
        self.screen.attach(self)
        self.stage = "MAIN_MENU"

    def notifyScreenRender(self, screen):
        if self.cursor_position == 0:
            self.screen.writeText("> Start new game <")
        else:
            self.screen.writeText("  Start new game")
        if self.cursor_position == 1:
            self.screen.writeText("> Exit game <")
        else:
            self.screen.writeText("  Exit game  ")

    def notifyNeedToRender(self, screen, rects):
        pass

    def inputPlayer(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j or event.key == pygame.K_DOWN:
                    self.menuCursorPosition(1)
                if event.key == pygame.K_k or event.key == pygame.K_UP:
                    self.menuCursorPosition(-1)
                if event.key == pygame.K_RETURN:
                    self.menuActivate()
                if event.key == pygame.K_d:
                    self.world.screen.debug = -self.world.screen.debug
                    self.world.screen.fullscreen_render = True
                    self.render()

    def render(self):
        self.screen.render(self.clock)

    def menuCursorPosition(self, delta):
        self.cursor_position = self.cursor_position + delta
        if self.cursor_position < 0:
            self.cursor_position = 0
        if self.cursor_position > 1:
            self.cursor_position = 1
        self.screen.fullscreen_render = True

    def menuActivate(self):
        if self.cursor_position == 0:
            self.stage = "NEW_GAME"
        if self.cursor_position == 1:
            self.stage = "EXIT_GAME"

    def mainLoop(self):
        while self.stage == "MAIN_MENU":
            self.inputPlayer()
            self.render()
            self.clock.tick(self.FPS)
        return self.stage
