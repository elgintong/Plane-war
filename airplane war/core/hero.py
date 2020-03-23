#! /usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from conf import settings
from core import bullet

class Plane(pygame.sprite.Sprite):

    def __init__(self,BGSIZE):
        super().__init__()
        self.image = pygame.image.load(r'%s\material\image\hero1.png'%settings.BASE_DIR)
        self.image1 = pygame.image.load(r'%s\material\image\hero2.png'%settings.BASE_DIR)
        # 获取我方飞机的位置
        self.rect = self.image.get_rect()
        # 本地化背景图片的尺寸
        self.width, self.height =BGSIZE[0],BGSIZE[1]
        # 获取飞机图像的掩膜用以更加精确的碰撞检测
        self.mask = pygame.mask.from_surface(self.image)
        # 定义飞机的初始化位置，底部预览60像素
        self.rect.left,self.rect.top =(self.width-self.rect.width)//2,self.height - self.rect.height-60
        # 定义飞机速度
        self.speed = 10
        # 设置飞机存储状态 True 存活  False 死亡
        self.active = True
        # 加载飞机损毁图片
        self.destory_images = []
        self.destory_images.extend(
            [
             pygame.image.load(r"%s\material\image\hero_blowup_n1.png" % settings.BASE_DIR),
             pygame.image.load ( r"%s\material\image\hero_blowup_n2.png" % settings.BASE_DIR ) ,
             pygame.image.load ( r"%s\material\image\hero_blowup_n3.png" % settings.BASE_DIR ) ,
             pygame.image.load ( r"%s\material\image\hero_blowup_n4.png" % settings.BASE_DIR ) ,
             ]

        )

    def move_up(self):
        """
        飞机往上移动
        :return:
        """
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def move_down(self):
        """
        飞机往下移动
        :return:
        """
        if self.rect.bottom < self.height - 60:
            self.rect.bottom += self.speed
        else:
            self.rect.bottom = self.height-60

    def move_left(self):
        """
        飞机往左移动
        :return:
        """
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def move_right(self):
        """
        飞机往右移动
        :return:
        """
        if self.rect.right < self.width:
            self.rect.right += self.speed
        else:
            self.rect.right = self.width

    def reset(self):
        """
        重新生成英雄飞机对象
        :return:
        """
        # 初始化英雄飞机的位置
        self.rect.left,self.rect.top = (self.width-self.rect.width)//2,self.height-self.rect.height-60
        # 飞机状态设为 True
        self.active = True

    def fire(self):

        for i in range(4):
            bullet1 = bullet.Bullet ()
            bullet1.rect.centerx = self.rect.centerx
            bullet1.rect.bottom = self.rect.top -20


