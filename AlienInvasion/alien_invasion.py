import pygame
import sys

from settings import Settings
import settings
class AlienInvasion:
    ##管理游戏资源和行为的类
    def __init__(self) -> None:
        pygame.init()    #用该函数初始化背景
        self.clock=pygame.time.Clock
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")    #游戏屏幕的标题
       
    def run_game(self):
    ##开始游戏主循环
        while True:
            ##侦听键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings,self.bg_color) ##重绘屏幕
            pygame.display.flip()
            self.clock.tick(60)
    
if __name__=='_main_':
    ai=AlienInvasion()
    ai.run_game()


