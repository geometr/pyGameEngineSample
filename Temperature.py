'''
Модуль обсчёта температуры
'''
import random

import pygame


class Temperature:
    '''
    Класс обсчета температуры
    '''
    local_temperature = 0
    global_temperature = 0
    maximal_delta = 20
    half_maximal_delta = maximal_delta / 2

    def notify_hour_changed(self, *argv):
        '''
        Прошёл час
        '''
        self.times_delta_temperature(*argv)
        self.need_update = True

    def notify_day_changed(self, *argv):
        '''
        Прошел день
        '''
        self.calculate_global_temperature(*argv)
        self.need_update = True

    def __init__(self, set_maximal_delta=20):
        self.maximal_delta = set_maximal_delta
        self.half_maxmial_delta = self.maximal_delta / 2
        self.global_temperature = -self.half_maximal_delta
        self.random_diff_local_temperature()
        self.need_update = True
        self.old_rect = pygame.Rect(0, 0, 0, 0)

    def calculate_global_temperature(self, current_day, days_in_year):
        '''
        Вычисляем глобальную температуру
        '''
        if current_day < days_in_year / 2:
            self.calculate_global_temperature_spring(current_day, days_in_year)
        else:
            self.calculate_global_temperature_autumn(current_day, days_in_year)
        self.random_diff_local_temperature()

    def calculate_global_temperature_spring(self, current_day, days_in_year):
        '''
        Температура в весеннем цикле (рост)
        '''
        self.global_temperature = self.half_maximal_delta - (
            current_day / days_in_year * 2 * self.maximal_delta
        )

    def calculate_global_temperature_autumn(self, current_day, days_in_year):
        '''
        Температура в осеннем цикле (падение)
        '''
        self.global_temperature = -self.half_maximal_delta + (
            current_day * 2 / days_in_year * self.maximal_delta)

    def random_diff_local_temperature(self):
        '''
        Случайное изменение локальной температуры
        '''
        self.local_temperature = self.global_temperature + random.randrange(
            1, self.maximal_delta) - self.half_maximal_delta

    def times_delta_temperature(self, times):
        '''
        температура в зависимости от времени суток
        '''
        if times == "night":
            self.local_temperature = self.local_temperature - 1
        elif times == "day":
            self.local_temperature = self.local_temperature + 2
        elif times == "morning":
            self.local_temperature = self.local_temperature + 0.5
        else:
            self.local_temperature = self.local_temperature - 0.5

    def get_temperature(self):
        '''
        Возвращает локальную температуру
        '''
        return self.local_temperature

    def notify_need_to_render(self, screen, rects):
        '''
        Событие частичной отрисовки
        '''
        if self.need_update:
            rects.append(self.old_rect)
            self.old_rect = screen.write_text_rect("Temperature " + str(
                int(self.local_temperature)) + "C", self.old_rect)
            self.need_update = False
            rects.append(self.old_rect)

    def notify_screen_render(self, screen):
        '''
        Событие полная отрисовка
        '''
        screen.write_text(
            "Temperature " + str(int(self.local_temperature)) + "C")
