import pygame
import sys

from settings import Settings
from ship import Ship
import settings
class AlienInvasion:
    ##管理游戏资源和行为的类
    def __init__(self) -> None:
        pygame.init()    #用该函数初始化背景
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")    #游戏屏幕的标题

        self.ship=Ship(self)    ##创建一个新的ship实例，将这个实例赋给self.ship,Ship(self)中的self是主程序，他被当作实参传给了ship类中的ai_game
       
    def run_game(self):
    ##开始游戏主循环
        while True:
            self._check_events()    #指定变量名和要调用的方法
            self._update_screen()

            #每次循环重绘屏幕
    def _check_events(self):
            ##侦听键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        ##向右移动飞船
                        self.ship.rect.x+=1
                        
    def _update_screen(self):
        ##更新屏幕上的
            self.screen.fill(self.settings.bg_color) ##重绘屏幕
            self.ship.blitme()
            pygame.display.flip()
            self.clock.tick(60)

    
if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()


