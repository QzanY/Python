import pygame
import sys
from pygame.locals import *
import random

pygame.init()

vec = pygame.math.Vector2

HEIGHT = 600
WIDTH = 800
FPS = 60
FramePerSec = pygame.time.Clock()
pygame.mixer.music.load("mrbeast.mp3")
pygame.mixer.music.play()

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
        self.pos = vec((90,HEIGHT-25))
        self.acc = vec(0,0)
        self.jumping = False
        self.walking = False
        self.falling = False
        self.climbing = False
        self.declimbing = False
        self.dead = False

    def move(self):
        self.acc = vec(0,0.25)
        pressed_keys = pygame.key.get_pressed()
        hits2 = pygame.sprite.spritecollide(P1,ladders,False)
        hits = pygame.sprite.spritecollide(P1,platforms,False)
        if pressed_keys[K_a]:
            print(len(barrels))
        if pressed_keys[K_LEFT] and self.climbing == False and self.declimbing == False:
            if (hits and self.pos.y < hits[0].rect.bottom) or (not(hits) or self.jumping):
                self.walking = True
                if self.pos.x < self.width/2:
                    self.pos.x = 0 + (self.width/2)
                else:
                    self.pos.x -= self.vel.x

        elif pressed_keys[K_RIGHT] and self.climbing == False and self.declimbing == False:
            if (hits and self.pos.y < hits[0].rect.bottom) or (not(hits) or self.jumping):
                self.walking = True
                if self.pos.x > WIDTH-self.width/2:
                    self.pos.x = WIDTH-(self.width/2)
                else:
                    self.pos.x += self.vel.x

        elif pressed_keys[K_UP] and hits2 and not(self.jumping):
            if 570+80<=self.pos.x<=580+80 or 60+80<=self.pos.x<=70+80 or 220+80<=self.pos.x<=230+80 or 266+80<=self.pos.x<=276+80 or 170+80<=self.pos.x<=180+80 or 330+80<=self.pos.x<=340+80 or 196+80<=self.pos.x<=206+80 or 510+80<=self.pos.x<=520+80 or 250+80<=self.pos.x<=260+80 or 380+80<=self.pos.x<=390+80:
                self.climbing = True
                self.declimbing = False
                self.climb()

        elif pressed_keys[K_DOWN] and hits2 and not(self.jumping):
            if (570+80<=self.pos.x<=580+80 or 60+80<=self.pos.x<=70+80 or 220+80<=self.pos.x<=230+80 or 266+80<=self.pos.x<=276+80 or 170+80<=self.pos.x<=180+80 or 330+80<=self.pos.x<=340+80 or 196+80<=self.pos.x<=206+80 or 510+80<=self.pos.x<=520+80 or 250+80<=self.pos.x<=260+80 or 380+80<=self.pos.x<=390+80) and self.pos.y < hits2[0].rect.bottom+1:
                self.declimbing = True
                self.climbing = False
                self.declimb()

        if self.jumping==True and self.climbing==False and self.declimbing == False:
            self.vel.y += self.acc.y
            self.pos.y += self.vel.y/1.5
        elif self.jumping==True and (self.climbing==True or self.declimbing == True):
            self.jumping = False

        self.rect.midbottom = self.pos

    def jump(self):
        if self.jumping == False:
            self.vel.y -= 6
            self.jumping = True

    def climb(self):
        self.pos.y -= 1

    def declimb(self):
        self.pos.y += 1

    def update(self):
        hits = pygame.sprite.spritecollide(P1,platforms,False)
        hits2 = pygame.sprite.spritecollide(P1,ladders,False)
        hits3 = pygame.sprite.spritecollide(P1,barrels,False)
        if hits3:
            self.dead = True
        if hits:
            if self.pos.y < hits[0].rect.bottom and self.declimbing==False:
                self.falling = False
                self.jumping = False
                self.climbing = False
                self.declimbing = False
                self.pos.y = hits[0].rect.top + 1
                self.vel.y = 0
            else:
                self.declimbing = False

        elif self.jumping == False and self.climbing == False and self.declimbing == False:
            self.vel.y += self.acc.y
            self.pos.y += self.vel.y/1.5
        elif hits2:
            pass

        else:
            self.declimbing = False
            self.climbing = False


