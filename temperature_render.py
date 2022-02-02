'''
Рендер температуры
'''
# pylint: disable=too-many-instance-attributes
import pygame

import abstract_render

class Temperature_render(abstract_render.Abstract_render):
    def __init__(self):
        super().__init__()
    def notify_need_to_render(self, local_temperature, screen, rects):
        '''
        Событие частичной отрисовки
        '''
        super().notify_need_to_render({'local_temperature': local_temperature, 'screen': screen, 'rects': rects});
    def notify_screen_render(self, local_temperature, screen):
        '''
        Событие полная отрисовка
        '''
        screen.write_text(
            "Temperature " + str(int(local_temperature)) + "C")
    def need_to_render(self, args):
        local_temperature = args['local_temperature']
        screen = args['screen']
        self.old_rect = screen.write_text_rect("Temperature " + str(
            int(local_temperature)) + "C", self.old_rect)

