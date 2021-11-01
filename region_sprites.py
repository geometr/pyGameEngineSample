'''
Модуль загрузки спрайтов для региона
'''
# pylint: disable=no-member
# pylint: disable=too-many-instance-attributes,too-few-public-methods
import pygame
'''
TODO: Выделить сабкласс спрайт
TODO: убрать pylint: disable=too-many-instance-attributes,
too-few-public-methods
'''


class RegionSprites:
    '''
    Класс содержит все спрайты для региона
    '''
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
        self.sprites = {}
        self.night = {}
        self.day = {}
        self.morning = {}
        self.evening = {}
        self.times = {}
        self.sizes = {}
        self.night_filter = {}
        self.day_filter = {}
        self.morning_filter = {}
        self.evening_filter = {}

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

        self.prepare_sprites()
        for sprite_id, sprite in self.night.items():
            self.times[sprite_id] = sprite

    def prepare_sprites(self):
        '''
        Создаёт спрайты с окраской по времени
        '''
        for sprite_id, (width, height) in self.sizes.items():
            self.night_filter[sprite_id] = pygame.Surface(
                (width, height)).convert_alpha()
            self.night_filter[sprite_id].fill((148, 148, 128, 0))
            self.day_filter[sprite_id] = pygame.Surface(
                (width, height)).convert_alpha()
            self.day_filter[sprite_id].fill((16, 0, 16, 0))
            self.morning_filter[sprite_id] = pygame.Surface(
                (width, height)).convert_alpha()
            self.morning_filter[sprite_id].fill((64, 32, 32, 0))
            self.evening_filter[sprite_id] = pygame.Surface(
                (width, height)).convert_alpha()
            self.evening_filter[sprite_id].fill((32, 64, 64, 0))

        for sprite_id, sprite in self.sprites.items():
            self.morning[sprite_id] = sprite.copy()
            self.day[sprite_id] = sprite.copy()
            self.night[sprite_id] = sprite.copy()
            self.evening[sprite_id] = sprite.copy()
            if sprite_id != self.LAVA:
                self.morning[sprite_id].blit(
                    self.morning_filter[sprite_id],
                    (0, 0),
                    None,
                    pygame.BLEND_RGBA_SUB)
                self.evening[sprite_id].blit(
                    self.evening_filter[sprite_id],
                    (0, 0),
                    None,
                    pygame.BLEND_RGBA_SUB)
                self.night[sprite_id].blit(
                    self.night_filter[sprite_id],
                    (0, 0),
                    None,
                    pygame.BLEND_RGBA_SUB)
                self.day[sprite_id].blit(
                    self.day_filter[sprite_id],
                    (0, 0),
                    None,
                    pygame.BLEND_RGBA_SUB)
