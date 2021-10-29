import pygame
from pygame.locals import *

class Screen:
    color_black = (0,0,0)
    color_darkgrey = (16,16,16)
    color_white = (255, 255, 255)
    i_text = 10
    _observers=set()

    def attach(self, observer):
        self._observers.add(observer)
    def detach(self, observer):
        self._observers.remove(observer)

    def notifyNeedToRender(self, *args):
        for observer in self._observers:
            observer.notifyNeedToRender(*args)
    def notifyScreenRender(self, *args):
        for observer in self._observers:
            observer.notifyScreenRender(*args)

    def __init__(self):
        pygame.init()
        self.debug = -1
        self.old_rect = pygame.Rect(0,0,0,0)
        self.fullscreen_render = True
        self.font = pygame.font.Font(None,24)
        screen_surface_flags = pygame.FULLSCREEN | pygame.DOUBLEBUF
        self.screen_surface = pygame.display.set_mode((800,600),screen_surface_flags)

    def anotherRender(self, clock):
        rects = []
        rects.append(self.old_rect)
        self.old_rect = self.writeTextRect("FPS: " + str(int(clock.get_fps())),self.old_rect)
        self.notifyNeedToRender(self, rects)
        rects.append(self.old_rect)
        if (len(rects)>1000):
            pygame.display.flip()
        else:
            pygame.display.update(rects)
        self.i_text = 10

    def render(self,clock):
        if self.fullscreen_render:
            self.screen_surface.fill(self.color_darkgrey)
            self.writeText("FPS: " + str(int(clock.get_fps())))
            self.notifyScreenRender(self)
            pygame.display.flip()
            self.fullscreen_render = False
            self.i_text = 10
        else:
            self.anotherRender(clock)
            self.i_text = 10

    def draw(self, sprite, x, y):
        self.screen_surface.blit(sprite, (x, y))
        if (self.debug>0):
            self.drawRect(sprite.get_rect().move(x,y))

    def writeTextXY(self, text_to_write, coord_x, coord_y, color = color_white):
        text = self.font.render(text_to_write, 1, color)
        self.screen_surface.blit(text, (coord_x, coord_y))

    def writeTextRect(self, text_to_write, old_rect):
        text = self.font.render(text_to_write, 1, self.color_white)
        rect=text.get_rect()
        rect.move_ip(10,self.i_text)
        self.cleanBox(old_rect)
        self.cleanBox(rect)
        self.screen_surface.blit(text,rect)
        if (self.debug>0):
            self.drawRect(rect)
        self.i_text = self.i_text + 30
        return rect

    def drawRect(self, rect):
        (l,t,w,h)=rect.left,rect.top,rect.w,rect.h
        self.screen_surface.fill((255,0,255),pygame.Rect(l,t,w,1))
        self.screen_surface.fill((255,0,255),pygame.Rect(l,t,1,h))
        self.screen_surface.fill((255,0,255),pygame.Rect(l,t+h-1,w,1))
        self.screen_surface.fill((255,0,255),pygame.Rect(l+w-1,t,1,h))

    def cleanBox(self,rect):
        (l,t,w,h)=rect.left,rect.top,rect.w,rect.h
        self.screen_surface.fill(self.color_darkgrey,pygame.Rect(l,t,w,h))

    def writeText(self,text_to_write):
        text = self.font.render(text_to_write, 1, self.color_white)
        self.fps_old_rect = text.get_rect().move(10,self.i_text)
        self.screen_surface.blit(text,(10,self.i_text))
        self.i_text = self.i_text + 30
