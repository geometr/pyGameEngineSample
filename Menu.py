'''
Главное меню
'''
# pylint: disable=no-member,wrong-import-order
import pygame

import screen


class Menu:
    '''
    Главное меню используется в классе игры.
    После создания объекта для вызова меню
    следует использовать вызов main_loop(),
    который вернёт выбранный пункт в виде
    предопределённых строковых кодов
    '''
    def __init__(self):
        self.fps = 0
        self.cursor_position = 0
        self.screen = screen.Screen()
        self.clock = pygame.time.Clock()
        self.screen.attach(self)
        self.stage = "MAIN_MENU"

    def notify_screen_render(self, surface):
        '''
        Пришло событие перерисовки экрана.
        Рисуем все объекты
        '''
        if self.cursor_position == 0:
            surface.write_text("> Start new game <")
        else:
            surface.write_text("  Start new game")
        if self.cursor_position == 1:
            surface.write_text("> Exit game <")
        else:
            surface.write_text("  Exit game  ")

    def notify_need_to_render(self, surface, rects):
        '''
        Пришло событие частичной перерисовки
        Рисуем изменения на экране и заносим координаты
        в rects
        '''

    def input_player(self):
        '''
        Обрабатываем события и нажатия на клавиатуру
        '''
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_j, pygame.K_DOWN):
                    self.menu_cursor_position(1)
                if event.key in (pygame.K_k, pygame.K_UP):
                    self.menu_cursor_position(-1)
                if event.key == pygame.K_RETURN:
                    self.menu_activate()
                if event.key == pygame.K_d:
                    self.screen.debug = -self.screen.debug
                    self.screen.fullscreen_render = True
                    self.render()

    def render(self):
        '''
        Запуск отрисовки экрана
        '''
        self.screen.render(self.clock)

    def menu_cursor_position(self, delta):
        '''
        Проверка положения курсора выбора пункта меню
        '''
        self.cursor_position = self.cursor_position + delta
        self.cursor_position = max(self.cursor_position, 0)
        self.cursor_position = min(self.cursor_position, 1)
        self.screen.fullscreen_render = True

    def menu_activate(self):
        '''
        Выбор пункта меню
        '''
        if self.cursor_position == 0:
            self.stage = "NEW_GAME"
        if self.cursor_position == 1:
            self.stage = "EXIT_GAME"

    def main_loop(self):
        '''
        Главный цикл и точка входа
        '''
        while self.stage == "MAIN_MENU":
            self.input_player()
            self.render()
            self.clock.tick(self.fps)
        return self.stage
