import sys
import pygame

def check_keydown_events(event,ship):
    """响应键盘按下事件"""
    if event.key==pygame.K_RIGHT:
        ship.move_right=True
    elif event.key==pygame.K_LEFT:
        ship.move_left=True
    elif event.key==pygame.K_UP:
        ship.move_up=True
    elif event.key==pygame.K_DOWN:
        ship.move_down==True

def check_keyup_events(event,ship):
    """响应键盘松开事件"""
    if event.key==pygame.K_RIGHT:
        ship.move_right=False
    elif event.key==pygame.K_LEFT:
        ship.move_left=False
    elif event.key==pygame.K_UP:
        ship.move_up=False
    elif event.key==pygame.K_DOWN:
        ship.move_down=False

def check_events(ship):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #让最近绘制的屏幕可见
    pygame.display.flip()
