import pygame
from conf import settings


class Bullet(pygame.sprite.Sprite):

    def __init__(self,centerx,top):
        super().__init__()
        self.image = pygame.image.load(r'%s\material\image\bullet1.png'%settings.BASE_DIR)
        self.rect = self.image.get_rect()

        self.rect.centerx = centerx
        self.rect.bottom = top -20

        # 获得掩膜，方便碰撞检测
        self.mask = pygame.mask.from_surface(self.image)

        self.speed = 5

        self.active=True

    def update(self, *args):
        if self.rect.top > - self.rect.height:
            self.rect.y -= self.speed
        else:
            self.kill()
