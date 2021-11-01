'''
Модуль работы с экраном
'''
# pylint: disable=no-member
import pygame


class Screen:
    '''
    Класс для работы с экраном и рендеринга изображений
    '''
    color_black = (0, 0, 0)
    color_darkgrey = (16, 16, 16)
    color_white = (255, 255, 255)
    fullscreen_render = True

    def attach(self, observer):
        '''
        Добавить наблюдателя
        '''
        self._observers.add(observer)

    def detach(self, observer):
        '''
        Убрать наблюдателя
        '''
        self._observers.remove(observer)

    def notify_need_to_render(self, *args):
        '''
        Объявить событие частичной перерисовки экрана
        '''
        for observer in self._observers:
            observer.notify_need_to_render(*args)

    def notify_screen_render(self, *args):
        '''
        Объявить событие полной перерисовки экрана
        '''
        for observer in self._observers:
            observer.notify_screen_render(*args)

    def __init__(self):
        self.i_text = 10
        self._observers = set()
        pygame.init()
        self.font = pygame.font.Font(None, 24)
        self.debug = -1
        self.old_rects = pygame.Rect(0, 0, 0, 0)
        screen_surface_flags = pygame.FULLSCREEN | pygame.DOUBLEBUF
        self.screen_surface = pygame.display.set_mode(
            (800, 600),
            screen_surface_flags)

    def render_rects(self, clock):
        '''
        Отрисовка экрана частично в рамках rects
        '''
        rects = []
        rects.append(self.old_rects)
        self.old_rects = self.write_text_rect("FPS: " + str(
            int(clock.get_fps())
        ), self.old_rects)
        self.notify_need_to_render(self, rects)
        rects.append(self.old_rects)
        if len(rects) > 1000:
            pygame.display.flip()
        else:
            pygame.display.update(rects)
        self.i_text = 10

    def render(self, clock):
        '''
        Отрисовка экрана полностью
        '''
        if self.fullscreen_render:
            self.screen_surface.fill(self.color_darkgrey)
            self.write_text("FPS: " + str(int(clock.get_fps())))
            self.notify_screen_render(self)
            pygame.display.flip()
            self.fullscreen_render = False
            self.i_text = 10
        else:
            self.render_rects(clock)
            self.i_text = 10

    def draw(self, sprite, coord_x, coord_y):
        '''
        Отрисовка спрайта по координатам coord_x, coord_y
        '''
        self.screen_surface.blit(sprite, (coord_x, coord_y))
        if self.debug > 0:
            self.draw_rect(sprite.get_rect().move(coord_x, coord_y))

    def write_text_xy(self, text, coord_x, coord_y, color=color_white):
        '''
        Отрисовка текста по координатам coord_x, coord_y
        '''
        text = self.font.render(text, 1, color)
        self.screen_surface.blit(text, (coord_x, coord_y))

    def write_text_rect(self, text, old_rects):
        '''
        Отрисовка текста в левом верхнем углу с предварительной
        заливкой прямоугольника под текстом фоновым цветом.
        '''
        text = self.font.render(text, 1, self.color_white)
        rect = text.get_rect()
        rect.move_ip(10, self.i_text)
        self.clean_box(old_rects)
        self.clean_box(rect)
        self.screen_surface.blit(text, rect)
        if self.debug > 0:
            self.draw_rect(rect)
        self.i_text = self.i_text + 30
        return rect

    def draw_rect(self, rect):
        '''
        Отрисовка прямоугольника rect
        '''
        (left, top, width, height) = rect.left, rect.top, rect.w, rect.h
        self.screen_surface.fill((255, 0, 255),
                                 pygame.Rect(left, top, width, 1))
        self.screen_surface.fill((255, 0, 255),
                                 pygame.Rect(left, top, 1, height))
        self.screen_surface.fill((255, 0, 255),
                                 pygame.Rect(left, top+height-1, width, 1))
        self.screen_surface.fill((255, 0, 255),
                                 pygame.Rect(left+width-1, top, 1, height))

    def clean_box(self, rect):
        '''
        Заполняет указанный rect фоновым цветом
        '''
        (left, top, width, height) = rect.left, rect.top, rect.w, rect.h
        self.screen_surface.fill(self.color_darkgrey, pygame.Rect(
            left, top, width, height))

    def write_text(self, text):
        '''
        Отрисовка текста в левом верхнем углу
        '''
        text = self.font.render(text, 1, self.color_white)
        self.screen_surface.blit(text, (10, self.i_text))
        self.i_text = self.i_text + 30
