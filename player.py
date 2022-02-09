# pylint: disable=too-many-instance-atributes
import pygame

class Player:

    BODY = 0

    def __init__(self):
        self.region = 5
        self.x = 5
        self.y = 5
        self.sprites = {}
        self.night = {}
        self.day = {}
        self.morning = {}
        self.evening = {}
        self.night_filter = {}
        self.day_filter = {}
        self.morning_filter = {}
        self.evening_filter = {}
        self.sizes = {}

        self.sprites[self.BODY] = pygame.image.load(
            'assets/player_body.png').convert_alpha()
        self.sizes[self.BODY] = (10, 20)

    def notify_need_to_render(self, screen, rects):
        body_width, body_height = self.sizes[self.BODY]
        rects.append(pygame.Rect(100,200, body_width,body_height))
        screen.draw(self.sprites[self.BODY],self.x, self.y)
    def notify_screen_render(self, screen):
        screen.draw(self.sprites[self.BODY], self.x, self.y)
    def move_left(self):
        self.x = self.x - 1
    def move_right(self):
        self.x = self.x + 1
    def move_up(self):
        self.y = self.y - 1
    def move_down(self):
        self.y = self.y + 1
