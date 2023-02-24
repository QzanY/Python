import pygame
import sys
from pygame.locals import *

pygame.init()

vec = pygame.math.Vector2

HEIGHT = 600
WIDTH = 640
FPS = 60
FramePerSec = pygame.time.Clock()

display_surface = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Konkey Dong")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = self.width,self.height = 27,40
        self.surf = pygame.Surface(self.size)
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect(center = (10,HEIGHT-75))
        self.vel = vec(2,0)
        self.health = 3
        self.pos = vec((10,HEIGHT-25))
        self.acc = vec(0,0)
        self.jumping = False
        self.walking = False
        self.falling = False
        self.level = 1

    def move(self):
        self.acc = vec(0,0.25)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.walking = True
            if self.pos.x < 0:
                self.pos.x = 0 + (self.width/2)
            else:
                self.pos.x -= self.vel.x

        elif pressed_keys[K_RIGHT]:
            self.walking = True
            if self.pos.x > WIDTH:
                self.pos.x = WIDTH-(self.width/2)
            else:
                self.pos.x += self.vel.x
        if self.jumping:
            self.vel.y += self.acc.y
            self.pos.y += self.vel.y/1.5
        self.rect.midbottom = self.pos

    def jump(self):
        if self.jumping == False:
            self.vel.y -= 6
            self.jumping = True

    def update(self):
        hits = pygame.sprite.spritecollide(P1,platforms,False)
        if hits:
            if self.pos.y < hits[0].rect.bottom:
                self.falling = False
                self.jumping = False
                self.pos.y = hits[0].rect.top + 1
                self.vel.y = 0
        elif self.jumping == False:
            self.vel.y += self.acc.y
            self.pos.y += self.vel.y


class Platform(pygame.sprite.Sprite):
    def __init__(self,width,height,posx,posy):
        super().__init__()
        self.surf = pygame.Surface((width,height))
        self.surf.fill((255,0,255))
        self.rect = self.surf.get_rect(bottomleft=(posx,posy))

class Barrel:
    def __init__(self):
        self.size = self.width,self.height = 30,30
        self.speed = 15

P1 = Player()

PT1_1 = Platform(WIDTH/2,15,0,HEIGHT-12)
PT1_2 = Platform(80,15,320,HEIGHT-14)
PT1_3 = Platform(80,15,400,HEIGHT-16)
PT1_4 = Platform(80,15,480,HEIGHT-18)
PT1_5 = Platform(80,15,560,HEIGHT-20)

PT2_1 = Platform(80,15,0,HEIGHT-107)
PT2_2 = Platform(80,15,80,HEIGHT-106)
PT2_3 = Platform(80,15,160,HEIGHT-105)
PT2_4 = Platform(80,15,240,HEIGHT-104)
PT2_5 = Platform(80,15,320,HEIGHT-103)
PT2_6 = Platform(80,15,400,HEIGHT-102)
PT2_7 = Platform(80,15,480,HEIGHT-101)
PT2_8 = Platform(80,15,560,HEIGHT-100)

PT3_1 = Platform(80,15,0,HEIGHT-195)
PT3_2 = Platform(80,15,80,HEIGHT-196)
PT3_3 = Platform(80,15,160,HEIGHT-197)
PT3_4 = Platform(80,15,240,HEIGHT-198)
PT3_5 = Platform(80,15,320,HEIGHT-199)
PT3_6 = Platform(80,15,400,HEIGHT-200)
PT3_7 = Platform(80,15,480,HEIGHT-201)
PT3_8 = Platform(80,15,560,HEIGHT-202)

PT4_1 = Platform(80,15,0,HEIGHT-297)
PT4_2 = Platform(80,15,80,HEIGHT-296)
PT4_3 = Platform(80,15,160,HEIGHT-295)
PT4_4 = Platform(80,15,240,HEIGHT-294)
PT4_5 = Platform(80,15,320,HEIGHT-293)
PT4_6 = Platform(80,15,400,HEIGHT-292)
PT4_7 = Platform(80,15,480,HEIGHT-291)
PT4_8 = Platform(80,15,560,HEIGHT-290)

