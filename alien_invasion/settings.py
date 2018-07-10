class Settings():
    """存储游戏的所有设置"""

    def __init__(self):
        #屏幕设置
        self.screen_width=800
        self.screen_height=600
        self.bg_color=(255,255,255)
        self.ship_speed_factor=1

        #子弹设置
        self.bullet_speed_factor=1
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=300
