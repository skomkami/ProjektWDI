import pygame


class Images:
    def __init__(self):
        self.background = pygame.image.load("pictures/image.jpg")
        self.ball = pygame.image.load("pictures/ball.png")
        self.pallet = pygame.image.load("pictures/paletka1.png")
        self.pallet_s = pygame.image.load("pictures/paletka1_s.png")
        self.pallet2 = pygame.image.load("pictures/paletka2.png")
        self.pallet2_s = pygame.image.load("pictures/paletka2_s.png")
        self.wall = pygame.image.load("pictures/wall.png")
        self.wall2 = pygame.image.load("pictures/wall2.png")
        self.h_wall = pygame.image.load("pictures/h_wall.png")
        self.h_wall2 = pygame.image.load("pictures/h_wall2.png")
        self.block_yellow = pygame.image.load("pictures/block_yellow.png")
        self.block_red = pygame.image.load("pictures/block_red.png")
        self.block_green = pygame.image.load("pictures/block_green.png")
        self.block_gold = pygame.image.load("pictures/block_gold.png")
        self.bullet = pygame.image.load("pictures/bullet.png")


class Sounds:
    def __init__(self):
        self.boop_sound = pygame.mixer.Sound('sounds/boop.wav')
        self.bloop_sound = pygame.mixer.Sound('sounds/bloop.wav')
        self.explosion_sound = pygame.mixer.Sound('sounds/explosion.wav')
        self.win_sound = pygame.mixer.Sound('sounds/tada.wav')
        self.shoot_sound = pygame.mixer.Sound('sounds/shoot.wav')


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        pictures = Images()
        self.image = pictures.bullet
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 670

    def move(self):
        self.rect.y -= 5


class Pallet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pictures = Images()
        self.create(self.pictures.pallet, x, y)

    def create(self, pic, x, y):
        self.image = pic
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.width = self.rect.right - self.rect.x

    def get_bigger(self, x, y):
        self.create(self.pictures.pallet2, x, y)

    def get_gun(self, x, y):
        self.create(self.pictures.pallet2_s, x, y)

    def reset(self, x, y):
        self.create(self.pictures.pallet, x, y)


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        pictures = Images()
        self.image = pictures.ball
        self.rect = self.image.get_rect()
        self.reset(x, y)

    def reset(self, x, y):
        self.rect.y = y
        self.rect.x = x

    def bounce(self, object, a, b):
        turnA, turnB = 1, 1

        if b == 0:
            turnA = -turnA
        elif (b > 0 and a < 0):
            if (self.rect.y < object.rect.bottom - 5):
                turnB = -turnB
            else:  # (self.rect.right > object.rect.x + 9):
                turnA = -turnA
        elif (b < 0 and a < 0):
            if (self.rect.x < object.rect.right - 9):
                turnA = -turnA
            else:  # (self.rect.y < object.rect.bottom - 5):#
                turnB = -turnB
        elif (b > 0 and a > 0):
            if (self.rect.right > object.rect.x + 9):#
                turnA = -turnA
            else: #(self.rect.bottom > object.rect.y + 5):
                turnB = -turnB
        elif (b < 0 and a > 0):
            if (self.rect.x < object.rect.right - 9):#
                turnA = -turnA
            else: #(self.rect.bottom > object.rect.y + 5):
                turnB = -turnB

        return [turnA, turnB]

    def pallet_bat(self, pallet, a, b):
        turnA, turnB = a, b

        if self.rect.bottom > pallet.rect.y + 5:
            turnB = -turnB
        elif ((self.rect.x + self.rect.right) / 2) < (pallet.rect.x + (pallet.rect.right - pallet.rect.x) / 7):
            turnB = -1.7
            turnA = -turnA
        elif ((self.rect.x + self.rect.right) / 2) >= (pallet.rect.x + (pallet.rect.right - pallet.rect.x) / 7) and (
                (self.rect.x + self.rect.right) / 2) < (pallet.rect.x + (pallet.rect.right - pallet.rect.x) / 7 * 2):
            turnB = -1
            turnA = -turnA
        elif ((self.rect.x + self.rect.right) / 2) >= (pallet.rect.x + (pallet.rect.right - pallet.rect.x) / 7 * 2) and (
                (self.rect.x + self.rect.right) / 2) < (pallet.rect.x + (pallet.rect.right - pallet.rect.x) / 7 * 3):
            turnB = -0.6
            turnA = -turnA
        elif ((self.rect.x + self.rect.right) / 2) >= (pallet.rect.x + (pallet.rect.right - pallet.rect.x) / 7 * 3) and (
                (self.rect.x + self.rect.right) / 2) < (pallet.rect.x + (pallet.rect.right - pallet.rect.x) / 7 * 4):
            turnB = 0
            turnA = -turnA
        elif ((self.rect.x + self.rect.right) / 2) >= (pallet.rect.x + (pallet.rect.right - pallet.rect.x) / 7 * 4) and (
                (self.rect.x + self.rect.right) / 2) < (pallet.rect.x + (pallet.rect.right - pallet.rect.x) / 7 * 5):
            turnB = 0.6
            turnA = -turnA
        elif ((self.rect.x + self.rect.right) / 2) >= (pallet.rect.x + (pallet.rect.right - pallet.rect.x) / 7 * 5) and (
                (self.rect.x + self.rect.right) / 2) < (pallet.rect.x + (pallet.rect.right - pallet.rect.x) / 7 * 6):
            turnB = 1
            turnA = -turnA
        elif ((self.rect.x + self.rect.right) / 2) >= (pallet.rect.x + (pallet.rect.right - pallet.rect.x) / 7 * 6) and (
                (self.rect.x + self.rect.right) / 2) < (pallet.rect.x + (pallet.rect.right - pallet.rect.x)):
            turnB = 1.7
            turnA = -turnA

        return [turnA, turnB]


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, number):
        pygame.sprite.Sprite.__init__(self)
        pictures = Images()
        if number == 1:
            self.image = pictures.wall
        elif number == 2:
            self.image = pictures.wall2

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class HorWall(pygame.sprite.Sprite):
    def __init__(self, x, y, number):
        pygame.sprite.Sprite.__init__(self)
        pictures = Images()
        if number == 1:
            self.image = pictures.h_wall
        elif number == 2:
            self.image = pictures.h_wall2

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Blocks(pygame.sprite.Sprite):
    def __init__(self, x, y, number):
        pygame.sprite.Sprite.__init__(self)
        pictures = Images()
        if number == 1:
            self.image = pictures.block_green
        elif number == 2:
            self.image = pictures.block_yellow
        elif number == 3:
            self.image = pictures.block_red
        elif number == 4:
            self.image = pictures.block_gold

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
