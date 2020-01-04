import pygame

import constants
from game.bullet import Bullet


class Plane(pygame.sprite.Sprite):
    plane_images = []                   #飞机图片
    active = True                       #存货状态
    bullets = pygame.sprite.Group()     #子弹发射精灵组

    def __init__(self,screen,speed=None):
        super().__init__()
        self.screen = screen
        self.img_list = []  #飞机图片静态资源列表
        self.speed = speed or 10

        self.load_scr()     #加载静态资源

        self.rect = self.img_list[0].get_rect() #获取飞机的位置

        self.plane_w,self.plane_h = self.img_list[0].get_size()   #获取飞机的宽和高
        self.width,self.height = self.screen.get_size()           #游戏窗口的宽和高
        self.rect.left = (self.width - self.plane_w) // 2         #设置飞机的左边距
        self.rect.top = self.height // 2                     #设置飞机的上边距

    def load_scr(self):
        if self.plane_images:
            for i in range(len(self.plane_images)):
                self.img_list.append(pygame.image.load(self.plane_images[i]))

    @property
    def image(self):    #以属性的访问定义方法,返回img_list中保存的第一个元素
        return self.img_list[0]

    def blit_me(self):
        self.screen.blit(self.image,self.rect)

    def move_up(self):              #飞机向上移动
        self.rect.top -= self.speed

    def move_down(self):            #飞机向下移动
        self.rect.down += self.speed

    def move_left(self):            #飞机向左移动
        self.rect.left -= self.speed

    def move_right(self):           #飞机向右移动
        self.rect.right += self.speed

    def shoot(self):                #飞机发射子弹
        bullet = Bullet(self.screen,self,15)    #实现子弹类,屏幕 飞机 速度
        self.bullets.add(bullet)


class OurPlane(Plane):
    plane_images = [constants.OUR_PLANE_IMG_1,constants.OUR_PLANE_IMG_2]

    def update(self, frame):        #设置飞机的飞行效果
        if frame % 5:
            self.screen.blit(self.image,self.rect)
        else:
            self.screen.blit(self.img_list[1],self.rect)

    def move_up(self):              #飞机向上移动
        super().move_up()
        if self.rect.top <= 0:
            self.rect.top = 0

    def move_down(self):            #飞机向下移动
        super().move_down()
        if self.rect.down >= self.height:
            self.rect.down = self.height

    def move_left(self):            #飞机向左移动
        super(OurPlane, self).move_left()
        if self.rect.left <= 0:
            self.rect.left = 0

    def move_right(self):           #飞机向右移动
        super(OurPlane, self).move_right()
        if self.rect.right >= self.width:
            self.rect.right = self.width
