'''
Рендер температуры
'''
# pylint: disable=too-many-instance-attributes
import pygame

class Temperature_render:
    def __init__(self):
        self.old_rect = pygame.Rect(0, 0, 0, 0)
    def notify_need_to_render(self, local_temperature, screen, rects):
        '''
        Событие частичной отрисовки
        '''
        rects.append(self.old_rect)
        self.old_rect = screen.write_text_rect("Temperature " + str(
            int(local_temperature)) + "C", self.old_rect)
        rects.append(self.old_rect)
    def notify_screen_render(self, local_temperature, screen):
        '''
        Событие полная отрисовка
        '''
        screen.write_text(
            "Temperature " + str(int(local_temperature)) + "C")
