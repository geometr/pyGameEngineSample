'''
Главный модуль игры
'''
# pylint: disable=wrong-import-order,no-member
import sys

import menu

import pygame

import world


class Game:
    ''' Основной класс игры '''
    def __init__(self):

        self.fps = 0
        self.running = True
        self.world = world.World()
        self.clock = pygame.time.Clock()
        self.make_step = -1
        self.main_menu = menu.Menu()
        self.stage = self.main_menu.main_loop()
        self.main_loop()

    def main_loop(self):
        ''' Главный цикл игры '''
        if self.stage == "NEW_GAME":
            while self.running:
                self.input_player()
                if self.make_step > 0:
                    self.update()
                self.render()
                self.clock.tick(self.fps)
        elif self.stage == "EXIT_GAME":
            pygame.quit()
            sys.exit()

    def render(self):
        ''' Рендер игры на экран '''
        self.world.render(self.clock)

    def update(self):
        ''' Обсчёт такта игры '''
        self.world.tick()

    def input_player(self):
        ''' Опрос клавиатуры '''
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
