import sys

import pygame

import constants
from game.plane import OurPlane


def main():
    pygame.init()
    width,height = 480,852                              #设置游戏屏幕宽和高
    screen = pygame.display.set_mode((width, height))   #加载屏幕对象
    pygame.display.set_caption('飞机大战')                #设置标题
    bg = pygame.image.load(constants.BG_IMG)            #加载游戏背景图片
    img_game_title = pygame.image.load(constants.IMG_GAME_TITLE)    #加载游戏标题的图片
    t_width,t_height = img_game_title.get_size()        #获取游戏标题图片的宽和高
    img_game_title_rect = img_game_title.get_rect()     #获取游戏标题图片的位置
    img_game_title_rect.left = (width - t_width) // 2   #使游戏标题图片位于屏幕中央
    img_game_title_rect.top = (height // 2 - t_height)  #使游戏标题图片位于屏幕中央
    btn_start = pygame.image.load(constants.IMG_GAME_START_BTN)     #获取开始按钮
    btn_width,btn_height = btn_start.get_size()         #获取开始按钮的宽高
    btn_start_rect = btn_start.get_rect()               #获取开始按钮的位置
    btn_start_rect.left = (width - btn_width) // 2        #使开始按钮位于屏幕中央
    btn_start_rect.top = (height // 2 + btn_height)       #使开始按钮位于屏幕中央

    pygame.mixer.music.load(constants.BG_MUSIC)         #加载游戏背景音乐
    pygame.mixer.music.play(-1)                         #设置无限播放模式

    '''设置游戏的状态，并将状态设置为准备'''
    READY = 0
    PLAYING = 1
    OVER = 2
    status = READY

    frame = 0       #设置帧数变量
    ourplane = OurPlane(screen)

    clock = pygame.time.Clock() #设置帧数

    while True:
        clock.tick(60)
        frame += 1
        if frame >= 60:
            frame = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if status == READY:
                    status = PLAYING
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    ourplane.move_up()
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    ourplane.move_down()
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    ourplane.move_left()
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    ourplane.move_right()
                elif event.key == pygame.K_SPACE:
                    ourplane.shoot()

        if status == READY:
            screen.blit(bg,bg.get_rect())
            screen.blit(img_game_title,img_game_title_rect)
            screen.blit(btn_start,btn_start_rect)
        elif status == PLAYING:
            screen.blit(bg, bg.get_rect())
            ourplane.update(frame)
            ourplane.bullets.update()

        pygame.display.flip()


if __name__ == '__main__':
    main()
