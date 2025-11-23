from random import choice

class Randomwalk:
    def __init__(self,num_points=5000) -> None:
        self.num_points=num_points
        #随机从原点开始,用两个列表分别储存x，y的坐标
        self.x_value = [0]
        self.y_value = [0]

    def fill_work(self):
        while len(self.x_value) < self.num_points:

            x_direction=choice([-1,1])  #用来表示向正or负坐标轴移动
            x_distance=choice([1,2,3,4])  #移动多少距离
            x_move=x_direction * x_distance

            y_direction=choice([-1,1])  #用来表示向正or负坐标轴移动
            y_distance=choice([1,2,3,4])  #移动多少距离
            y_move=y_direction * y_distance

            #点不会在原地重复
            if x_move == 0 and y_move ==0:
                continue
            
            x = self.x_value[-1] + x_move
            y = self.y_value[-1] + y_move

            self.x_value.append(x)
            self.y_value.append(y)


            

            


