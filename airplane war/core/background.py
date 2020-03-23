import pygame
from conf import settings


class BackGround(pygame.sprite.Sprite):

    def __init__(self,image_file,speed = 1,is_alt = False):
        super().__init__()
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.top, self.rect.left = 0 ,0
        self.speed = speed

        if is_alt is True:
            self.rect.top = -settings.BGSIZE[1]

    def update(self, *args):
        if self.rect.top < settings.BGSIZE[1]:
            self.rect.top += self.speed
        else:
            self.rect.top = -settings.BGSIZE[1]
