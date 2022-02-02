'''
Рендер состояния времени
'''
# pylint: disable=too-many-instance-atributes
import pygame

class Time_render:
    '''
    Класс рендера состояния времени
    '''
    def __init__(self):
        self.old_rect = pygame.Rect(0, 0, 0, 0)

    def notify_need_to_render(self, screen, rects, times_of_day, current_hour, current_day, current_year):
        '''
        Событие частичной отрисовки
        '''
        rects.append(self.old_rect)
        self.old_rect = screen.write_text_rect("Today " +
                                                   str(current_day) +
                                                   " day of " +
                                                   str(current_year) +
                                                   " year. Now " +
                                                   str(current_hour) +
                                                   " o'clock (" +
                                                   times_of_day +
                                                   ").", self.old_rect)
        rects.append(self.old_rect)

    def notify_screen_render(self, screen, times_of_day, current_hour, current_day, current_year):
        screen.write_text("Today " + str(current_day) +
                          " day of " + str(current_year) +
                          " year. Now " + str(current_hour) +
                          " o'clock (" + times_of_day + ").")
