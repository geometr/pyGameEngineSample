import Screen
import random
import array

class Region:
    region_size = 50
    level_map = array.array('b')
    color_terrain = (4, 20, 4)
    color_water = (4, 4, 20)
    def __init__(self):
        i = 0
        while i < self.region_size:
            j = 0
            while j < self.region_size:
                self.level_map.append(random.randrange(0,2))
                j =j + 1
            i = i + 1

    def notifyScreenRender(self, screen):
        y = 0
        while y < self.region_size:
            x = 0
            while x < self.region_size:
                tile = self.level_map[x + y * self.region_size]
                if tile:
                    color = self.color_terrain
                else:
                    color = self.color_water
                screen.writeTextXY(".", (x - y) * 4 + 300, (x + y) * 2 + 150, color)
                screen.writeTextXY(".", (x - y) * 4 + 300, (x + y) * 2 + 152, color)
                x = x + 1
            y = y + 1

    def notifyDayChanged(self, *args):
        pass;

    def notifyTimesChanged(self, times):
        if times == "morning":
            self.color_terrain = (0, 80 ,15)
            self.color_water = (0, 15, 80)
        elif times == "evening":
            self.color_terrain = (15, 80, 0)
            self.color_water = (15, 0, 80)
        elif times == "day":
            self.color_terrain = (15, 120, 15)
            self.color_water = (15, 15, 120)
        else:
            self.color_terrain = (4, 20, 4)
            self.color_water = (4, 4, 20)


