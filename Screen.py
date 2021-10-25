import pygame
from pygame.locals import *

class Screen:
    color_black = (0,0,0)
    color_white = (255, 255, 255)
    i_text = 10
    _observers=set()

    def attach(self, observer):
        self._observers.add(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notifyScreenRender(self, *args):
        for observer in self._observers:
            observer.notifyScreenRender(*args)

    def __init__(self):
        pygame.init()
        self.font = pygame.font.Font(None,24)
        screen_surface_flags = pygame.FULLSCREEN
        self.screen_surface = pygame.display.set_mode((640,480),screen_surface_flags)

    def render(self,clock):
        self.screen_surface.fill(self.color_black)
        self.writeText("FPS: " + str(int(clock.get_fps())))
        self.notifyScreenRender(self)
        pygame.display.flip()
        self.i_text = 10

    def writeTextXY(self, text_to_write, coord_x, coord_y, color = color_white):
        text = self.font.render(text_to_write, 1, color)
        self.screen_surface.blit(text, (coord_x, coord_y))

    def writeText(self,text_to_write):
        text = self.font.render(text_to_write, 1, self.color_white)
        self.screen_surface.blit(text,(10,self.i_text))
        self.i_text = self.i_text + 30