class Barrel(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        super().__init__()
        self.size = self.width,self.height = 30,30
        self.surf = pygame.Surface((self.width,self.height))
        self.surf.fill((90,50,10))
        self.rect = self.surf.get_rect(bottomleft=(posx,posy))
        self.vel = vec(2,0)
        self.pos = vec((posx,posy))
        self.rolling = True  
        self.falling = False
        self.xvel = 3
        self.yvel = 1
        self.direction = 1

    def move(self):
        if self.rolling:
            self.falling = False
            self.xvel = 3
            self.yvel = 1
            if self.pos.x < 15:
                self.direction *= -1
                self.pos.x = 0 + (self.width/2)
            elif self.pos.x >= WIDTH-self.width:
                self.direction *= -1
                self.pos.x = WIDTH-(self.width)-1
            self.vel = vec(self.xvel*self.direction,self.yvel)
            self.pos += self.vel
        elif self.falling:
            self.rolling = False
            self.xvel = 0
            self.yvel = 2
            self.vel = vec(self.xvel*self.direction,self.yvel)
            self.pos += self.vel
        elif self.falling2:
            self.falling = False
            self.rolling = False
            self.xvel = 3
            self.yvel = 2
            if self.pos.x < 0:
                self.direction *= -1
                self.pos.x = 1
            elif self.pos.x >= WIDTH-self.width:
                self.direction *= -1
                self.pos.x = WIDTH-(self.width)-1
            self.vel = vec(self.xvel*self.direction,self.yvel)
            self.pos += self.vel
        self.rect.bottomleft = self.pos

    def update(self):
        if 15<=self.pos.x<=30 and HEIGHT-30<=self.pos.y<=HEIGHT-20:
            self.kill()
        hitss = pygame.sprite.spritecollide(self,platforms,False)
        hitss2 = pygame.sprite.spritecollide(self,hladders,False)
        if hitss:
            if hitss2:
                if (hitss2[0].rect.bottomleft[0] <= self.pos.x <= hitss2[0].rect.bottomleft[0]+3) and (hitss2[0].rect.topleft[1]-3 <= self.pos.y <= hitss2[0].rect.topleft[1]+hitss2[0].height-30):
                    if (hitss2[0].rect.topleft[1]-3 <= self.pos.y <= hitss2[0].rect.topleft[1]+2):
                        global RNG
                        RNG = random.randint(0,1)
                        if RNG ==0:
                            pass
                        else:
                            self.direction *=-1
                    if RNG !=0:
                        self.falling = True
                        self.rolling = False

                else:
                    self.rolling = True
                    self.falling = False
                    self.pos.y = hitss[0].rect.top+1
            else:
                self.rolling = True
                self.falling = False
                self.pos.y = hitss[0].rect.top+1
        elif hitss2:
            self.falling = True
            self.rolling = False

        else:
            self.falling2 = True
            self.rolling = False
            self.falling = False
            

class Platform(pygame.sprite.Sprite):
    def __init__(self,width,height,posx,posy):
        super().__init__()
        self.surf = pygame.Surface((width,height))
        self.surf.fill((255,0,255))
        self.rect = self.surf.get_rect(bottomleft=(posx,posy))

class Ladder(pygame.sprite.Sprite):
    def __init__(self,height,posx,posy):
        super().__init__()
        self.surf = pygame.Surface((30,height))
        self.surf.fill((0,20,255))
        self.rect = self.surf.get_rect(bottomleft=(posx,posy))

class hLadder(pygame.sprite.Sprite):
    def __init__(self,height,posx,posy):
        super().__init__()
        self.height = height
        self.surf = pygame.Surface((30,height))
        self.surf.fill((0,0,0))
        self.rect = self.surf.get_rect(bottomleft=(posx,posy))

class fLadder(pygame.sprite.Sprite):
    def __init__(self,height,posx,posy):
        super().__init__()
        self.surf = pygame.Surface((30,height))
        self.surf.fill((0,20,255))
        self.rect = self.surf.get_rect(bottomleft=(posx,posy))

def gameOverScreen(flag:int):
    if flag:
        pygame.time.delay(2000)
        display_surface.fill((0,0,0))
        winFont = pygame.font.SysFont('comicsans', 80)
        winText = winFont.render("You Win!!!",1,(255,255,255))
        textRect = winText.get_rect()
        textRect.center = (WIDTH/2,HEIGHT/2)
        display_surface.blit(winText,textRect)
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()
    else:
        pygame.time.delay(2000)
        display_surface.fill((0,0,0))
        winFont = pygame.font.SysFont('comicsans', 80)
        winText = winFont.render("You Lose",1,(255,255,255))
        textRect = winText.get_rect()
        textRect.center = (WIDTH/2,HEIGHT/2)
        display_surface.blit(winText,textRect)
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()
    

P1 = Player()
start_ticks = pygame.time.get_ticks()
barrels = pygame.sprite.Group()

# barrels.add(Barrel(30,HEIGHT-503))
# barrels.add(Barrel(70,HEIGHT-503))
# barrels.add(Barrel(130,HEIGHT-503))



PT1_01 = Platform(80,15,0,HEIGHT-12)
PT1_1 = Platform(WIDTH/2,15,0+80,HEIGHT-12)
PT1_2 = Platform(80,15,320+80,HEIGHT-14)
PT1_3 = Platform(80,15,400+80,HEIGHT-16)
PT1_4 = Platform(80,15,480+80,HEIGHT-18)
PT1_5 = Platform(80,15,560+80,HEIGHT-20)
PT1_6 = Platform(80,15,560+80+80,HEIGHT-22)

PT2_01 = Platform(80,15,0,HEIGHT-108)
PT2_1 = Platform(80,15,0+80,HEIGHT-107)
PT2_2 = Platform(80,15,80+80,HEIGHT-106)
PT2_3 = Platform(80,15,160+80,HEIGHT-105)
PT2_4 = Platform(80,15,240+80,HEIGHT-104)
PT2_5 = Platform(80,15,320+80,HEIGHT-103)
PT2_6 = Platform(80,15,400+80,HEIGHT-102)
PT2_7 = Platform(80,15,480+80,HEIGHT-101)
PT2_8 = Platform(80,15,560+80,HEIGHT-100)

PT3_1 = Platform(80,15,0+80,HEIGHT-195)
PT3_2 = Platform(80,15,80+80,HEIGHT-196)
PT3_3 = Platform(80,15,160+80,HEIGHT-197)
PT3_4 = Platform(80,15,240+80,HEIGHT-198)
PT3_5 = Platform(80,15,320+80,HEIGHT-199)
PT3_6 = Platform(80,15,400+80,HEIGHT-200)
PT3_7 = Platform(80,15,480+80,HEIGHT-201)
PT3_8 = Platform(80,15,560+80,HEIGHT-202)
PT3_9 = Platform(80,15,560+80+80,HEIGHT-203)

PT4_01 = Platform(80,15,0,HEIGHT-298)
PT4_1 = Platform(80,15,0+80,HEIGHT-297)
PT4_2 = Platform(80,15,80+80,HEIGHT-296)
PT4_3 = Platform(80,15,160+80,HEIGHT-295)
PT4_4 = Platform(80,15,240+80,HEIGHT-294)
PT4_5 = Platform(80,15,320+80,HEIGHT-293)
PT4_6 = Platform(80,15,400+80,HEIGHT-292)
PT4_7 = Platform(80,15,480+80,HEIGHT-291)
PT4_8 = Platform(80,15,560+80,HEIGHT-290)

PT5_1 = Platform(80,15,0+80,HEIGHT-385)
PT5_2 = Platform(80,15,80+80,HEIGHT-386)
PT5_3 = Platform(80,15,160+80,HEIGHT-387)
PT5_4 = Platform(80,15,240+80,HEIGHT-388)
PT5_5 = Platform(80,15,320+80,HEIGHT-389)
PT5_6 = Platform(80,15,400+80,HEIGHT-390)
PT5_7 = Platform(80,15,480+80,HEIGHT-391)
PT5_8 = Platform(80,15,560+80,HEIGHT-392)
PT5_9 = Platform(80,15,560+80+80,HEIGHT-393)

PT6_01 = Platform(80,15,0,HEIGHT-488)
PT6_1 = Platform(320,15,0+80,HEIGHT-488)
PT6_2 = Platform(80,15,320+80,HEIGHT-486)
PT6_3 = Platform(80,15,400+80,HEIGHT-484)
PT6_4 = Platform(80,15,480+80,HEIGHT-482)
PT6_5 = Platform(80,15,560+80,HEIGHT-481)

PT7_1 = Platform(80,15,160+80,70)
PT7_2 = Platform(160,15,240+80,55)

HL1_1 = hLadder(93,210+80,HEIGHT-27)
HL2 = hLadder(80,560+80,HEIGHT-35)
HL3 = hLadder(88,50+80,HEIGHT-122)
HL4 = hLadder(94,256+80,HEIGHT-119)
HL5_1 = hLadder(98,160+80,HEIGHT-212)
HL6 = hLadder(94,320+80,HEIGHT-214)
HL7 = hLadder(88,560+80,HEIGHT-217)
HL8 = hLadder(88,50+80,HEIGHT-312)
HL9 = hLadder(92,186+80,HEIGHT-310)
HL10_1 = hLadder(100,506+80,HEIGHT-306)
HL11_1 = hLadder(100,240+80,HEIGHT-403)
HL12 = hLadder(88,560+80,HEIGHT-408)

L1_1 = Ladder(30,210+80,HEIGHT-27)
F1_2 = fLadder(30,210+80,HEIGHT-80)
L2 = Ladder(80,560+80,HEIGHT-35)
L3 = Ladder(88,50+80,HEIGHT-122)
L4 = Ladder(94,256+80,HEIGHT-119)
L5_1 = Ladder(40,160+80,HEIGHT-212)
F5_2 = fLadder(20,160+80,HEIGHT-275)
L6 = Ladder(94,320+80,HEIGHT-214)
L7 = Ladder(88,560+80,HEIGHT-217)
L8 = Ladder(88,50+80,HEIGHT-312)
L9 = Ladder(92,186+80,HEIGHT-310)
L10_1 = Ladder(30,506+80,HEIGHT-306)
F10_2 = fLadder(21,506+80,HEIGHT-370)
L11_1 = Ladder(30,240+80,HEIGHT-403)
F11_2 = fLadder(30,240+80,HEIGHT-463)
L12 = Ladder(89,560+80,HEIGHT-407)
L13 = Ladder(HEIGHT-551,370+80,HEIGHT-501)
L14 = Ladder(200,160+80,HEIGHT-488)
L15 = Ladder(200,240-30+80,HEIGHT-488)

hladders = pygame.sprite.Group()
hladders.add(HL1_1)
hladders.add(HL2)
hladders.add(HL3)
hladders.add(HL4)
hladders.add(HL5_1)
hladders.add(HL6)
hladders.add(HL7)
hladders.add(HL8)
hladders.add(HL9)
hladders.add(HL10_1)
hladders.add(HL11_1)
hladders.add(HL12)


ladders = pygame.sprite.Group()
ladders.add(L1_1)
ladders.add(L2)
ladders.add(L3)
ladders.add(L4)
ladders.add(L5_1)
ladders.add(L6)
ladders.add(L7)
ladders.add(L8)
ladders.add(L9)
ladders.add(L10_1)
ladders.add(L11_1)
ladders.add(L12)
ladders.add(L13)
ladders.add(L14)
ladders.add(L15)

platforms = pygame.sprite.Group()
platforms.add(PT1_01)
platforms.add(PT1_1)
platforms.add(PT1_2)
platforms.add(PT1_3)
platforms.add(PT1_4)
platforms.add(PT1_5)
platforms.add(PT1_6)

platforms.add(PT2_01)
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
platforms.add(PT3_9)

platforms.add(PT4_01)
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
platforms.add(PT5_9)

platforms.add(PT6_01)
platforms.add(PT6_1)
platforms.add(PT6_2)
platforms.add(PT6_3)
platforms.add(PT6_4)
platforms.add(PT6_5)

platforms.add(PT7_1)
platforms.add(PT7_2)

all_sprites = pygame.sprite.Group()

all_sprites.add(HL1_1)
all_sprites.add(HL2)
all_sprites.add(HL3)
all_sprites.add(HL4)
all_sprites.add(HL5_1)
all_sprites.add(HL6)
all_sprites.add(HL7)
all_sprites.add(HL8)
all_sprites.add(HL9)
all_sprites.add(HL10_1)
all_sprites.add(HL11_1)
all_sprites.add(HL12)

all_sprites.add(L1_1)
# all_sprites.add(L1_2)
all_sprites.add(L2)
all_sprites.add(L3)
all_sprites.add(L4)
all_sprites.add(L5_1)
all_sprites.add(L6)
all_sprites.add(L7)
all_sprites.add(L8)
all_sprites.add(L9)
all_sprites.add(L10_1)
all_sprites.add(L11_1)
all_sprites.add(L12)
all_sprites.add(L13)
all_sprites.add(L14)
all_sprites.add(L15)
all_sprites.add(F1_2)
all_sprites.add(F5_2)
all_sprites.add(F10_2)
all_sprites.add(F11_2)


all_sprites.add(PT1_01)
all_sprites.add(PT1_1)
all_sprites.add(PT1_2)
all_sprites.add(PT1_3)
all_sprites.add(PT1_4)
all_sprites.add(PT1_5)
all_sprites.add(PT1_6)

all_sprites.add(PT2_01)
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
all_sprites.add(PT3_9)

all_sprites.add(PT4_01)
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
all_sprites.add(PT5_9)

all_sprites.add(PT6_01)
all_sprites.add(PT6_1)
all_sprites.add(PT6_2)
all_sprites.add(PT6_3)
all_sprites.add(PT6_4)
all_sprites.add(PT6_5)
all_sprites.add(PT7_1)
all_sprites.add(PT7_2)
all_sprites.add(P1)
# all_sprites.add(B1)
for barrel in barrels:
    all_sprites.add(barrel)

#Main Loop -----------------------------------------

run = True
while run:
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
    now = pygame.time.get_ticks()
    seconds = (now-start_ticks)/1000
    if 2.99<seconds<3.01:
        start_ticks=now
        barrel1 = Barrel(90,HEIGHT-503)
        barrels.add(barrel1)
        all_sprites.add(barrel1)
    for barrel in barrels:
        barrel.move()
        barrel.update()
    if P1.dead:
        pygame.mixer.quit()
        gameOverScreen(False)
    if 320<P1.pos.x<480 and 38<P1.pos.y<41 and P1.climbing == False and P1.declimbing == False:
        for entity in all_sprites:
            display_surface.blit(entity.surf,entity.rect)
        pygame.display.update()
        pygame.mixer.quit()
        gameOverScreen(True)
    for entity in all_sprites:
        display_surface.blit(entity.surf,entity.rect)

    pygame.display.update()
    FramePerSec.tick(FPS)
