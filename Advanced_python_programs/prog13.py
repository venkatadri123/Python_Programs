# Create square class and derive rectangle from it, display their area.
class square:
    def __init__(self,x):
        self.x=x
    def area(self):
        print('area=',self.x*self.x)

class rect(square):
    def __init__(self,x,y):
        super().__init__(x)
        self.y=y
    def area(self):
        super().area()
        print('area of rectangle=',self.x*self.y)
r=rect(10,25)
r.area()
