import pygame
class Ship:
    ##管理飞船的类
    def __init__(self,ai_game):
        ##初始化飞船和位置
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()

        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()

        ##每艘飞船在屏幕底部的中央
        self.rect.midbottom=self.screen_rect.midbottom
        self.moving_right=False
    def update(self):
        if self.moving_rignt:
            self.rect.x +=1

    def blitme(self):
        ##在指定位置绘制飞船图像
        self.screen.blit(self.image,self.rect)
    