
from random import choice
Class RandomWalk():
   "一个生成随机漫步数据的类"
Class RandomWalk():

    def __init__(self,num_points=5000):
       "初始化随机漫步的属性"
        self.num_points=num_points

       #所有随机漫步都始于(0,0)
        self.x_values=[0]
        self.y_values=[0]
