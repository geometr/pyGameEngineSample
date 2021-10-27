import Screen
import random
import array
import pygame
import RegionSprites

class Region:
    region_size = 20
    def __init__(self, set_screen_offset_x = 300, set_screen_offset_y = 50, set_max_biom = 1, set_min_biom = 0):
        self.level_map = array.array('b')
        self.screen_offset_x = set_screen_offset_x
        self.screen_offset_y = set_screen_offset_y
        self.max_biom = set_max_biom
        self.min_biom = set_min_biom
        self.sprites = RegionSprites.RegionSprites()
        i = 0
        while i < self.region_size:
            j = 0
            while j < self.region_size:
                self.level_map.append(random.randrange(0 + self.min_biom,self.max_biom))
                j =j + 1
            i = i + 1

    def notifyDayChanged(self, *args):
        pass

    def notifyTimesChanged(self, times):
        if times == "night":
            for type, sprite in self.sprites.night.items():
                self.sprites.times[type] = sprite
        elif times == "day":
            for type, sprite in self.sprites.day.items():
                self.sprites.times[type] = sprite
        elif times == "morning":
            for type, sprite in self.sprites.morning.items():
                self.sprites.times[type] = sprite
        else:
            for type, sprite in self.sprites.evening.items():
                self.sprites.times[type] = sprite

    def notifyScreenRender(self, screen):
        x_offset = self.sprites.width / 2
        y_offset = self.sprites.height / 2
        y = 0
        while y < self.region_size:
            x = 0
            while x < self.region_size:
                tile = self.level_map[x + y * self.region_size]
                sprite = self.sprites.times[int(tile)]
                screen.draw(sprite, (x - y) * x_offset + self.screen_offset_x, (x + y) * y_offset + self.screen_offset_y)
                x = x + 1
            y = y + 1
