import pygame

class RegionSprites:
    TERRAIN = 1
    WATER = 0
    DESERT = 2
    LAVA = 3

    def __init__(self):
        self.sprites = dict()
        self.night = dict()
        self.day = dict()
        self.morning = dict()
        self.evening = dict()
        self.times = dict()

        self.sprites[self.TERRAIN] = pygame.image.load('../assets/tile_grass.png').convert_alpha()
        self.sprites[self.WATER] = pygame.image.load('../assets/tile_water.png').convert_alpha()
        self.sprites[self.DESERT] = pygame.image.load('../assets/tile_sand.png').convert_alpha()
        self.sprites[self.LAVA] = pygame.image.load('../assets/tile_lava.png').convert_alpha()
        self.prepareSprites()

        for type,sprite in self.night.items():
            self.times[type] = sprite


    def prepareSprites(self):
        size = self.width, self.height = (20, 10)
        self.sprite_night_filter = pygame.Surface(size).convert_alpha()
        self.sprite_night_filter.fill((148,148,128,0))
        self.sprite_day_filter = pygame.Surface(size).convert_alpha()
        self.sprite_day_filter.fill((16,0,16,0))
        self.sprite_morning_filter = pygame.Surface(size).convert_alpha()
        self.sprite_morning_filter.fill((64,32,32,0))
        self.sprite_evening_filter = pygame.Surface(size).convert_alpha()
        self.sprite_evening_filter.fill((32,64,64,0))

        for type,sprite in self.sprites.items():
            self.morning[type] = sprite.copy()
            self.day[type] = sprite.copy()
            self.night[type] = sprite.copy()
            self.evening[type] = sprite.copy()

            self.morning[type].blit(self.sprite_morning_filter, (0,0), None, pygame.BLEND_RGBA_SUB)
            self.day[type].blit(self.sprite_day_filter, (0,0), None, pygame.BLEND_RGBA_SUB)
            self.evening[type].blit(self.sprite_evening_filter, (0,0), None, pygame.BLEND_RGBA_SUB)
            self.night[type].blit(self.sprite_night_filter, (0,0), None, pygame.BLEND_RGBA_SUB)
