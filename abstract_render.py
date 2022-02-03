'''
Абстрактный рендер для сущностей.
'''
import pygame

class Abstract_render:
    def __init__(self):
        self.old_rect = pygame.Rect(0, 0, 0, 0)

    def notify_need_to_render(self, args):
        self.__before_render(args['rects'])
        self.need_to_render(args)
        self.__after_render(args['rects'])

    def __before_render(self, rects):
        rects.append(self.old_rect)

    def __after_render(self, rects):
        rects.append(self.old_rect)

    def need_to_render(self, args):
        pass

    def notify_screen_render(self, args):
        self.screen_render(args)

    def screen_render(self, args):
        pass
