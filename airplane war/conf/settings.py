#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import pygame
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# 定义刷新频率
FRAME_SEC = 60

BGSIZE = 480,852 # 设置游戏背景大小常量
pygame.display.set_caption('飞机大战') # 设置游戏名字

pygame.init() # 游戏初始化
pygame.mixer.init() # 游戏混音器初始化

ENEMY1_CREAT_EVENT = pygame.USEREVENT # 小敌机产生的定时器常量
ENEMY2_CREAT_EVENT = pygame.USEREVENT +1 # 中敌机产生的定时器常量
HERO_FIRE_EVENT = pygame.USEREVENT + 2 # 子弹发射的定时器常量

# 游戏背景音乐
pygame.mixer.music.load(os.path.join(BASE_DIR,'material/sound/game_music.wav'))
pygame.mixer.music.set_volume(0.2)

# # 子弹发射音乐
# bullet_sound = pygame.mixer.Sound(os.path.join(BASE_DIR,'material/sound/bullet.wav'))
# bullet_sound.set_volume(0.2)
#
# # 我方飞机挂了音乐
# hero_die_sound = pygame.mixer.Sound(os.path.join(BASE_DIR,'material/sound/game_over.wav'))
# hero_die_sound.set_volume(0.2)
#
# # 敌方飞机挂了音乐
# eney_die_sound = pygame.mixer.Sound(os.path.join(BASE_DIR,'material/sound/enemy1_down.wav'))
# eney_die_sound.set_volume(0.2)


def music_event(file_path,volume = 0.2):
    music = pygame.mixer.Sound(file_path)
    music.set_volume(volume)
    music.play()


