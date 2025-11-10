import pygame
import sys
class AlienInvasion:
    ##管理游戏资源和行为的类
    def __init__(self) -> None:
        pygame.init()    #用该函数初始化背景
        self.clock=pygame.time.Clock
        self.screen=pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")    #游戏屏幕的标题
        self.bg_color=(230,230,230)
    def run_game(self):
    ##开始游戏主循环
        while True:
            ##侦听键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color) ##重绘屏幕
            pygame.display.flip()
            self.clock.tick(60)
    
if __name__=='_main_':
    ai=AlienInvasion()
    ai.run_game()


