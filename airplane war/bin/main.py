#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import pygame
from conf import settings
from core import hero
from core import background
from core import enemy
from core import bullet


class Game(object):

    def __init__(self):
        self.screen = pygame.display.set_mode ( settings.BGSIZE )  # 建立屏幕
        pygame.mixer.music.play(loops = -1) # 音乐循环播放
        self.clock = pygame.time.Clock() # 设立游戏时钟
        self.__create_sprites()
        pygame.time.set_timer(settings.ENEMY1_CREAT_EVENT,1000) # 设定小敌机出现定时器，每隔一段时间执行固定操作
        pygame.time.set_timer ( settings.ENEMY2_CREAT_EVENT , 5000 )  # 设定中敌机定时器
        pygame.time.set_timer ( settings.HERO_FIRE_EVENT , 300 )  # 设定子弹定时器

        self.score = 0
        self.life_times = 0

    def __create_sprites(self):
        """
        创建精灵与精灵组
        :return:
        """
        # 创建背景 与 背景精灵组
        bg1 = background.BackGround ( r'%s\material\image\background.png' % settings.BASE_DIR )
        bg2 = background.BackGround ( r'%s\material\image\background.png' % settings.BASE_DIR , is_alt=True )
        self.back_group = pygame.sprite.Group ( bg1 , bg2 )

        # 创建英雄飞机与英雄飞机精灵组
        self.my_plane = hero.Plane ( settings.BGSIZE )
        self.hero_group = pygame.sprite.Group(self.my_plane)

        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        self.enemy_group2 = pygame.sprite.Group ()

        # 创建子弹精灵组
        self.bullet_group = pygame.sprite.Group ()

    def update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.enemy_group2.update ()
        self.enemy_group2.draw ( self.screen )

        self.bullet_group.update ()
        self.bullet_group.draw ( self.screen )

    def check_collide(self):
        # pygame.sprite.groupcollide(self.bullet_group,self.enemy_group,True,True)
        # enemy_hit_list = pygame.sprite.groupcollide(self.bullet_group,self.enemy_group,True,True)
        # 检测小型飞机是否被击中
        for s in self.bullet_group.sprites():
            enemy_hit1 = pygame.sprite.spritecollide(s,self.enemy_group,True)
            # print(enemy_hit)
            if len(enemy_hit1)>0:
                self.score += 1
                settings.music_event(r'%s\material\sound\enemy1_down.wav' % settings.BASE_DIR)

        # 检测中型飞机是否被击中
        for s in self.bullet_group.sprites():
            enemy_hit2 = pygame.sprite.spritecollide(s,self.enemy_group2,True)
            # print(enemy_hit)
            if len(enemy_hit2)>0:
                self.score += 1
                settings.music_event(r'%s\material\sound\enemy2_down.wav' % settings.BASE_DIR)

        enemy_list = pygame.sprite.spritecollide(self.my_plane,self.enemy_group,True)
        if len(enemy_list)>0 and self.life_times<3:
            self.my_plane.reset()
            self.life_times +=1
        elif len(enemy_list)>0 and self.life_times>=3:
            quit() # TODO 英雄牺牲接口
            print(self.score)

    def start(self):
        while True:
            # screen.blit(bg,(0,0)) # blit(image,position),image表示要放置的图片，position就我目前的理解来看应该是图片左上角的x，y坐标
            # 设置刷新帧率
            self.clock.tick(settings.FRAME_SEC)
            # 事件监听
            self.event_handler()
            # 碰撞检测
            self.check_collide()
            # 更新/绘制精灵或精灵组
            self.update_sprites ()
            # 更新显示
            pygame.display.update()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == 12:
                pygame.quit()
                sys.exit()
            elif event.type == settings.ENEMY1_CREAT_EVENT:
                enemy1 = enemy.EnemySmall()
                self.enemy_group.add(enemy1)
            elif event.type == settings.ENEMY2_CREAT_EVENT:
                enemy2 = enemy.EnemyMid()
                self.enemy_group2.add(enemy2)
            elif event.type == settings.HERO_FIRE_EVENT:
                bullet1 = bullet.Bullet(self.my_plane.rect.centerx,self.my_plane.rect.top)
                settings.music_event(r'%s\material\sound\bullet.wav'% settings.BASE_DIR)
                self.bullet_group.add(bullet1)

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP] :
            self.my_plane.move_up()
        if key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
            self.my_plane.move_down()
        if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
            self.my_plane.move_left()
        if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
            self.my_plane.move_right()


if __name__ == '__main__':
    game = Game()
    game.start()


