import pygame
import random
from conf import settings


class EnemySmall(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'%s\material\image\enemy1.png'%settings.BASE_DIR)
        self.rect = self.image.get_rect()
        # 初始化敌机位置
        self.rect.left = random.randrange(0,settings.BGSIZE[0]-self.rect.width)
        self.rect.top = random.randint(1,5)
        # 获得掩膜，方便碰撞检测
        self.mask = pygame.mask.from_surface(self.image)
        self.active=True
        self.speed = random.randint(1,3)
        self.destroy_images = []
        self.destroy_images.extend (
            [
                pygame.image.load (r"%s\material\image\enemy1_down1.png" % settings.BASE_DIR) ,
                pygame.image.load ( r"%s\material\image\enemy1_down2.png" % settings.BASE_DIR) ,
                pygame.image.load ( r"%s\material\image\enemy1_down3.png" % settings.BASE_DIR ) ,
                pygame.image.load ( r"%s\material\image\enemy1_down4.png" % settings.BASE_DIR )
            ]
        )

    def update(self, *args):
        if self.rect.bottom < settings.BGSIZE[1]:
            self.rect.y += self.speed
        else:
            self.reset()

    def reset(self):
        self.rect.left = random.randrange ( settings.BGSIZE[1] - self.rect.width )
        self.rect.top = random.randint ( 1 , 5 )
        self.active = True


class EnemyMid(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'%s\material\image\enemy2.png'%settings.BASE_DIR)
        self.rect = self.image.get_rect()
        # 初始化敌机位置
        self.rect.left = random.randrange(0,settings.BGSIZE[0]-self.rect.width)
        self.rect.top = random.randint(1,5)
        # 获得掩膜，方便碰撞检测
        self.mask = pygame.mask.from_surface(self.image)
        self.active=True
        self.energy = 9
        self.speed = random.randint(1,3)
        self.destroy_images = []
        self.destroy_images.extend (
            [
                pygame.image.load (r"%s\material\image\enemy1_down1.png" % settings.BASE_DIR) ,
                pygame.image.load ( r"%s\material\image\enemy1_down2.png" % settings.BASE_DIR) ,
                pygame.image.load ( r"%s\material\image\enemy1_down3.png" % settings.BASE_DIR ) ,
                pygame.image.load ( r"%s\material\image\enemy1_down4.png" % settings.BASE_DIR )
            ]
        )

    def update(self, *args):
        if self.rect.bottom < settings.BGSIZE[1]:
            self.rect.y += self.speed
        else:
            self.reset()

    def reset(self):
        self.rect.left = random.randrange ( settings.BGSIZE[1] - self.rect.width )
        self.rect.top = random.randint ( 1 , 5 )
        self.active = True
