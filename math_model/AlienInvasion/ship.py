import pygame
class Ship:
    ##管理飞船的类
    def __init__(self,ai_game):
        ##初始化飞船和位置
        self.screen=ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()
        ##加载飞船图像，获取飞船的外接矩形
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()

        ##每艘飞船在屏幕底部的中央
        self.rect.midbottom=self.screen_rect.midbottom
        ##飞船属性x中存储一个浮点数
        self.x=float(self.rect.x)
        self.moving_left=False
        self.moving_right=False    ##飞船一开始不移动
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x +=self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -=self.settings.ship_speed
    def blitme(self):
        ##在指定位置绘制飞船图像
        self.screen.blit(self.image,self.rect)
    