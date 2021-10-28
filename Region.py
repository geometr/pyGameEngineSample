import Screen
import random
import array
import pygame
import RegionSprites

class Region:
    region_size = 20
    x_offset = int(20/2)
    y_offset = int(10/2)
    def __init__(self, set_screen_offset_x = 300, set_screen_offset_y = 50, set_max_biom = 1, set_min_biom = 0):
        self.level_map = array.array('H')
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
        if self.min_biom == 1 and self.max_biom == 2:
            t = 0
            while t < 10:
                x = random.randrange(0,self.region_size)
                y = random.randrange(0,self.region_size)
                self.level_map[int(x + y * self.region_size)] = self.sprites.TREE
                t = t + 1
            self.level_map[int(self.region_size/2 + self.region_size * ( self.region_size /2 -1))]=self.sprites.SHAVAR_ALDAN

        if self.min_biom == 1 and self.max_biom == 3:
            self.level_map[int(self.region_size/2 + self.region_size * ( self.region_size /2 -1))]=self.sprites.SHAVAR
        if self.min_biom == 0 and self.max_biom == 2:
            self.level_map[int(self.region_size/2 + self.region_size * ( self.region_size /2 -1))]=self.sprites.SHAVAR_ALDAN
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
        y = 0
        while y < self.region_size:
            x = 0
            while x < self.region_size:
                xoff = 0
                yoff = 0
                tile = self.level_map[x + y * self.region_size]
                sprite = self.sprites.times[int(tile)]
                sprite_xoff, sprite_yoff = self.sprites.sizes[int(tile)]
                if (int(sprite_xoff/2) != self.x_offset):
                    xoff = -sprite_xoff + self.x_offset*2
                if (int(sprite_yoff/2) != self.y_offset):
                    yoff = -sprite_yoff + self.y_offset*2
                screen.draw(sprite, (x - y) * self.x_offset + xoff + self.screen_offset_x, yoff + (x + y) * self.y_offset + self.screen_offset_y)
                x = x + 1
            y = y + 1
