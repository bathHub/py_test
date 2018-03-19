import car
class oil_car(car):
    def __init__(self,name,color,weight,size=70):
        car.__init__(name,color,weight)
        self.size=size
    def desc(self):
        print(str(self.name)+str(self.weight)+str(self.size))
mycar=oil_car('audi',"yello","122")
mycar.desc()