PT5_1 = Platform(80,15,0,HEIGHT-385)
PT5_2 = Platform(80,15,80,HEIGHT-386)
PT5_3 = Platform(80,15,160,HEIGHT-387)
PT5_4 = Platform(80,15,240,HEIGHT-388)
PT5_5 = Platform(80,15,320,HEIGHT-389)
PT5_6 = Platform(80,15,400,HEIGHT-390)
PT5_7 = Platform(80,15,480,HEIGHT-391)
PT5_8 = Platform(80,15,560,HEIGHT-392)

PT6_1 = Platform(320,15,0,HEIGHT-488)
PT6_2 = Platform(80,15,320,HEIGHT-486)
PT6_3 = Platform(80,15,400,HEIGHT-484)
PT6_4 = Platform(80,15,480,HEIGHT-482)
PT6_5 = Platform(80,15,560,HEIGHT-480)

PT7_1 = Platform(80,15,160,80)
PT7_2 = Platform(160,15,240,65)

platforms = pygame.sprite.Group()
platforms.add(PT1_1)
platforms.add(PT1_2)
platforms.add(PT1_3)
platforms.add(PT1_4)
platforms.add(PT1_5)

platforms.add(PT2_1)
platforms.add(PT2_2)
platforms.add(PT2_3)
platforms.add(PT2_4)
platforms.add(PT2_5)
platforms.add(PT2_6)
platforms.add(PT2_7)
platforms.add(PT2_8)

platforms.add(PT3_1)
platforms.add(PT3_2)
platforms.add(PT3_3)
platforms.add(PT3_4)
platforms.add(PT3_5)
platforms.add(PT3_6)
platforms.add(PT3_7)
platforms.add(PT3_8)

platforms.add(PT4_1)
platforms.add(PT4_2)
platforms.add(PT4_3)
platforms.add(PT4_4)
platforms.add(PT4_5)
platforms.add(PT4_6)
platforms.add(PT4_7)
platforms.add(PT4_8)

platforms.add(PT5_1)
platforms.add(PT5_2)
platforms.add(PT5_3)
platforms.add(PT5_4)
platforms.add(PT5_5)
platforms.add(PT5_6)
platforms.add(PT5_7)
platforms.add(PT5_8)

platforms.add(PT6_1)
platforms.add(PT6_2)
platforms.add(PT6_3)
platforms.add(PT6_4)
platforms.add(PT6_5)

platforms.add(PT7_1)
platforms.add(PT7_2)

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1_1)
all_sprites.add(PT1_2)
all_sprites.add(PT1_3)
all_sprites.add(PT1_4)
all_sprites.add(PT1_5)
all_sprites.add(PT2_1)
all_sprites.add(PT2_2)
all_sprites.add(PT2_3)
all_sprites.add(PT2_4)
all_sprites.add(PT2_5)
all_sprites.add(PT2_6)
all_sprites.add(PT2_7)
all_sprites.add(PT2_8)
all_sprites.add(PT3_1)
all_sprites.add(PT3_2)
all_sprites.add(PT3_3)
all_sprites.add(PT3_4)
all_sprites.add(PT3_5)
all_sprites.add(PT3_6)
all_sprites.add(PT3_7)
all_sprites.add(PT3_8)
all_sprites.add(PT4_1)
all_sprites.add(PT4_2)
all_sprites.add(PT4_3)
all_sprites.add(PT4_4)
all_sprites.add(PT4_5)
all_sprites.add(PT4_6)
all_sprites.add(PT4_7)
all_sprites.add(PT4_8)
all_sprites.add(PT5_1)
all_sprites.add(PT5_2)
all_sprites.add(PT5_3)
all_sprites.add(PT5_4)
all_sprites.add(PT5_5)
all_sprites.add(PT5_6)
all_sprites.add(PT5_7)
all_sprites.add(PT5_8)
all_sprites.add(PT6_1)
all_sprites.add(PT6_2)
all_sprites.add(PT6_3)
all_sprites.add(PT6_4)
all_sprites.add(PT6_5)
all_sprites.add(PT7_1)
all_sprites.add(PT7_2)
all_sprites.add(P1)

#Main Loop -----------------------------------------

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                P1.jump()
    display_surface.fill((0,0,0))
    P1.move()
    P1.update()
    for entity in all_sprites:
        display_surface.blit(entity.surf,entity.rect)

    pygame.display.update()
    FramePerSec.tick(FPS)
