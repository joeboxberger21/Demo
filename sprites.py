#This file was created by Joe Boxberger
#Sprite Classes for game

import pygame as pg
from pygame.sprite import Sprite
import random, math
from settings import *


# player_HEIGHT = 45
# player_WIDTH = 35


class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.width = 35
        self.height = 45
        self.image = pg.Surface((self.width, self.height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (self.width / 2, self.height / 2)
        self.vx = 0
        self.vy = 0
        self.speed = 5
    
    def update(self):
        self.vx = 0
        self.vy = 0
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.vx = -self.speed
        if keys[pg.K_d]:
            self.vx = self.speed
        if keys[pg.K_s]:
            self.vy = self.speed
        if keys[pg.K_w]:
            self.vy = -self.speed
        if self.vx != 0 and self.vy != 0:
            # 1/square root 2 = ~0.7071, use this to lower the vx and vy if moving both at once, this number is found b/c of a^2 + b^2 = c^2
            self.vx *= 0.7071
            self.vy *= 0.7071

        print('X: ' + str(self.rect.x) + ' Y: ' + str(self.rect.y))
        self.rect.x += self.vx
        self.rect.y += self.vy

class Enemy(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.width = 35
        self.height = 45
        self.image = pg.Surface((self.width, self.height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (self.width / 2, self.height / 2)
        self.vx = 0
        self.vy = 0
        self.rect.x = 0
        self.rect.y = 0
        self.x = 0
        self.y = 0
        self.follow = None
        self.speed = 3
    
    def update(self):
        #Pythag to find distance from player
        self.c = math.sqrt((self.follow.rect.x - self.rect.x) **2 + (self.follow.rect.y - self.rect.y)**2)

        if self.c != 0:
            #Create a multiplier from the distance between the player, 
            self.x = (self.follow.rect.x - self.rect.x) / self.c
            self.y = (self.follow.rect.y - self.rect.y) / self.c
        print('c: ' + str(self.c))

        self.rect.x += self.x * self.speed
        self.rect.y += self.y * self.speed

class Weapon(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.width = 60
        self.height = 10
        self.image = pg.Surface((self.height, self.height))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (self.width / 2, self.height / 2)
        self.player = None
    
    def update(self):
        mx, my = pg.mouse.get_pos()
        #TODO: Rotate based on mouse pos

        self.rect.x = self.player.rect.x + self.player.width / 2
        self.rect.y = self.player.rect.y + self.player.height / 2

# class Projectile(Sprite):
#     def __init__(self):
#         Sprite.__init__(self)
#         self.width = 5
#         self.height = 5
#         self.image = pg.Surface((self.width, self.height))
#         self.image.fill(WHITE)
#         self.rect = self.image.get_rect()
#     def update(self):
