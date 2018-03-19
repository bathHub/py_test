

class car:
    def __init__(self,weight,name,color):
        self.color=color
        self.weight=weight
        self.name=name
        self.high=2

    def describe(self):
        print ("这个汽车的名字是:"+str(self.name)+"重量是:"+str(self.weight))

my_car = car('23','benq','yellow')
my_car.describe()
 
