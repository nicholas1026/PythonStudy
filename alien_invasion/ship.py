import pygame

class Ship():

    def __init__(self,ai_settings,screen):
        self.screen=screen
        self.ai_settings=ai_settings

        #加载飞船并获取其外接矩形
        self.image=pygame.image.load('ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.centery=self.screen_rect.centery

        #在飞船的属性center中存储小数值
        self.center1=float(self.rect.centerx)
        self.center2=float(self.rect.centery)

        #是否移动的标志
        self.move_right=False
        self.move_left=False
        self.move_up=False
        self.move_down=False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center1 += self.ai_settings.ship_speed_factor
        elif self.move_left and self.rect.left > 0:
            self.center1 -= self.ai_settings.ship_speed_factor


        if self.move_up and self.rect.top >0:
            self.center2 -= self.ai_settings.ship_speed_factor
        elif self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.center2 += self.ai_settings.ship_speed_factor


        self.rect.centerx=self.center1
        self.rect.centery=self.center2
