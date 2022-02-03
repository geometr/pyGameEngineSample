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
        super().notify_need_to_render({'local_temperature': local_temperature, 'screen': screen, 'rects': rects})
    def notify_screen_render(self, local_temperature, screen):
        '''
        Событие полная отрисовка
        '''
        super().notify_screen_render({'local_temperature': local_temperature, 'screen': screen})

    def screen_render(self, args):
        local_temperature = args['local_temperature']
        screen = args['screen']
        screen.write_text(self.text_to_render(local_temperature))

    def need_to_render(self, args):
        local_temperature = args['local_temperature']
        screen = args['screen']
        self.old_rect = screen.write_text_rect(self.text_to_render(local_temperature), self.old_rect)

    def text_to_render(self, local_temperature):
        return "Temperature " + str(int(local_temperature)) + "C"

