'''
Рендер состояния времени
'''
# pylint: disable=too-many-instance-atributes
import pygame

import abstract_render

class Time_render(abstract_render.Abstract_render):
    '''
    Класс рендера состояния времени
    '''
    def __init__(self):
        super().__init__()

    def notify_need_to_render(self, screen, rects, times_of_day, current_hour, current_day, current_year):
        super().notify_need_to_render({'current_day': current_day,
                                        'current_year': current_year,
                                        'current_hour': current_hour,
                                        'times_of_day': times_of_day,
                                        'screen': screen,
                                        'rects': rects})

    def notify_screen_render(self, screen, times_of_day, current_hour, current_day, current_year):
        super().notify_screen_render({'current_day': current_day,
                                        'current_year': current_year,
                                        'current_hour': current_hour,
                                        'times_of_day': times_of_day,
                                        'screen': screen})
    def screen_render(self, args):
        current_day = args['current_day']
        current_year = args['current_year']
        current_hour = args['current_hour']
        times_of_day = args['times_of_day']
        screen = args['screen']
        screen.write_text(self.text_to_render(current_day, current_year, current_hour, times_of_day))

    def need_to_render(self, args):
        current_day = args['current_day']
        current_year = args['current_year']
        current_hour = args['current_hour']
        times_of_day = args['times_of_day']
        screen = args['screen']
        self.old_rect = screen.write_text_rect(
            self.text_to_render(current_day, current_year, current_hour, times_of_day), self.old_rect)
    def text_to_render(self, current_day, current_year, current_hour, times_of_day):
        return "Today " + str(current_day) + " day of " + str(current_year) + " year. Now " + str(current_hour) + " o'clock (" + times_of_day + ")."

