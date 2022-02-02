'''
Абстрактный рендер для сущностей.
'''
import pygame

class Abstract_render:
    def __init__(self):
        self.old_rect = pygame.Rect(0, 0, 0, 0)

    def notify_need_to_render(self, args):
        self.before_render(args['rects'])
        self.need_to_render(args)
        self.after_render(args['rects'])

    def before_render(self, rects):
        rects.append(self.old_rect)

    def after_render(self, rects):
        rects.append(self.old_rect)

    def need_to_render(self, args):
        pass
