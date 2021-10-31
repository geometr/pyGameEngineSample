import pygame


class RegionSprites:
    TERRAIN = 1
    WATER = 0
    DESERT = 2
    LAVA = 3

    SHAVAR = 1000
    SHAVAR_ALDAN = 1001
    SHAVAR_GOO = 1002
    TREE = 1003
    OLD_TREE = 1004

    def __init__(self):
        self.sprites = dict()
        self.night = dict()
        self.day = dict()
        self.morning = dict()
        self.evening = dict()
        self.times = dict()
        self.sizes = dict()
        self.night_filter = dict()
        self.day_filter = dict()
        self.morning_filter = dict()
        self.evening_filter = dict()

        self.sprites[self.TERRAIN] = pygame.image.load(
            '../assets/tile_grass.png').convert_alpha()
        self.sizes[self.TERRAIN] = (20, 10)
        self.sprites[self.WATER] = pygame.image.load(
            '../assets/tile_water.png').convert_alpha()
        self.sizes[self.WATER] = (20, 10)
        self.sprites[self.DESERT] = pygame.image.load(
            '../assets/tile_sand.png').convert_alpha()
        self.sizes[self.DESERT] = (20, 10)
        self.sprites[self.LAVA] = pygame.image.load(
            '../assets/tile_lava.png').convert_alpha()
        self.sizes[self.LAVA] = (20, 10)

        self.sprites[self.SHAVAR] = pygame.image.load(
            '../assets/tile_shavar.png').convert_alpha()
        self.sizes[self.SHAVAR] = (20, 10)
        self.sprites[self.SHAVAR_ALDAN] = pygame.image.load(
            '../assets/tile_shavar_aldan.png').convert_alpha()
        self.sizes[self.SHAVAR_ALDAN] = (20, 10)
        self.sprites[self.SHAVAR_GOO] = pygame.image.load(
            '../assets/tile_shavar_goo.png').convert_alpha()
        self.sizes[self.SHAVAR_GOO] = (20, 10)

        self.sprites[self.TREE] = pygame.image.load(
            '../assets/tile_tree.png').convert_alpha()
        self.sizes[self.TREE] = (20, 30)

        self.sprites[self.OLD_TREE] = pygame.image.load(
            '../assets/tile_old_tree.png').convert_alpha()
        self.sizes[self.OLD_TREE] = (20, 30)

        self.prepareSprites()
        for type, sprite in self.night.items():
            self.times[type] = sprite

    def prepareSprites(self):
        for type, (width, height) in self.sizes.items():
            self.night_filter[type] = pygame.Surface(
                (width, height)).convert_alpha()
            self.night_filter[type].fill((148, 148, 128, 0))
            self.day_filter[type] = pygame.Surface(
                (width, height)).convert_alpha()
            self.day_filter[type].fill((16, 0, 16, 0))
            self.morning_filter[type] = pygame.Surface(
                (width, height)).convert_alpha()
            self.morning_filter[type].fill((64, 32, 32, 0))
            self.evening_filter[type] = pygame.Surface(
                (width, height)).convert_alpha()
            self.evening_filter[type].fill((32, 64, 64, 0))

        for type, sprite in self.sprites.items():
            self.morning[type] = sprite.copy()
            self.day[type] = sprite.copy()
            self.night[type] = sprite.copy()
            self.evening[type] = sprite.copy()
            if (type != self.LAVA):
                self.morning[type].blit(
                    self.morning_filter[type],
                    (0, 0),
                    None,
                    pygame.BLEND_RGBA_SUB)
                self.evening[type].blit(
                    self.evening_filter[type],
                    (0, 0),
                    None,
                    pygame.BLEND_RGBA_SUB)
                self.night[type].blit(
                    self.night_filter[type],
                    (0, 0),
                    None,
                    pygame.BLEND_RGBA_SUB)
                self.day[type].blit(
                    self.day_filter[type],
                    (0, 0),
                    None,
                    pygame.BLEND_RGBA_SUB)
