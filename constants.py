import os

BASE_DIR = os.path.abspath('.')                                         #项目文件夹路径
ASSETS_DIR = os.path.join(BASE_DIR,'assets')                            #静态资源文件夹路径
BG_IMG = os.path.join(ASSETS_DIR,'images','background.png')             #游戏背景图片路径
IMG_GAME_TITLE = os.path.join(ASSETS_DIR,'images','game_title.png')     #飞机大战标题图片路径
IMG_GAME_START_BTN = os.path.join(ASSETS_DIR,'images','game_start.png') #游戏开始图片路径
BG_MUSIC = os.path.join(ASSETS_DIR,'sounds','game_bg_music.mp3')        #获取游戏运行时背景音乐路径
BULLET_SHOOT_SOUND = os.path.join(ASSETS_DIR,'sounds','bullet.wav')     #发射子弹时背景音乐路径
OUR_PLANE_IMG_1 = os.path.join(ASSETS_DIR,'images','hero1.png')         #获取我方飞机图片资源路径
OUR_PLANE_IMG_2 = os.path.join(ASSETS_DIR,'images','hero2.png')         #获取我方飞机图片资源路径
BULLET_IMG = os.path.join(ASSETS_DIR,'images','bullet1.png')            #子弹图片资源路径
