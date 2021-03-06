import sys
import pygame
from bullet import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """响应键盘按下事件"""
    if event.key==pygame.K_RIGHT:
        ship.move_right=True
    elif event.key==pygame.K_LEFT:
        ship.move_left=True
    elif event.key==pygame.K_UP:
        ship.move_up=True
    elif event.key==pygame.K_DOWN:
        ship.move_down=True
    elif event.key==pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key==pygame.K_q:
        sys.exit()

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
        #print("K_DOWN")

def check_events(ai_settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship,alien,bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)

    #重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.blitme()

    #让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()

    #删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)

def fire_bullet(ai_settings,screen,ship,bullets):
    if  len(bullets) < ai_settings.bullets_allowed:
        new_bullet=Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
