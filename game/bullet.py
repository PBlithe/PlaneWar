import pygame

import constants


class Bullet(pygame.sprite.Sprite):
    active = True

    def __init__(self,screen,plane,speed=None):
        super().__init__()
        self.screen = screen
        self.plane = plane
        self.speed = speed or 10
        self.image = pygame.image.load(constants.BULLET_IMG)
        self.rect = self.image.get_rect()
        self.rect.centerx = plane.rect.centerx  #设置子弹在屏幕中的位置
        self.rect.top = plane.rect.top          #设置子弹在屏幕中的位置
        self.shoot_sound = pygame.mixer.Sound(constants.BULLET_SHOOT_SOUND)
        self.shoot_sound.set_volume(0.3)
        self.shoot_sound.play()

    def update(self, *args):
        self.rect.top -= self.speed
        self.screen.blit(self.image,self.rect)
        if self.rect.top <= 0:
            self.remove(self.plane.bullets)
