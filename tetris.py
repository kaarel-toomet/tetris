#!/usr/bin/python3
import pygame as pg

class metasprite(pg.sprite.Group):
    def __init__(self,x,y,componentlist):
        # componentlist: [ (rx, ry, img), (rx, ry,img), ...]
        # rx, ry: relative location wrt to the metasprite x, y
        super(pg.sprite.Group, self).__init__()
        for rx,ry,img in componentlist:
            sprite = pg.sprite.Sprite()
            sprite.image = img
            sprite.rect = sprite.image.get_rect()
            sprite.rect.x = x
            sprite.rect.y = y
            self.add(sprite)
        self.x=x
        self.y=y
        self.componentlist=componentlist

    def relmove(x,y):
        self.x += x
        self.y += y

pg.init()
screen = pg.display.set_mode((0,0), pg.RESIZABLE)
screenw = screen.get_width()
screenh = screen.get_height()
pg.display.set_caption("movepic")
img = pg.image.load("block.png")
ms = metasprite(1000,1000,[(10,10,img)])

while True:
    screen.fill((0,0,0))
    ms.draw(screen)
    pg.display.update()

pg.quit()
