'''
Модуль реализации региона мира
'''
# pylint: disable=too-many-instance-attributes
import array
import random

import pygame

import region_sprites


class Region:
    '''
    Регион мира. При инициализации нужно указать координаты вывода на экран
    '''
    region_size = 20
    x_offset = int(20/2)
    y_offset = int(10/2)

    def __init__(self, screen_offset_x=300, screen_offset_y=50,
                 max_biom=1, min_biom=0):
        self.need_update = True
        self.level_map = array.array('H')
        self.screen_offset_x = screen_offset_x
        self.screen_offset_y = screen_offset_y
        self.max_biom = max_biom
        self.min_biom = min_biom
        self.old_times = "night"
        i = 0
        self.sprites = region_sprites.RegionSprites()

        while i < self.region_size:
            j = 0
            while j < self.region_size:
                self.level_map.append(
                    random.randrange(0 + self.min_biom, self.max_biom)
                )
                j = j + 1
            i = i + 1
        half_region_size = self.region_size / 2
        if (self.min_biom == 1 and self.max_biom < 4):
            num_trees = 0
            while num_trees < 10:
                x_coord = random.randrange(0, self.region_size)
                y_coord = random.randrange(0, self.region_size)
                if self.max_biom < 3:
                    tree = self.sprites.TREE
                else:
                    tree = self.sprites.OLD_TREE
                self.level_map[int(
                    x_coord + y_coord * self.region_size)] = tree
                num_trees = num_trees + 1
                self.level_map[int(
                    half_region_size +
                    self.region_size * (half_region_size - 1)
                )] = self.sprites.SHAVAR_ALDAN

        if self.min_biom == 1 and self.max_biom == 3:
            self.level_map[int(
                half_region_size + self.region_size * (half_region_size - 1)
            )] = self.sprites.SHAVAR
        if self.min_biom == 0 and self.max_biom == 2:
            self.level_map[int(
                half_region_size + self.region_size * (half_region_size - 1)
            )] = self.sprites.SHAVAR_ALDAN

    def notify_day_changed(self, *args):
        '''
        Сменился день
        '''

    def notify_hour_changed(self, times):
        '''
        Сменился час
        '''
        if times != self.old_times:
            self.old_times = times
            self.need_update = True
        if times == "night":
            for sprite_id, sprite in self.sprites.night.items():
                self.sprites.times[sprite_id] = sprite
        elif times == "day":
            for sprite_id, sprite in self.sprites.day.items():
                self.sprites.times[sprite_id] = sprite
        elif times == "morning":
            for sprite_id, sprite in self.sprites.morning.items():
                self.sprites.times[sprite_id] = sprite
        else:
            for sprite_id, sprite in self.sprites.evening.items():
                self.sprites.times[sprite_id] = sprite

    def draw_region(self, surface, rects):
        '''
        Отрисовка региона
        '''
        if self.need_update:
            reg_y = 0
            while reg_y < self.region_size:
                reg_x = 0
                while reg_x < self.region_size:
                    xoff = 0
                    yoff = 0
                    tile = self.level_map[reg_x + reg_y * self.region_size]
                    sprite = self.sprites.times[int(tile)]
                    sprite_xoff, sprite_yoff = self.sprites.sizes[int(tile)]
                    if int(sprite_xoff/2) != self.x_offset:
                        xoff = -sprite_xoff + self.x_offset*2
                    if int(sprite_yoff/2) != self.y_offset:
                        yoff = -sprite_yoff + self.y_offset*2
                    i = (reg_x-reg_y)*self.x_offset+xoff+self.screen_offset_x
                    j = (reg_x+reg_y)*self.y_offset+yoff+self.screen_offset_y
                    if self.need_update:
                        rects.append(
                            pygame.Rect(i, j, sprite_xoff, sprite_yoff))
                    surface.draw(sprite, i, j)
                    reg_x = reg_x + 1
                reg_y = reg_y + 1
            self.need_update = False

    def notify_need_to_render(self, surface, rects):
        '''
        Пришло событие обновления экрана.
        Отрисовка изменений и заполнение
        массива rects
        '''
        self.draw_region(surface, rects)

    def notify_screen_render(self, surface):
        '''
        Пришло событие полного обновления экрана
        '''
        self.draw_region(surface, [])
