'''
Описание механики мира
'''
import json

import local_time

import player

import region

import screen

import temperature


class World:
    '''
    Механика мира
    '''
    def __init__(self, set_hours_in_day=24, set_days_in_year=360):
        self.screen = screen.Screen()
        self.local_time = local_time.Time(set_hours_in_day, set_days_in_year)
        self.temperature = temperature.Temperature()
        self.local_time.attach(self.temperature)
        self.player = player.Player()
        self.regions = set()
        for coord_x, coord_y, biom, min_biom in ((400, 0, 2, 1),
                                                 (600, 100, 3, 1),
                                                 (800, 200, 4, 2),
                                                 (200, 100, 2, 0),
                                                 (400, 200, 2, 0),
                                                 (600, 300, 4, 2),
                                                 (0, 200, 1, 0),
                                                 (200, 300, 2, 0),
                                                 (400, 400, 4, 2)):
            self.regions.add(self.create_region(
                coord_x, coord_y, biom, min_biom))
        self.screen.attach(self.temperature)
        self.screen.attach(self.local_time)
        self.screen.attach(self.player)

    def create_region(self, coord_x, coord_y, biom, min_biom):
        '''
        Создание региона
        '''
        local_region = region.Region(coord_x, coord_y, biom, min_biom)
        self.local_time.attach(local_region)
        self.screen.attach(local_region)
        return local_region

    def tick(self):
        '''
        Шаг мира
        '''
        self.local_time.tick()

    def render(self, clock):
        '''
        Отрисовка
        '''
        self.screen.render(clock)
