'''
Обработка хода времени
'''
# pylint: disable=too-many-instance-attributes
import pygame


class Time:
    '''
    Класс работы со временем
    '''
    hours_in_day = 24
    days_in_year = 360
    years_in_century = 100
    current_hour = 0
    times_of_day = ""
    current_day = 0
    current_year = 0

    morning_begins = 0.0
    day_begins = 0.0
    evening_begins = 0.0
    night_begins = 0.0

    delta_times_of_day = 0.0
    delta_day = 0.0
    _observers = set()

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

    def notify_day_changed(self, *args):
        '''
        Новый день
        '''
        for observer in self._observers:
            observer.notify_day_changed(*args)

    def notify_hour_changed(self, *args):
        '''
        Новый час
        '''
        for observer in self._observers:
            observer.notify_hour_changed(*args)

    def __init__(self, set_hours_in_day=24, set_days_in_year=360):
        self.hours_in_day = set_hours_in_day
        self.days_in_year = set_days_in_year
        self.delta_times_of_day = self.hours_in_day/4
        self.update_timing_begins()
        self.calculate_times_of_day()
        self.need_update = True
        self.old_rect = pygame.Rect(0, 0, 0, 0)

    def update_timing_begins(self):
        '''
        Вычисление смены времени суток
        '''
        self.delta_day = -16 / self.days_in_year ** 2 * (
            self.current_day-self.days_in_year/2) ** 2 + 2
        self.morning_begins = (self.delta_times_of_day -
                               self.delta_day - self.delta_times_of_day / 2)
        self.day_begins = self.morning_begins + self.delta_times_of_day
        self.evening_begins = (self.day_begins + self.delta_times_of_day
                               + self.delta_day)
        self.night_begins = self.evening_begins + self.delta_times_of_day

    def get_steps_in_century(self):
        '''
        Сколько часов в столетии
        '''
        return self.get_steps_in_year()*self.years_in_century

    def get_steps_in_year(self):
        '''
        Сколько часов в году
        '''
        return self.hours_in_day*self.days_in_year

    def tick(self):
        '''
        Шаг часов - 1 час
        '''
        self.current_hour = self.current_hour + 1
        if self.current_hour == self.hours_in_day:
            self.current_hour = 0
            self.current_day = self.current_day + 1
            self.notify_day_changed(self.current_day, self.days_in_year)
            self.update_timing_begins()

        if self.current_day == self.days_in_year:
            self.current_day = 0
            self.current_year = self.current_year + 1
        self.calculate_times_of_day()
        self.need_update = True

    def calculate_times_of_day(self):
        '''
        Вычисление времени суток
        '''
        if self.current_hour < self.morning_begins:
            self.night_world()
        elif self.current_hour < self.day_begins:
            self.morning_world()
        elif self.current_hour < self.evening_begins:
            self.day_world()
        elif self.current_hour < self.night_begins:
            self.evening_world()
        else:
            self.night_world()
        self.notify_hour_changed(self.times_of_day)

    def night_world(self):
        '''
        Наступила ночь
        '''
        self.times_of_day = "night"

    def morning_world(self):
        '''
        Наступило утро
        '''
        self.times_of_day = "morning"

    def day_world(self):
        '''
        Наступило день
        '''
        self.times_of_day = "day"

    def evening_world(self):
        '''
        Наступило вечер
        '''
        self.times_of_day = "evening"

    def notify_need_to_render(self, screen, rects):
        '''
        Отрисовка части экрана
        '''
        if self.need_update:
            rects.append(self.old_rect)
            self.old_rect = screen.write_text_rect("Today " +
                                                   str(self.current_day) +
                                                   " day of " +
                                                   str(self.current_year) +
                                                   " year. Now " +
                                                   str(self.current_hour) +
                                                   " o'clock (" +
                                                   self.times_of_day +
                                                   ").", self.old_rect)
            rects.append(self.old_rect)
            self.need_update = False

    def notify_screen_render(self, screen):
        '''
        Отрисовка всего экрана
        '''
        screen.write_text("Today " + str(self.current_day) +
                          " day of " + str(self.current_year) +
                          " year. Now " + str(self.current_hour) +
                          " o'clock (" + self.times_of_day + ").")
