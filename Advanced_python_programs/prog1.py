# Creating class and Object.

class person:
    def __init__(self,a,b):
        self.name=a
        self.age=b
    def talk(self):
        print('my name is %s' %self.name)
        print('my age is %d' %self.age)
x=input("enter name:")
y=int(input('enter age:'))
p1=person(x,y)
p1.talk()

